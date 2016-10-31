
from ...system.component import Component, Identifiable
from ...system import event_ids
from ...system import target_ids
from ...script.command import Command


class CommandHandler(Identifiable, Component):
    def __init__(self, bus, config):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.CONTROL_MANAGER)
        self.__bus = bus
        self.__config = config

        self._listen(event_ids.USER__COMMAND, target_ids.ANY, self._on_command)

    # noinspection PyUnusedLocal
    def _on_command(self, event_id, target_id, obj):
        request = obj['command']
        name, args = self._split_command(request)
        for cmd in self.__config.commands.commands:
            assert isinstance(cmd, Command)
            if cmd.matches(name):
                try:
                    cmd.invoke(self.__bus, args)
                except BaseException as e:
                    self._log_error("OnCommand failed: '{0}'".format(request, e))
                return
        self._log_error("CONFIG No such registered command {0} (request: {1})".format(name, request))

    @staticmethod
    def _split_command(request):
        request = request.strip()
        args = request.split(',')
        pos = args[0].strip().find(' ')
        if pos > 0:
            name = args[0][:pos].strip().lower()
            ret_args = [args[0][pos:].strip()]
        else:
            name = args[0]
            ret_args = []
        for arg in args[1:]:
            ret_args.append(arg.strip())
        return name, ret_args

