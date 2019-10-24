
# mypy: allow-any-expr
# mypy: allow-any-generics
# mypy: allow-any-explicit

"""
Creates extension event API documentation.
"""

from typing import Tuple, Sequence, List, Optional
import os
import sys
import re
import argparse
import importlib
import datetime
import traceback
import collections.abc
BINDIR = os.path.dirname(sys.argv[0])
BASEDIR = os.path.join(BINDIR, os.path.pardir)
SRCDIR = os.path.join(BASEDIR, "src")
sys.path.append(SRCDIR)
from petronia.base.events.bootstrap import bootstrap_core_events
from petronia.base.bus import EventBus, ListenerId, EventId, ListenerRegistrar, EventCallback
from petronia.base.participant import ComponentId, ParticipantId
from petronia.base.util import T
from petronia.base.events.bus import RegisterEventEvent, EVENT_ID_REGISTER_EVENT
from petronia.base.bus import (QUEUE_EVENT_HIGH, QUEUE_EVENT_IO)
from petronia.base.util.serial import add_repr
from petronia.core.state.api import StateStoreUpdatedEvent, EVENT_ID_UPDATED_STATE
from petronia.core.config_persistence.api import PersistentConfigurationState
from petronia.core.hotkeys.api import (
    HotkeyBoundServiceAnnouncementEvent, EVENT_ID_HOTKEY_BOUND_SERVICE_ANNOUNCEMENT,
    BoundServiceActionSchema,
)
from petronia.defimpl.extensions.defs.discover_types import DiscoveredExtension
from petronia.base.util.simple_type import (
    PersistTypeSchemaItem,
    PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA,
    PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT,
    PERSISTENT_TYPE_SCHEMA_TYPE__ID,
    PERSISTENT_TYPE_SCHEMA_TYPE__REF,
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_TYPE__BOOL,
    PERSISTENT_TYPE_SCHEMA_TYPE__ANY,
    PERSISTENT_TYPE_SCHEMA_NAME__DOC,
)

NOW = datetime.datetime.utcnow().utcnow().strftime("%Y-%b-%d")


class Config:
    def __init__(self, src_dir: str, dest_dir: str, template_dir: str) -> None:
        self.src_dir = src_dir
        self.dest_dir = dest_dir
        self.template_dir = template_dir


def mk_base(config: Config) -> None:
    """Create the documentation for the `petronia.base` tree.  It's very special."""
    events = []
    for event in bootstrap_core_events():
        # Returns a list of event_id, priority, event object, event object example
        events.append(create_event_data(RegisterEventEvent(*event)))
    data = {
        "now": NOW,
        "events": events,
        "has_events": len(events) > 0,
    }
    write_template(config, "base.template.md", "base.md", data)


def mk_built_in(config: Config) -> List[dict]:
    """Create the core API documentation"""
    found = []
    for search_dir in ('petronia/core', 'petronia/defimpl'):
        for fqn, mod_name in find_dir_module(os.path.join(config.src_dir, search_dir), config.src_dir):
            try:
                mod = importlib.import_module(mod_name)
            except BaseException as err:
                # Could be an OS compatibility issue...
                print("Skipping {0}: {1}".format(mod_name, err))
                # traceback.print_exception(type(err), err, err.__traceback__)
                continue
            if hasattr(mod, 'EXTENSION_METADATA') and hasattr(mod, 'start_extension'):
                # print(fqn)
                md = getattr(mod, 'EXTENSION_METADATA')
                starter = getattr(mod, 'start_extension')
                config_schema = None
                if hasattr(mod, 'CONFIG_SCHEMA'):
                    print("!! {0}".format(mod_name))
                    config_schema = getattr(mod, 'CONFIG_SCHEMA')
                else:
                    print("No configuration schema in {0}".format(mod_name))
                document_extension(config, fqn, mod, starter, md, config_schema)
                found.append({
                    "name": md['name'],
                    "version": "{0}.{1}.{2}".format(*md['version']),
                    "doc": clean_doc_str(mod.__doc__, True),
                })

    write_template(config, "README.template.md", "README.md", {
        "now": NOW,
        "extensions": found,
    })
    return found


def find_dir_module(basedir, relative_to):
    basedir = os.path.abspath(basedir)
    relative_to = os.path.abspath(relative_to)
    if not relative_to[-1] == os.path.sep:
        relative_to = relative_to + os.path.sep
    root_len = len(relative_to)
    for dirpath, dirnames, filenames in os.walk(basedir):
        for dn in dirnames:
            full = os.path.join(dirpath, dn)
            yield full, full[root_len:].replace(os.path.sep, '.')


