#!/usr/bin/env python3
"""Test Suite for testing client.py"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Tests whether GithubOrgClient.org returns the correct value"""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org')
    def test_public_repose_url(self, mock_org):
        """
        Unit-tests the _public_repos_url property of the GithubOrgClient class
        """
        test_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = test_payload

        test_client = GithubOrgClient("google")
        result = test_client._public_repos_url

        self.assertEqual(result, test_payload["repos_url"])

