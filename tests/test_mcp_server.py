from fastapi.testclient import TestClient
from mcp_server.server import app

client = TestClient(app)

def test_read_root():
    """
    Test the root endpoint of the MCP server.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "TutorX MCP Server is running"}

def test_mcp_endpoint_exists():
    """
    Test that the MCP endpoint is mounted and returns the MCP JSON-ADR.
    """
    response = client.get("/mcp")
    assert response.status_code == 200
    # Check for a key that should exist in the MCP JSON-ADR response
    assert "adr.mcp" in response.json()
    assert response.json()["adr.mcp"] == "1.0"