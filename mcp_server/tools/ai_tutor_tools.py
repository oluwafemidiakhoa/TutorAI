from fastapi import APIRouter
from ..model import gemini_flash

router = APIRouter(
    prefix="/ai_tutor",
    tags=["AI Tutor Tools"],
)

# In-memory store for tutoring sessions. In a real app, this would be a database.
sessions = {}

@router.post("/start_session", summary="Start a new AI tutoring session")
def start_tutoring_session(student_id: str) -> dict:
    """
    Start a new contextualized AI tutoring session with memory.

    :param student_id: The ID of the student starting the session.
    :return: A dictionary with the new session ID.
    """
    session_id = f"session_{student_id}_{len(sessions) + 1}"
    sessions[session_id] = {"student_id": student_id, "history": [], "understanding": {}}
    return {"session_id": session_id, "message": "Tutoring session started."}

@router.post("/chat", summary="Send a message to the AI tutor")
def ai_tutor_chat(session_id: str, message: str) -> dict:
    """
    Interactive chat with the AI tutor within a session.

    :param session_id: The ID of the current tutoring session.
    :param message: The student's message.
    :return: The AI tutor's response.
    """
    if session_id not in sessions:
        return {"error": "Session not found."}

    session = sessions[session_id]
    context = f"Session history: {session['history']}. Student understanding: {session['understanding']}. New message: {message}"
    prompt = f"You are an AI Tutor. Based on the following context, provide a helpful and adaptive response to the student's message.\n\nContext: {context}"

    response = gemini_flash.generate_text(prompt)
    session["history"].append({"user": message, "tutor": response})

    return {"response": response}

@router.get("/get_step_by_step", summary="Get step-by-step guidance for a concept")
def get_step_by_step_guidance(concept: str) -> dict:
    """
    Break down a complex concept into manageable steps.

    :param concept: The concept to break down.
    :return: A list of steps.
    """
    prompt = f"Provide a step-by-step guide to understanding the concept of '{concept}'. Format the output as a JSON object with a 'steps' array."
    guidance = gemini_flash.generate_text(prompt)
    return {"concept": concept, "guidance": guidance}

@router.get("/get_alternative_explanations", summary="Get an alternative explanation for a concept")
def get_alternative_explanations(concept: str, explanation_type: str = "analogy") -> dict:
    """
    Provide an alternative explanation for a concept (e.g., analogy, real-world example).

    :param concept: The concept to explain.
    :param explanation_type: The type of explanation to provide.
    :return: The alternative explanation.
    """
    prompt = f"Explain the concept of '{concept}' using a '{explanation_type}'. Be creative and clear."
    explanation = gemini_flash.generate_text(prompt)
    return {"concept": concept, "explanation_type": explanation_type, "explanation": explanation}

@router.post("/update_understanding", summary="Update a student's understanding level")
def update_student_understanding(session_id: str, concept: str, level: float) -> dict:
    """
    Track and adapt to a student's level of understanding.

    :param session_id: The ID of the current tutoring session.
    :param concept: The concept being tracked.
    :param level: The student's understanding level (e.g., 0.0 to 1.0).
    :return: A confirmation message.
    """
    if session_id not in sessions:
        return {"error": "Session not found."}

    sessions[session_id]["understanding"][concept] = level
    return {"message": f"Updated understanding of '{concept}' to {level}."}

@router.post("/end_session", summary="End a tutoring session")
def end_tutoring_session(session_id: str) -> dict:
    """
    End a tutoring session and provide a summary.

    :param session_id: The ID of the session to end.
    :return: A summary of the session.
    """
    if session_id not in sessions:
        return {"error": "Session not found."}

    session = sessions.pop(session_id)
    summary = f"Session summary for {session['student_id']}:\n- Topics covered: {list(session['understanding'].keys())}\n- Final understanding levels: {session['understanding']}"
    return {"summary": summary}