def document_extension(config: Config, fqn, mod, starter, md, schema):
    if 'name' not in md:
        raise ValueError('no "name" in ' + fqn)
    name = md['name']
    version = (1, 0, 0,)
    if 'version' in md:
        version = md['version']
    secure_version = (True, tuple(version),)
    ext_doc = clean_doc_str(mod.__doc__)
    ext = DiscoveredExtension(name, secure_version, md, no_op_loader)
    bus = MockEventBus()
    starter(bus)
    if ext.is_api:
        prefix = "api"
    elif ext.is_implementation:
        prefix = "impl"
    elif ext.is_standalone:
        prefix = "standalone"
    else:
        raise ValueError('unknown extension type {0}'.format(fqn))

    # print("{0} <- {1}".format(fqn, name))
    write_template(
        config, prefix + '.template.md', name + '.md', create_data(
            config, ext, ext_doc, bus.events, bus.listens, schema, bus.bound, bus.states
        )
    )


def create_data(config, ext, ext_doc, events, listens, schema, bound, states):
    dep_data = [create_compat_data(dep) for dep in ext.depends_on]
    impl_data = [create_compat_data(impl) for impl in ext.implements]
    defaults_data = [create_compat_data(default) for default in ext.defaults]
    event_data = [create_event_data(event) for event in events]

    return {
        "name": ext.name,
        "version": "{0}.{1}.{2}".format(*ext.version),
        "summary": ext.description,
        "doc": ext_doc,
        "authors": ', '.join(ext.authors or []),
        "license": ext.license or '(not specified)',
        "secure_text": ext.is_secure and 'elevated privileges' or 'private sandbox',
        "depends": dep_data,
        "has_depends": len(dep_data) > 0,
        "implements": impl_data,
        "has_implements": len(impl_data) > 0,
        "defaults": defaults_data,
        "has_defaults": len(defaults_data) > 0,
        "events": event_data,
        "has_events": len(event_data) > 0,
        "listens_to": listens,
        "has_listens_to": len(listens) > 0,
        "configuration": create_schema_str(config, 'configuration.template.md', ext.name, schema),
        "has_config": schema is not None,
        "now": NOW,
        "binding": create_bindings(config, bound),
        "has_binding": len(bound) > 0,
        "states": create_states(config, ext.name, states),
        "has_states": len(states) > 0,
    }


def create_compat_data(dep):
    compat = "no version restriction"
    if dep.minimum is not None and dep.minimum[0] >= 0:
        compat = "at least version {0}.{1}.{2}".format(dep.minimum[0], dep.minimum[1], dep.minimum[2])
        if dep.below is not None and dep.below[0] >= 0:
            compat += ", but not greater than {0}.{1}.{2}".format(
                dep.below[0], dep.below[1], dep.below[2]
            )
    elif dep.below is not None and dep.below[0] >= 0:
        compat = "any version below {0}.{1}.{2}".format(*dep.below)
    return {
        "name": dep.name,
        "compat": compat,
    }


def create_event_data(event: RegisterEventEvent):
    if event.priority == QUEUE_EVENT_IO:
        pri = 'I/O'
    elif event.priority == QUEUE_EVENT_HIGH:
        pri = 'high'
    else:
        pri = 'normal'
    return {
        "event_id": event.event_id,
        "priority": pri,
        "type": event.event_class.__module__ + '.' + event.event_class.__name__,
        "doc": clean_doc_str(event.event_class.__doc__),
        "produce": "public" if event.protection.public_produce else "private",
        "consume": "public" if event.protection.public_consume else "private",
        "produce_text": (
            "Public triggering allowed" if event.protection.public_produce else "Only instance triggering permitted"
        ),
        "consume_text": (
            "Public listening allowed" if event.protection.public_consume else "Only instance listening permitted"
        ),
    }


def create_bindings(config: Config, bindings: List[BoundServiceActionSchema]):
    ret = []
    for bound in bindings:
        ret.append({
            "action": bound.action,
            "service": bound.service,
            "schema": create_schema_str(config, 'hotkey.template.md', bound.action, bound.parameters or {}, 'bind')
        })
    return ret


def create_states(config: Config, mod_name: str, states: List[StateStoreUpdatedEvent]):
    ret = []
    for state in states:
        if state.state and isinstance(state.state, PersistentConfigurationState):
            # External Config
            pass
        else:
            # Internal State
            pass
    return ret


