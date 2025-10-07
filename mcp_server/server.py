"""
TutorX-MCP FastAPI Server

This script initializes the FastAPI application that serves as the
core of the MCP server. It mounts the MCP instance and defines
the necessary API endpoints.
"""
from mcp_server.mcp_instance import mcp
from starlette.requests import Request
from starlette.responses import JSONResponse

# Use the MCP instance as the main FastAPI app
app = mcp

@app.custom_route("/", methods=["GET"])
async def root(request: Request):
    """
    Root endpoint for the server.
    Provides a welcome message and basic information.
    """
    return JSONResponse({
        "message": "Welcome to the TutorX-MCP Server!",
        "mcp_endpoint": "/mcp",
        "docs": "/docs",
    })

# Further endpoints, such as for SSE transport, can be added here.
# For example, an SSE endpoint might be set up as follows:
# from mcp.transport.sse import add_sse_transport
# add_sse_transport(app, mcp, "/sse")