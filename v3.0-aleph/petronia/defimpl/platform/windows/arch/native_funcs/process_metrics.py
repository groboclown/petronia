
"""
Information for a process
"""

from typing import Sequence, Optional


class ProcessMetrics:
    __slots__ = (
        'display_name',
        'service_name',
        'service_type',
        'current_state',
        'controls_accepted',
        'exit_code',
        'service_exit_code',
        'check_point',
        'wait_time_millis_hint',
        'process_id',
        'flags',
    )

    def __init__(
            self,
            display_name: str,
            service_name: str,
            service_type: Optional[str],
            current_state: Optional[str],
            controls_accepted: Sequence[str],
            exit_code: int,
            service_exit_code: int,
            check_point: int,
            wait_time_millis_hint: int,
            process_id: int,
            flags: Sequence[str],

    ):
        self.display_name = display_name
        self.service_name = service_name
        self.service_type = service_type
        self.current_state = current_state
        self.controls_accepted = tuple(controls_accepted)
        self.exit_code = exit_code
        self.service_exit_code = service_exit_code
        self.check_point = check_point
        self.wait_time_millis_hint = wait_time_millis_hint
        self.process_id = process_id
        self.flags = tuple(flags)