def clean_doc_str(doc, overview=False):
    """
    Transform a Python doc string into a Markdown string.

    First, it finds the indentation of the whole block.  It's assumed that
    everything in the block shares the same basic indentation.

    Any line that starts with ":" is considered to be Python meta-information,
    and is stripped out.  If the line following the ":" has the same indention
    and is not whitespace, it too is stripped out.

    For markdown support, lines with the same indention immediately after each
    other are considered to be the same line, and are joined together.
    """
    doc = doc or ''
    ret = ''
    current = ''
    base_indent = 0
    prev_indent = 0
    strip_prev = False

    def get_indent(val: str) -> int:
        ind = 0
        while ind < len(val) and val[ind].isspace():
            ind += 1
        if ind >= len(val):
            return 0
        return ind

    for o_line in doc.splitlines():
        line = o_line.rstrip()
        curr_indent = get_indent(line)

        # Check for Python meta-data
        if line and line.lstrip()[0] == ':':
            prev_indent = curr_indent
            strip_prev = True
            continue
        if curr_indent == prev_indent and strip_prev:
            continue

        if not ret and line:
            # First non-empty line.
            base_indent = get_indent(line)
            prev_indent = base_indent
            current += line[base_indent:]
            continue

        if not line:
            # Empty line
            if current:
                if ret and overview:
                    return ret.lstrip()
                ret += '\n\n' + current
                current = ''
            # leave the previous indent the same.
            continue

        current += '\n' + line[base_indent:].lstrip()

    if current:
        ret += '\n\n' + current
    if not ret:
        ret = '(no documentation provided)'
    return ret.lstrip()


def create_schema_str(
        config: Config, template_name: str, ext_name: str, schema: Optional[dict], default_name: str = 'Configuration'
) -> Optional[str]:
    if not schema:
        return None

    if PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA in schema:
        item = schema[PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA]
        assert isinstance(item, PersistTypeSchemaItem)
        assert item.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__ID
        name = item.description
    else:
        name = default_name

    doc_data = schema.get(
        PERSISTENT_TYPE_SCHEMA_NAME__DOC,
        PersistTypeSchemaItem('(no documentation)', PERSISTENT_TYPE_SCHEMA_TYPE__STR)
    )
    if isinstance(doc_data, PersistTypeSchemaItem):
        doc = clean_doc_str(doc_data.description)
    else:
        doc = ''

    layout = ''
    parts = []
    children_parts = []
    for key, val in schema.items():
        kid_layout, kid_parts, grandkid_parts = inner_schema_part_str(name + '.properties', key, '    ', val)
        layout += kid_layout
        parts.extend(kid_parts)
        children_parts.extend(grandkid_parts)
    parts.extend(children_parts)

    all_parts = []
    seen = set()
    for part in parts:
        if part['key'] not in seen:
            seen.add(part['key'])
            all_parts.append(part)

    return transform_template(config, template_name, {
        "ext_name": ext_name,
        "doc": doc,
        "layout": layout,
        "parts": all_parts,
    })


def inner_schema_part_str(name, key, indent, val) -> Tuple[str, Sequence[dict], Sequence[dict]]:
    assert isinstance(key, str)
    if key in (PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA, PERSISTENT_TYPE_SCHEMA_NAME__DOC,):
        return '', [], []
    if key == '':
        pref = indent + '-'
        key = '[]'
        name += '[]'
    else:
        pref = indent + key + ':'
        name += '.' + key
    if isinstance(val, PersistTypeSchemaItem):
        if val.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__ANY:
            layout = pref + ' (any type)\n'
        elif val.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__BOOL:
            layout = pref + ' (true / false)\n'
        elif val.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__STR:
            layout = pref + ' "text"\n'
        elif val.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT:
            layout = pref + ' (some number)\n'
        elif val.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__REF:
            layout = pref + '\n' + indent + '  (a "' + val.description + '" sub-schema value)\n'
        else:
            layout = pref + ' (unknown)\n'
        return layout, [{"key": name, "desc": val.description}], []

    if isinstance(val, collections.abc.Mapping):
        layout = pref + '\n'
        if PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA in val:
            item = val[PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA]
            assert isinstance(item, PersistTypeSchemaItem)
            assert item.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__ID
            name = item.description
            layout += indent + '  # Sub-Schema Definition: ' + name + '\n'
        doc = str(val.get(PERSISTENT_TYPE_SCHEMA_NAME__DOC, ''))
        if doc:
            parts = [{"key": name, "desc": doc}]
        else:
            parts = []
        grandkid_parts = []
        for subkey, subval in val.items():
            kid_layout, kid_parts, gkp = inner_schema_part_str(name, subkey, indent + '  ', subval)
            layout += kid_layout
            parts.extend(kid_parts)
            grandkid_parts.extend(gkp)
        return layout, parts, grandkid_parts
    elif isinstance(val, collections.abc.Iterable):
        # A list of one or more of these types
        layout = pref + '\n' + indent + '  # one or more of these types\n'
        parts = []
        grandkid_parts = []
        for kid in val:
            # Better key name?
            kid_layout, kid_parts, gkp = inner_schema_part_str(name, '', indent + '  ', kid)
            layout += kid_layout
            parts.extend(kid_parts)
            grandkid_parts.extend(gkp)
        return layout, parts, grandkid_parts
    else:
        print("{0} has unknown schema key {1} value {2}".format(name, key, repr(val)))
        return '', [], []


