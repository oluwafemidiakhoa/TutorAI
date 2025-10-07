import pytest
from mcp_server.mcp_instance import mcp
from mcp_server.tools import concept_tools, learning_path_tools

def test_get_concept_tool():
    """
    Test the get_concept_tool to ensure it retrieves data from the concept graph.
    """
    # This is a direct call to the tool function, not through the MCP protocol.
    result = concept_tools.get_concept_tool("algebra")
    assert result is not None
    assert "definition" in result
    assert result["definition"] == "A branch of mathematics that substitutes letters for numbers."

def test_get_learning_path_tool():
    """
    Test the get_learning_path tool to ensure it generates a valid path.
    """
    result = learning_path_tools.get_learning_path("test_student", "calculus")
    assert result is not None
    assert "learning_path" in result
    # The path should include dependencies in the correct order
    expected_path = ["arithmetic", "algebra", "geometry", "trigonometry", "calculus"]
    assert result["learning_path"] == expected_path
