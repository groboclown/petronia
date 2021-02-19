"""Test the module."""

import unittest
from .. import process_metrics


class ProcessMetricsTest(unittest.TestCase):
    """Test the functions and structures in the module."""

    def test_process_metrics(self) -> None:
        """Test the ProcessMetrics structure."""
        prm = process_metrics.ProcessMetrics(
            display_name='dn',
            service_name='sn',
            service_type='st',
            current_state='cs',
            controls_accepted=['ca', 'cb'],
            exit_code=5,
            service_exit_code=6,
            check_point=7,
            wait_time_millis_hint=8,
            process_id=9,
            flags=['a', 'b'],
        )
        self.assertEqual('dn', prm.display_name)
        self.assertEqual('sn', prm.service_name)
        self.assertEqual('st', prm.service_type)
        self.assertEqual('cs', prm.current_state)
        self.assertEqual(('ca', 'cb'), prm.controls_accepted)
        self.assertEqual(5, prm.exit_code)
        self.assertEqual(6, prm.service_exit_code)
        self.assertEqual(7, prm.check_point)
        self.assertEqual(8, prm.wait_time_millis_hint)
        self.assertEqual(9, prm.process_id)
        self.assertEqual(('a', 'b'), prm.flags)
