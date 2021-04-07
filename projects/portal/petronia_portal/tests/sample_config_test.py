"""Test out sample config parsing."""

import unittest
from petronia_common.util.yaml_support import load_yaml_documents
from ..entrypoint import parse_config


CONFIG_1 = """
config:
  default_window_behavior:
    - match:
        - key: executable
          match_type: glob
          value: "*firefox*"
      managed: true
      fit:
        justify_horizontal: left
        justify_vertical: top
        fit_horizontal: fit
        fit_vertical: fit
      initial_portal: default
  
  workspaces:
    # Layout 1: 1 screen.
    - name: 1 screen
      screens:
        - block:
            x: 0
            y: 0
            width: 1024
            height: 768
          layout:
            size: 1
            direction: horizontal
            contents:
            - ^: portal
              $:
                portal_aliases: ['default']
                size: 2
                preferred_location:
                  justify_horizontal: left
                  justify_vertical: top
                  fit_horizontal: shrink
                  fit_vertical: shrink
                padding_top: 0
                padding_bottom: 0
                padding_left: 0
                padding_right: 0
            - ^: split
              $:
                size: 1
                direction: vertical
                contents:
                  - ^: portal
                    $:
                      portal_aliases: ['default']
                      size: 3
                      preferred_location:
                        justify_horizontal: right
                        justify_vertical: top
                        fit_horizontal: fit
                        fit_vertical: fit
                      padding_top: 0
                      padding_bottom: 0
                      padding_left: 0
                      padding_right: 0
                  - ^: portal
                    $:
                      portal_aliases: ['default']
                      size: 2
                      preferred_location:
                        justify_horizontal: right
                        justify_vertical: bottom
                        fit_horizontal: shrink
                        fit_vertical: shrink
                      padding_top: 0
                      padding_bottom: 0
                      padding_left: 0
                      padding_right: 0
"""


class SampleConfigTest(unittest.TestCase):
    """Test out sample configurations."""

    def test_config_1(self) -> None:
        """Test CONFIG_1"""
        res = load_yaml_documents(CONFIG_1)
        self.assertIsNone(res.error)
        self.assertEqual(len(res.result), 1)
        raw_data = res.result[0]
        assert isinstance(raw_data, dict)  # nosec
        raw_data = raw_data.get('config')
        assert isinstance(raw_data, dict)  # nosec
        config_res = parse_config(raw_data)
        self.assertIsNone(config_res.error)
