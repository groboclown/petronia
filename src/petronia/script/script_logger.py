
from ..system import event_ids
from ..system import target_ids
from ..system.bus import Bus
import traceback


def create_bus_logger(bus):
    return SimpleLogger(bus)


class SimpleLogger(object):
    def __init__(self, bus):
        assert isinstance(bus, Bus)
        self._bus = bus

    def warn(self, msg, ex=None):
        self._bus.fire(event_ids.LOG__WARN, target_ids.LOGGER, {
            'message': msg,
            'exception': ex,
        })

    def error(self, msg, ex=None):
        self._bus.fire(event_ids.LOG__ERROR, target_ids.LOGGER, {
            'message': msg,
            'exception': ex,
        })


def create_stdout_logger():
    return StdoutLogger()


class StdoutLogger(object):
    def warn(self, msg, ex=None):
        self._log("WARNING", msg, ex)

    def error(self, msg, ex=None):
        self._log("ERROR", msg, ex)

    @staticmethod
    def _log(level, msg, ex):
        print("{0}: {1}".format(level, msg))
        if ex is not None:
            try:
                traceback.print_exception(ex, ex, ex)
            except BaseException:
                print("  {0} (no stacktrace available)".format(ex))
