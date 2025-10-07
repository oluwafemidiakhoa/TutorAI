"""
TutorX-MCP Server Entry Point

This script initializes and runs the MCP (Model Context Protocol) server,
making the educational tools and resources available to clients.
"""
from mcp_server.server import app
from mcp_server.mcp_instance import mcp, register_tools
import uvicorn

def main():
    """
    Main function to run the MCP server.
    """
    print("Initializing TutorX-MCP Server...")
    register_tools()
    print("All tools registered with MCP.")
    # The server is run via `run.py`, this file is for setup.
    print("MCP Server is ready. Use run.py to start.")

if __name__ == "__main__":
    # This allows running the server directly for debugging,
    # though `run.py` is the recommended way.
    main()
    uvicorn.run(app, host="0.0.0.0", port=8000)