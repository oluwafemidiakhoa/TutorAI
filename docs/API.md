# TutorX-MCP API Documentation

This document provides detailed documentation for the TutorX-MCP API, including all available endpoints and MCP tools.

## 1. RESTful API Endpoints

The server exposes the following RESTful endpoints:

- **`GET /`**: The root endpoint. Returns a welcome message and basic server information.
- **`GET /docs`**: Provides access to the auto-generated FastAPI documentation (Swagger UI).
- **`GET /redoc`**: Provides access to the auto-generated ReDoc documentation.

## 2. Model Context Protocol (MCP) Endpoint

The primary way to interact with the TutorX platform is through the MCP endpoint:

- **`/mcp`**: The main endpoint for all MCP tool calls.

### 2.1. Available Tools

Below is a list of the MCP tools available through the `/mcp` endpoint.

#### Concept Tools
- `get_concept_tool(concept_name: str)`
- `assess_skill_tool(student_id: str, concept_name: str)`

#### Quiz Tools
- `generate_quiz_tool(concept_name: str, difficulty: str, num_questions: int)`

#### Lesson Tools
- `generate_lesson_tool(concept_name: str, student_level: str)`

#### OCR Tools
- `mistral_document_ocr(document_url: str)`

#### Interaction Tools
- `text_interaction(student_id: str, query: str)`
- `check_submission_originality(submission_text: str)`

#### Learning Path Tools
- `get_learning_path(student_id: str, target_concept: str)`

#### AI Tutoring Tools
- `start_tutoring_session(student_id: str, topic: str)`
- `ai_tutor_chat(session_id: str, message: str)`
- `get_step_by_step_guidance(session_id: str, concept: str)`
- `end_tutoring_session(session_id: str)`

#### Content Generation Tools
- `generate_interactive_exercise(topic: str)`
- `generate_scenario_based_learning(topic: str)`
- `generate_gamified_content(topic: str)`
- `validate_generated_content(content: dict)`

For more details on each tool's parameters and return values, please refer to the tool's docstring in the source code.