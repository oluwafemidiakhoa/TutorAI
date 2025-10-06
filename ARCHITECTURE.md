# TutorX-MCP Architecture

This document provides a detailed overview of the TutorX-MCP system architecture. It expands on the information provided in the `README.md` file.

## 1. System Overview

TutorX-MCP is designed with a modular, service-oriented architecture that separates concerns between the user interface, the core application logic, and the AI model integrations. This allows for scalability, maintainability, and flexibility.

## 2. Core Components

The system is composed of several key components:

- **Gradio Web Interface (`app.py`)**: The primary user-facing component, providing an interactive web-based UI for students and educators.
- **MCP Server (`main.py`, `mcp_server/`)**: The backend engine that exposes educational tools and resources via the Model Context Protocol (MCP).
- **AI Model Layer (`mcp_server/model/`)**: Integrates with external AI services like Google Gemini and Mistral for content generation, OCR, and tutoring.
- **Tool Modules (`mcp_server/tools/`)**: A collection of specialized modules that implement the core educational features of the platform.
- **Resource Modules (`mcp_server/resources/`)**: Manages educational data, such as the concept graph and curriculum standards.

## 3. Communication Flow

- The **Gradio UI** acts as an MCP client, communicating with the **MCP Server** to access the educational tools.
- The **MCP Server** orchestrates calls to the appropriate **Tool Modules**.
- **Tool Modules** interact with the **AI Model Layer** to generate responses and with the **Resource Modules** to retrieve educational data.

## 4. Data Management

- **Concept Graph**: A structured representation of educational concepts and their relationships.
- **Curriculum Standards**: Data on national educational standards to ensure content alignment.
- **Session Memory**: (Future) A Memory Bank to store context and state for personalized tutoring sessions.

## 5. Scalability and Deployment

The architecture is designed to be deployed in a containerized environment (e.g., Docker) and can be scaled horizontally by running multiple instances of the MCP server.