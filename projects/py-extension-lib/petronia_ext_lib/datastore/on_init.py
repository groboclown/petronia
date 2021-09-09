"""
Very common patterns involving initialization.
"""

from typing import Dict, List, Callable, Optional, Generic, Any
import threading
from petronia_common.util import StdRet, T, join_none_results, RET_OK_NONE
from . import listen, send
from ..runner.registry import (
    EventRegistryContext, ContextEventObjectTarget, EventObjectTarget,
    EventObjectParser,
)
from ..extension_loader import send_register_listeners
from ..events import timer as timer_event
from ..events import datastore as datastore_event


class InitCachedInstance(listen.CachedInstance[T]):
    """Cached instance that includes initialization state."""
    __slots__ = ('__initialized', '__data_id')

    def __init__(
            self,
            data_id: str,
            parser: Callable[[Dict[str, Any]], StdRet[T]],
            callback: Optional[Callable[[Optional[T]], None]],
    ) -> None:
        listen.CachedInstance.__init__(self, EventObjectParser(parser), callback)
        self.__data_id = data_id
        self.__initialized = False

    @property
    def data_id(self) -> str:
        """The target id for the data."""
        return self.__data_id

    def is_initialized(self) -> bool:
        """Is this instance initialized?"""
        return self.__initialized

    def on_delete(self) -> None:
        self.__initialized = True
        listen.CachedInstance.on_delete(self)

    def update(self, event: datastore_event.DataUpdateEvent) -> StdRet[None]:
        self.__initialized = True
        return listen.CachedInstance.update(self, event)


class CollectionCache(Generic[T]):
    """Stores data of a similar type whose ID starts with a prefix.  By its nature, these
    cannot be initialized (the ID isn't known until after it has been sent)."""
    __slots__ = ('__prefix', '__parser', '__callback', '__store')

    def __init__(
            # For now, a prefix; could be a regular expression.
            self, prefix: str,
            parser: Callable[[Dict[str, Any]], StdRet[T]],
            callback: Optional[Callable[[str, Optional[T]], StdRet[None]]],
    ) -> None:
        self.__prefix = prefix
        self.__parser = EventObjectParser(parser)
        self.__callback = callback
        self.__store: Dict[str, T] = {}

    @property
    def prefix(self) -> str:
        """The target prefix"""
        return self.__prefix

    def is_target_match(self, target_id: str) -> bool:
        """Is the target ID a match against this cache?"""
        return target_id.startswith(self.__prefix)

    def get(self, target_id: str) -> Optional[T]:
        """Get the value from the data store."""
        return self.__store.get(target_id)

    def on_delete(self, target_id: str) -> StdRet[None]:
        """Called when the matching target ID is reported as deleted."""
        if target_id in self.__store:
            del self.__store[target_id]
            if self.__callback:
                self.__callback(target_id, None)
        return RET_OK_NONE

    def update(self, target_id: str, event: datastore_event.DataUpdateEvent) -> StdRet[None]:
        """Called when the data for the target is reported as added or updated."""

        parsed = listen.get_event_data_value(event, self.__parser)
        if parsed.has_error:
            return parsed.forward()
        if parsed.value is None and target_id in self.__store:
            del self.__store[target_id]
        if parsed.value is not None:
            self.__store[target_id] = parsed.value
        if self.__callback:
            return self.__callback(target_id, parsed.value)
        return RET_OK_NONE


