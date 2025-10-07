"""
MCP Tools for AI Tutoring

This module provides tools for contextualized AI tutoring sessions,
including session management, interactive chat, and step-by-step guidance.
"""
from mcp_server.mcp_instance import mcp
from mcp_server.model.gemini_flash import GeminiFlash

_gemini_client = None

def get_gemini_client():
    """Initializes and returns a singleton Gemini client."""
    global _gemini_client
    if _gemini_client is None:
        try:
            _gemini_client = GeminiFlash()
        except ValueError as e:
            print(f"Error initializing Gemini: {e}")
    return _gemini_client

# In-memory store for tutoring sessions. In a real app, this would be
# replaced with a database or a more robust caching solution.
tutor_sessions = {}

@mcp.tool()
def start_tutoring_session(student_id: str, topic: str) -> dict:
    """
    Starts a new AI tutoring session for a student on a specific topic.

    :param student_id: The ID of the student.
    :param topic: The topic for the tutoring session.
    :return: A dictionary with the session details.
    """
    gemini = get_gemini_client()
    if not gemini:
        return {"error": "Gemini AI client not initialized. Check API keys."}

    session_id = f"session_{student_id}_{topic.replace(' ', '_')}"

    # Start a new chat session with the AI, including a system prompt
    initial_history = [
        {"role": "user", "parts": [f"Let's start a tutoring session about {topic}."]},
        {"role": "model", "parts": [f"Great! I'm ready to help you with {topic}. What's your first question?"]}
    ]
    chat_session = gemini.start_chat(history=initial_history)

    tutor_sessions[session_id] = {
        "student_id": student_id,
        "topic": topic,
        "chat_session": chat_session,
        "history": initial_history, # Keep our own history log
    }
    return {"session_id": session_id, "status": "started", "topic": topic}

@mcp.tool()
def ai_tutor_chat(session_id: str, message: str) -> dict:
    """
    Handles an interactive chat message within a tutoring session.

    :param session_id: The ID of the tutoring session.
    :param message: The student's message.
    :return: A dictionary with the tutor's response.
    """
    if session_id not in tutor_sessions:
        return {"error": "Session not found."}

    session = tutor_sessions[session_id]
    chat_session = session.get("chat_session")

    if not chat_session:
        return {"error": "Chat session not found for this session ID."}

    # Send the user's message to the Gemini chat session
    response = chat_session.send_message(message)
    response_text = response.text

    # Log the interaction in our history
    session["history"].append({"role": "user", "parts": [message]})
    session["history"].append({"role": "model", "parts": [response_text]})

    return {"session_id": session_id, "response": response_text}

@mcp.tool()
def get_step_by_step_guidance(session_id: str, concept: str) -> dict:
    """
    Provides step-by-step guidance on a complex concept.

    :param session_id: The ID of the tutoring session.
    :param concept: The concept to break down.
    :return: A dictionary with the step-by-step guidance.
    """
    if session_id not in tutor_sessions:
        return {"error": "Session not found."}

    return {
        "concept": concept,
        "steps": [
            f"Step 1: Understand the basics of {concept}.",
            f"Step 2: Explore the core components of {concept}.",
            f"Step 3: Apply {concept} to a real-world example.",
        ]
    }

@mcp.tool()
def end_tutoring_session(session_id: str) -> dict:
    """
    Ends a tutoring session and provides a summary.

    :param session_id: The ID of the tutoring session to end.
    :return: A summary of the session.
    """
    if session_id not in tutor_sessions:
        return {"error": "Session not found."}

    session = tutor_sessions.pop(session_id)
    return {
        "session_id": session_id,
        "status": "ended",
        "summary": f"Session on {session['topic']} is complete. Great work!",
    }