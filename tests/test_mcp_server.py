"""
Tests for the MCP Server

This module contains tests for the main MCP server functionality,
such as server startup and endpoint availability.
"""
import unittest
from starlette.testclient import TestClient
from mcp_server.server import app

class TestMCPServer(unittest.TestCase):
    """
    Test suite for the MCP server.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up the test client once for the entire test class.
        """
        cls.client_cm = TestClient(app.streamable_http_app())
        cls.client = cls.client_cm.__enter__()

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the test client after all tests have run.
        """
        cls.client_cm.__exit__(None, None, None)

    def test_root_endpoint(self):
        """
        Test that the root endpoint is accessible and returns a
        successful response.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to the TutorX-MCP Server!", response.json()["message"])

    def test_mcp_endpoint_mounted(self):
        """
        Test that the MCP endpoint is mounted. This doesn't check for
        tool functionality, just that the endpoint exists.
        """
        # This is a basic check. A 404 would mean the endpoint is not mounted.
        # A more specific test would depend on the MCP library's behavior.
        response = self.client.get("/mcp")
        # Assuming the MCP library returns a specific status code when no tool is specified
        self.assertNotEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()