class CacheStore:
    """A collection of caches which may need to be initialized."""
    __slots__ = (
        '__caches', '__collection_caches', '__lock', '__extension_name',
        '__error_result_handler',
    )

    def __init__(
            self,
            extension_name: str,
            error_result_handler: Optional[Callable[[StdRet[None]], None]] = None,
    ) -> None:
        self.__extension_name = extension_name
        self.__caches: Dict[str, InitCachedInstance[Any]] = {}
        self.__collection_caches: List[CollectionCache[Any]] = []
        self.__error_result_handler = error_result_handler or (lambda x: None)
        self.__lock = threading.Lock()

    def register(self, context: EventRegistryContext) -> StdRet[None]:
        """Register this store with the datastore and heartbeat listeners."""
        return join_none_results(
            context.register_event_parser(
                datastore_event.DataUpdateEvent.FULL_EVENT_NAME,
                datastore_event.DataUpdateEvent.parse_data,
            ),
            context.register_event_parser(
                datastore_event.DataRemovedEvent.FULL_EVENT_NAME,
                datastore_event.DataRemovedEvent.parse_data,
            ),
            context.register_event_parser(
                timer_event.HeartbeatEvent.FULL_EVENT_NAME,
                timer_event.HeartbeatEvent.parse_data,
            ),
            context.register_target(
                datastore_event.DataUpdateEvent.FULL_EVENT_NAME,
                None,
                CacheStoreUpdateTarget(self),
            ),
            context.register_target(
                datastore_event.DataRemovedEvent.FULL_EVENT_NAME,
                None,
                CacheStoreDeleteTarget(self),
            ),
            context.register_target(
                timer_event.HeartbeatEvent.FULL_EVENT_NAME,
                timer_event.HeartbeatEvent.UNIQUE_TARGET_FQN,
                TransmitUninitializedTarget(context, self),
            ),

            send_register_listeners(context, self.__extension_name, (
                (
                    datastore_event.DataUpdateEvent.FULL_EVENT_NAME,
                    None,
                ),
                (
                    datastore_event.DataRemovedEvent.FULL_EVENT_NAME,
                    None,
                ),
                (
                    timer_event.HeartbeatEvent.FULL_EVENT_NAME,
                    timer_event.HeartbeatEvent.UNIQUE_TARGET_FQN,
                ),
            )),
        )

    def add_collection_cache(self, cache: CollectionCache[Any]) -> None:
        """Add the collection cache to the list.  These caches can overlap with instance caches
        and other named caches."""
        with self.__lock:
            self.__collection_caches.append(cache)

    def add_instance_cache(self, cache: InitCachedInstance[Any]) -> bool:
        """Add a cache to the list.  Only one cache with a data ID can be added.
        Returns True if there was a problem."""
        with self.__lock:
            if cache.data_id in self.__caches:
                return True
            self.__caches[cache.data_id] = cache
        return False

    def get_value(self, data_id: str, convert: Callable[[Any], T]) -> Optional[T]:
        """Get the cache's data.  It can be None if the data is deleted or not initialized or
        the data id is not registered.  This will scan instance caches first, then named
        caches."""
        with self.__lock:
            cache = self.__caches.get(data_id)
            if cache:
                return convert(cache.value)
            for coll in self.__collection_caches:
                if coll.is_target_match(data_id):
                    return convert(coll.get(data_id))
        return None

    def send_request_data_for_uninitialized(self, context: EventRegistryContext) -> StdRet[None]:
        """"Send the request data event for each cache that needs initialization."""
        res: List[StdRet[None]] = []
        with self.__lock:
            for cache in self.__caches.values():
                if not cache.is_initialized():
                    res.append(send.send_request_data_state(
                        context, self.__extension_name + ':data-requester', cache.data_id,
                    ))
            # collection caches are not in this state, so no send can be made.
        return join_none_results(*res)

    def handle_res(self, res: StdRet[Any]) -> None:
        """Handle res objects for errors."""
        if res.has_error:
            self.__error_result_handler(res.forward())

    def on_update(self, target_id: str, item: datastore_event.DataUpdateEvent) -> None:
        """Sends an update to the data item for the target id."""
        with self.__lock:
            cache = self.__caches.get(target_id)
            if cache:
                self.handle_res(cache.update(item))
            for coll in self.__collection_caches:
                if coll.is_target_match(target_id):
                    self.handle_res(coll.update(target_id, item))

    def on_delete(self, target_id: str) -> None:
        """Sends an update to the data item for the target id."""
        with self.__lock:
            cache = self.__caches.get(target_id)
            if cache:
                cache.on_delete()
            for coll in self.__collection_caches:
                if coll.is_target_match(target_id):
                    self.handle_res(coll.on_delete(target_id))


class TransmitUninitializedTarget(ContextEventObjectTarget[timer_event.HeartbeatEvent]):
    """Retransmit an event at every heartbeat until the value is True."""

    __slots__ = ('__cache_store',)

    def __init__(
            self, context: EventRegistryContext,
            cache_store: CacheStore,
    ) -> None:
        ContextEventObjectTarget.__init__(self, context)
        self.__cache_store: Optional[CacheStore] = cache_store

    def on_close(self) -> None:
        self.__cache_store = None
        ContextEventObjectTarget.on_close(self)

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: timer_event.HeartbeatEvent,
    ) -> bool:
        if self.__cache_store:
            self.__cache_store.handle_res(
                self.__cache_store.send_request_data_for_uninitialized(context)
            )
            return False
        return True


class CacheStoreUpdateTarget(EventObjectTarget[datastore_event.DataUpdateEvent]):
    """Handle datastore update announcements to the cache store."""

    __slots__ = ('__cache_store',)

    def __init__(self, cache_store: CacheStore) -> None:
        self.__cache_store: Optional[CacheStore] = cache_store

    def on_close(self) -> None:
        self.__cache_store = None

    def on_event(self, source: str, target: str, event: datastore_event.DataUpdateEvent) -> bool:
        if self.__cache_store:
            self.__cache_store.on_update(target, event)
            return False
        return True


class CacheStoreDeleteTarget(EventObjectTarget[datastore_event.DataRemovedEvent]):
    """Handle datastore delete announcements to the cache store."""

    __slots__ = ('__cache_store',)

    def __init__(self, cache_store: CacheStore) -> None:
        self.__cache_store: Optional[CacheStore] = cache_store

    def on_close(self) -> None:
        self.__cache_store = None

    def on_event(self, source: str, target: str, event: datastore_event.DataRemovedEvent) -> bool:
        if self.__cache_store:
            self.__cache_store.on_delete(target)
            return False
        return True
