from ..mcp_instance import mcp
from ..model import gemini_flash

@mcp.tool("tutorx/interaction/text")
def text_interaction(student_query: str, session_context: dict = None) -> dict:
    """
    Process a student's text query and provide an educational response.

    :param student_query: The query from the student.
    :param session_context: The current context of the tutoring session.
    :return: A dictionary with the response and updated context.
    """
    prompt = f"A student asks: '{student_query}'. Based on the session context: {session_context}, provide a helpful and educational response."

    response_text = gemini_flash.generate_text(prompt)

    # Update context (this is a simplified example)
    if session_context is None:
        session_context = {}
    session_context['history'] = session_context.get('history', []) + [student_query]

    return {
        "response": response_text,
        "updated_context": session_context,
    }

@mcp.tool("tutorx/interaction/check_originality")
def check_submission_originality(submission_text: str) -> dict:
    """
    Analyze a student submission for potential plagiarism.

    :param submission_text: The text of the student's submission.
    :return: A dictionary with the originality analysis.
    """
    prompt = f"Analyze the following text for originality and potential plagiarism: '{submission_text}'. Provide a similarity score and highlight any potential issues."

    analysis = gemini_flash.generate_text(prompt)

    return {
        "submission": submission_text,
        "originality_analysis": analysis,
        # In a real system, this would be a structured score.
        "similarity_score": "low", # Placeholder
    }