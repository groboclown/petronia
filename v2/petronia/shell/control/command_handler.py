
from ...system.component import Component, Identifiable
from ...system import event_ids
from ...system import target_ids
from ...script.command import Command


# noinspection PyUnusedLocal
def command_handler_factory(bus, config, id_manager):
    CommandHandler(bus, config)


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
        assert isinstance(request, tuple)
        name = request[0]
        args = request[1:]
        for cmd in self.__config.commands.commands:
            assert isinstance(cmd, Command)
            if cmd.matches(name):
                try:
                    cmd.invoke(self.__bus, args)
                except BaseException as e:
                    self._log_error("OnCommand failed: '{0}'".format(request), e)
                return
        self._log_error("CONFIG No such registered command {0} (request: {1})".format(name, request))
