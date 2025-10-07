"""
Shared MCP Instance for TutorX

This module creates a single, shared instance of the MCP (Model Context
Protocol) to be used across the application. This approach avoids
circular dependencies between the server and the tool modules.
"""
from mcp.server.fastmcp import FastMCP

# Create a shared MCP instance, which is a FastAPI app
mcp = FastMCP()

def register_tools():
    """
    Imports and registers all MCP tools with the shared MCP instance.
    This function is called at startup to ensure all tools are available.
    """
    # Import tool modules here to register them
    from mcp_server.tools import (
        concept_tools,
        quiz_tools,
        lesson_tools,
        ocr_tools,
        interaction_tools,
        learning_path_tools,
        ai_tutor_tools,
        content_generation_tools,
    )
    print("All tools registered.")