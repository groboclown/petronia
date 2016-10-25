
from . import event_ids
from . import target_ids
from .component import MarshalableComponent, Identifiable


LEVEL_DEBUG = 0
LEVEL_VERBOSE = 10
LEVEL_INFO = 20
LEVEL_WARN = 30
LEVEL_ERROR = 40
LEVEL_FATAL = 50

LOG_LEVELS = {
    "DEBUG": LEVEL_DEBUG,
    "VERBOSE": LEVEL_VERBOSE,
    "INFO": LEVEL_INFO,
    "WARN": LEVEL_WARN,
    "ERROR": LEVEL_ERROR,
    "FATAL": LEVEL_FATAL
}


class Logger(Identifiable, MarshalableComponent):
    def __init__(self, bus, threshold=LEVEL_DEBUG):
        MarshalableComponent.__init__(self, bus)
        Identifiable.__init__(self, target_ids.LOGGER)

        self.__level = threshold
        self._listen(event_ids.LOG__DEBUG, target_ids.LOGGER, lambda e, t, o: self.debug(*self.__as_args(o)))
        self._listen(event_ids.LOG__VERBOSE, target_ids.LOGGER, lambda e, t, o: self.verbose(*self.__as_args(o)))
        self._listen(event_ids.LOG__INFO, target_ids.LOGGER, lambda e, t, o: self.info(*self.__as_args(o)))
        self._listen(event_ids.LOG__WARN, target_ids.LOGGER, lambda e, t, o: self.warn(*self.__as_args(o)))
        self._listen(event_ids.LOG__ERROR, target_ids.LOGGER, lambda e, t, o: self.error(*self.__as_args(o)))
        self._listen(event_ids.LOG__FATAL, target_ids.LOGGER, lambda e, t, o: self.fatal(*self.__as_args(o)))

    def debug(self, message, ex=None):
        self.__do_log(LEVEL_DEBUG, message, ex)

    def verbose(self, message, ex=None):
        self.__do_log(LEVEL_VERBOSE, message, ex)

    def info(self, message, ex=None):
        self.__do_log(LEVEL_INFO, message, ex)

    def warn(self, message, ex=None):
        self.__do_log(LEVEL_WARN, message, ex)

    def error(self, message, ex=None):
        self.__do_log(LEVEL_ERROR, message, ex)

    def fatal(self, message, ex=None):
        self.__do_log(LEVEL_FATAL, message, ex)
        self._fire(event_ids.SYSTEM__QUIT, target_ids.ANY, {})

    def set_level(self, level):
        if isinstance(level, str) and level in LOG_LEVELS:
            self.__level = LOG_LEVELS[level]
        elif isinstance(level, int):
            self.__level = level
        else:
            self.warn("Unknown logging level {0}".format(level))

    def __do_log(self, level, message, ex):
        if level > self.__level:
            # TODO real logging
            if ex is None:
                print("[{0}] {1}".format(level, message))
            else:
                print("[{0}] {1} {2}".format(level, message, ex))

    @staticmethod
    def __as_args(event_obj):
        ret = []
        if "message" in event_obj:
            ret.append(event_obj["message"])
        elif "msg" in event_obj:
            ret.append(event_obj["msg"])
        else:
            ret.append("<no message>")

        if "exception" in event_obj:
            ret.append(event_obj["exception"])
        elif "error" in event_obj:
            ret.append(event_obj["error"])
        elif "ex" in event_obj:
            ret.append(event_obj["ex"])
        else:
            ret.append(None)

        return ret
