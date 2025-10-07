# TutorX-MCP Architecture

This document provides a detailed overview of the TutorX-MCP system architecture.

## Core Principles

The architecture is designed with the following principles in mind:

- **Modularity**: Components are self-contained and can be developed, tested, and deployed independently.
- **Scalability**: The system can handle a growing number of users and increasing complexity of interactions.
- **Extensibility**: New features, tools, and models can be easily integrated.
- **Maintainability**: A clear separation of concerns makes the codebase easier to understand and manage.

## System Components

The TutorX-MCP platform is composed of several key components:

### 1. MCP Server (`mcp_server/`)

The heart of the system, built with FastAPI. It exposes all educational functionalities as MCP tools and resources.

- **`server.py`**: The main FastAPI application that initializes the MCP instance and registers all the tools. It handles HTTP requests and manages the SSE transport layer for real-time communication with clients.
- **`mcp_instance.py`**: A singleton module that holds the shared MCP instance. This prevents circular dependencies and ensures all parts of the application can access the same set of tools.

### 2. Tool Modules (`mcp_server/tools/`)

Each file in this directory represents a set of related MCP tools. This modular approach allows for clean separation of functionalities.

- **`ai_tutor_tools.py`**: Manages interactive, contextualized tutoring sessions.
- **`content_generation_tools.py`**: Handles the creation of educational materials like quizzes, lessons, and exercises.
- **`concept_tools.py`**: Provides tools for accessing and assessing the educational concept graph.
- ...and other specialized tool modules.

### 3. AI Model Integration (`mcp_server/model/`)

This layer abstracts the interactions with external AI models, such as Google's Gemini and Mistral's OCR.

- **`gemini_flash.py`**: Contains the logic for communicating with the Gemini API, including a fallback mechanism for model availability. This ensures that the application remains resilient.

### 4. Educational Resources (`mcp_server/resources/`)

These modules manage the underlying data and knowledge bases that the educational tools rely on.

- **`concept_graph.py`**: Implements the knowledge graph of educational concepts and their relationships.
- **`curriculum_standards.py`**: Provides access to national curriculum standards to align content.

### 5. Gradio Web Interface (`app.py`)

The primary user interface for the platform, built with Gradio. It acts as an MCP client, communicating with the backend server to provide a rich, interactive experience for students and educators. It is designed to be a standalone component that can be run independently of the MCP server if needed.

### 6. Testing Suite (`tests/`)

A comprehensive set of tests to ensure the reliability and correctness of the application.

- **`test_mcp_server.py`**: Tests for the core MCP server functionality.
- **`test_tools_integration.py`**: Integration tests to ensure that all MCP tools work together as expected.
- **`test_client.py`**: Tests for the client-side interactions.

## Data Flow

1.  A client (either the Gradio UI or a standalone MCP client) sends a request to the MCP server.
2.  The FastAPI server receives the request and routes it to the appropriate MCP tool.
3.  The tool processes the request, potentially interacting with AI models (via the model integration layer) or educational data (via the resources layer).
4.  The result is sent back to the client through the MCP protocol, often over an SSE connection for real-time updates.

This layered and modular architecture ensures that TutorX-MCP is a robust, scalable, and maintainable platform for delivering personalized AI-powered tutoring.