def no_op_loader(_bus):
    raise NotImplementedError()


def write_template(config: Config, base_template_name, outfile_name, data) -> None:
    if outfile_name[0] == '/':
        raise ValueError(outfile_name, data)
    if not os.path.exists(config.dest_dir):
        os.makedirs(config.dest_dir)
    outfile = os.path.abspath(os.path.join(config.dest_dir, outfile_name))
    # print("{0} -> {1} ({2} / {3})".format(base_template_name, outfile, config.dest_dir, outfile_name))
    with open(outfile, 'w') as out:
        out.write(transform_template(config, base_template_name, data))


_IMPORT_MATCH = re.compile(r'{#([^:]+):([^#]+)#\}')


def transform_template(config, template_name, data) -> str:
    """A trivial template language.

    {#key:template#} is replaced with an included template file.  The "key" is the internal
    data in the data structure which is used as the data in the included template file.  If the
    key is a list, then the key's is looped through, using that index's data for the template file.
    If the key's value is a boolean value, then the template file is imported only if it's true, or,
    if the template has a ',' in the name, then true -> template in first half, false -> template in
    second half.
    """
    src_template_file = os.path.join(config.template_dir, template_name)
    with open(src_template_file, 'r') as inp:
        template = inp.read()
    ret = ''
    start = 0
    while start < len(template):
        # print("{0} :: {1}".format(template_name, start))
        m = _IMPORT_MATCH.search(template, start)
        if not m:
            break
        ret += template[start:m.start()].format(**data)
        key = m.group(1)
        template_file = m.group(2)
        if isinstance(data[key], dict):
            # print(" ** {1} [{0}]".format(key, template_file))
            ret += transform_template(config, template_file, data[key])
        elif isinstance(data[key], bool):
            if ',' in template_file:
                if data[key]:
                    tfn = template_file[0:template_file.find(',')]
                    # print(" ** True {0}".format(tfn))
                    ret += transform_template(config, tfn, data)
                else:
                    tfn = template_file[template_file.find(',') + 1:]
                    # print(" ** False {0}".format(tfn))
                    ret += transform_template(config, tfn, data)
            elif data[key]:
                # print(" ** (True) {0}".format(template_file))
                ret += transform_template(config, template_file, data)
        else:
            for val in data[key]:
                # print(" ** [] {1} [{0}]".format(key, template_file))
                ret += transform_template(config, template_file, val)
        start = m.end()
    if start < len(template):
        ret += template[start:].format(**data)
    return ret


class MockEventBus(EventBus):
    def __init__(self) -> None:
        self.events = []
        self.listens = []
        self.states = []  # type: List[StateStoreUpdatedEvent]
        self.bound = []  # type: List[BoundServiceActionSchema]

    def add_listener(
            self,
            target_id: ParticipantId,
            listener_setup: ListenerRegistrar[T],
            listener: EventCallback[T]
    ) -> ListenerId:
        ls, cb = listener_setup(None)
        self.listens.append({
            "target": target_id,
            "event_id": ls,
        })
        return ListenerId(0)

    def remove_listener(self, listener_id: ListenerId) -> bool:
        """De-register the listener."""
        return True

    def trigger(self, event_id: EventId, target_id: ParticipantId, event_obj: T) -> None:
        """
        Triggers an event to fire.  The event priority is based upon the
        event id registration.
        """
        if event_id == EVENT_ID_REGISTER_EVENT:
            assert isinstance(event_obj, RegisterEventEvent)
            self.events.append(event_obj)
        elif event_id == EVENT_ID_UPDATED_STATE:
            assert isinstance(event_id, StateStoreUpdatedEvent)
            self.states.append((target_id, event_obj,))
        elif event_id == EVENT_ID_HOTKEY_BOUND_SERVICE_ANNOUNCEMENT:
            assert isinstance(event_obj, HotkeyBoundServiceAnnouncementEvent)
            self.bound.append(event_obj.schema)

    def create_component_id(self, component_category: str) -> ComponentId:
        # Essentially ignore
        return ComponentId((component_category, 1))


def main():
    add_repr(RegisterEventEvent)
    petronia_base_dir = os.path.join(os.path.dirname(sys.argv[0]), os.path.pardir)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--src", default=SRCDIR,
        help="Petronia source directory"
    )
    parser.add_argument(
        "--dest", default=os.path.join(petronia_base_dir, "docs/extensions/api"),
        help="Documentation output directory"
    )
    parser.add_argument(
        "--template", default=os.path.join(BINDIR, "doc_templates"),
        help="Documentation template directory"
    )
    args = parser.parse_args()
    config = Config(
        src_dir=args.src,
        dest_dir=args.dest,
        template_dir=args.template
    )
    mk_base(config)
    mk_built_in(config)
    return 0


if __name__ == '__main__':
    sys.exit(main())
