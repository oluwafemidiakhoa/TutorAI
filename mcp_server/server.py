from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI(
    title="TutorX MCP Server",
    description="A comprehensive Model Context Protocol (MCP) server for educational AI tutoring.",
    version="0.1.0",
)

from .tools import (
    concept_tools,
    quiz_tools,
    lesson_tools,
    ocr_tools,
    interaction_tools,
    learning_path_tools,
    ai_tutor_tools,
    content_generation_tools,
)

app.include_router(concept_tools.router, prefix="/tutorx")
app.include_router(quiz_tools.router, prefix="/tutorx")
app.include_router(lesson_tools.router, prefix="/tutorx")
app.include_router(ocr_tools.router, prefix="/tutorx")
app.include_router(interaction_tools.router, prefix="/tutorx")
app.include_router(learning_path_tools.router, prefix="/tutorx")
app.include_router(ai_tutor_tools.router, prefix="/tutorx")
app.include_router(content_generation_tools.router, prefix="/tutorx")

@app.get("/", summary="Root endpoint for server status")
def read_root():
    """
    Check if the server is running.
    """
    return {"message": "TutorX MCP Server is running"}

# Create and mount the MCP server from the FastAPI app
mcp = FastApiMCP(app)
mcp.mount()