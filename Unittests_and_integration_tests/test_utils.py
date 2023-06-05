#!/usr/bin/env python3
"""Test Suite for testing utils"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Class that unittests the `access_nested_map` function within utils.py"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Tests the access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests that a `KeyError` is raised"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """Class that unittests the `get_json` function within utils.py"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Tests whether `utils.get_json` returns the expected result"""
        mock_response = Mock()
        mock_response.json.return_value = payload
        with patch('requests.get', return_value=mock_response) as mock_get:
            response = get_json(url)
            mock_get.assert_called_once_with(url)
            self.assertEqual(response, payload)
