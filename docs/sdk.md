# TutorX-MCP Client SDK Documentation

This document provides instructions and examples for using the TutorX-MCP Client SDK to interact with the TutorX platform.

## 1. Introduction

The TutorX-MCP Client SDK provides a simple and convenient way to communicate with the TutorX-MCP server from any Python application. It handles the details of the Model Context Protocol (MCP), allowing you to focus on building your application.

## 2. Installation

To use the SDK, you first need to install the `mcp-client` library:

```bash
pip install mcp-client
```

## 3. Getting Started

### 3.1. Initializing the Client

To begin, create an instance of the `Client` class, passing the URL of the TutorX-MCP server.

```python
from mcp_client import Client

# The default URL for a local server
server_url = "http://localhost:8000"
client = Client(server_url)
```

### 3.2. Calling a Tool

Once the client is initialized, you can call any of the available MCP tools on the server using the `call()` method. The first argument to `call()` is the name of the tool, followed by the tool's parameters as keyword arguments.

```python
# Example: Generate a quiz
try:
    quiz = client.call(
        "generate_quiz_tool",
        concept_name="photosynthesis",
        difficulty="easy",
        num_questions=5
    )
    print("Quiz generated successfully:")
    print(quiz)
except Exception as e:
    print(f"An error occurred: {e}")
```

### 3.3. Example: Starting a Tutoring Session

Here's a more complete example showing how to start a tutoring session and interact with the AI tutor:

```python
from mcp_client import Client

client = Client("http://localhost:8000")

# 1. Start a new session
session_info = client.call("start_tutoring_session", student_id="student123", topic="Biology")
session_id = session_info.get("session_id")

if session_id:
    print(f"Tutoring session started with ID: {session_id}")

    # 2. Send a message to the tutor
    response = client.call("ai_tutor_chat", session_id=session_id, message="What is a cell?")
    print(f"Tutor response: {response.get('response')}")

    # 3. End the session
    summary = client.call("end_tutoring_session", session_id=session_id)
    print(f"Session summary: {summary.get('summary')}")
else:
    print("Failed to start tutoring session.")
```

## 4. Error Handling

If a tool call fails, the SDK will raise an exception. It is important to wrap your tool calls in `try...except` blocks to handle potential errors, such as network issues or problems on the server side.