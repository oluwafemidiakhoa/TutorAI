# Model Context Protocol (MCP) in TutorX

This document describes how the TutorX project utilizes the Model Context Protocol (MCP) for its backend services.

## 1. Overview

The Model Context Protocol (MCP) is the core communication layer for the TutorX platform. It provides a standardized way for the frontend (Gradio UI) and other potential clients to interact with the backend's educational tools.

## 2. MCP Server

The MCP server is implemented using FastAPI and the `mcp-server` library. It exposes a single endpoint, `/mcp`, which handles all tool calls.

## 3. Tool Registration

All educational tools are defined in the `mcp_server/tools/` directory. Each tool is decorated with `@mcp.tool()`, which automatically registers it with the shared MCP instance. This makes the tool discoverable and callable by any MCP client.

### Example Tool Registration:
```python
from mcp_server.mcp_instance import mcp

@mcp.tool()
def get_concept_tool(concept_name: str) -> dict:
    """
    Retrieves detailed information about an educational concept.
    """
    # ... implementation ...
```

## 4. Client Interaction

Clients, such as the Gradio web interface, use an MCP client library to connect to the server and call tools. The client sends a request to the `/mcp` endpoint specifying the tool name and its arguments. The server then executes the tool and returns the result.

### Example Client Call:
```python
from mcp_client import Client

# Connect to the server
client = Client(server_url="http://localhost:8000")

# Call a remote tool
result = client.call("get_concept_tool", concept_name="photosynthesis")

print(result)
```

## 5. SSE Transport

For real-time communication, the server will implement Server-Sent Events (SSE) transport. This will allow the server to push updates to the client, which is essential for features like live tutoring sessions and progress monitoring. The SSE endpoint will be available at `/sse`.