"""Test the module"""

import unittest
from .. import keymap


class KeymapTest(unittest.TestCase):
    """Test the module functions."""

    def test_vk_to_names(self) -> None:
        """Test vk_to_names"""
        self.assertEqual(
            ['#0xffffff'],
            keymap.vk_to_names(0xffffff),
        )
        self.assertEqual(
            {'return', 'enter', 'cr', 'lf'},
            set(keymap.vk_to_names(0x0d)),
        )

    def test_is_vk_modifier(self) -> None:
        """Test is_vk_modifier"""
        vk_code = keymap.STR_VK_MAP['a']
        self.assertFalse(keymap.is_vk_modifier(vk_code))
        vk_code = keymap.STR_VK_MAP['lshift']
        self.assertTrue(keymap.is_vk_modifier(vk_code))

    def test_is_specially_handled_vk_key(self) -> None:
        """Test is_specially_handled_vk_key"""
        vk_code = keymap.STR_VK_MAP['a']
        self.assertFalse(keymap.is_specially_handled_vk_key(vk_code))
        vk_code = keymap.STR_VK_MAP['rshift']
        self.assertFalse(keymap.is_specially_handled_vk_key(vk_code))
        vk_code = keymap.STR_VK_MAP['rsuper']
        self.assertTrue(keymap.is_specially_handled_vk_key(vk_code))

    def test_contains_specially_handled_vk_key(self) -> None:
        """Test contains_specially_handled_vk_key"""
        self.assertFalse(keymap.contains_specially_handled_vk_key([]))
        self.assertFalse(keymap.contains_specially_handled_vk_key(
            [keymap.STR_VK_MAP['a'], keymap.STR_VK_MAP['rshift']]
        ))
        self.assertTrue(keymap.contains_specially_handled_vk_key(
            [keymap.STR_VK_MAP['a'], keymap.STR_VK_MAP['rsuper']]
        ))
        self.assertTrue(keymap.contains_specially_handled_vk_key(
            [keymap.STR_VK_MAP['lsuper'], keymap.STR_VK_MAP['rsuper']]
        ))

    def test_get_modifier_vk_keys(self) -> None:
        """Test get_modifier_vk_keys"""
        with_special = keymap.get_modifier_vk_keys(True)
        without = keymap.get_modifier_vk_keys(False)
        self.assertNotEqual(without, with_special)
