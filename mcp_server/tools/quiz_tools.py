"""
MCP Tools for Quiz Generation

This module provides MCP tools for creating LLM-generated quizzes for
specific concepts and difficulty levels.
"""
import json
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

@mcp.tool()
def generate_quiz_tool(concept_name: str, difficulty: str = "medium", num_questions: int = 5) -> dict:
    """
    Generates a quiz for a given educational concept using an AI model.

    :param concept_name: The concept the quiz should be about.
    :param difficulty: The difficulty level of the quiz (e.g., 'easy', 'medium', 'hard').
    :param num_questions: The number of questions to generate.
    :return: A dictionary representing the generated quiz.
    """
    gemini = get_gemini_client()
    if not gemini:
        return {"error": "Gemini AI client not initialized. Check API keys."}

    prompt = f"""
    Generate a quiz about '{concept_name}'.
    The quiz should have a difficulty level of '{difficulty}'.
    It must contain exactly {num_questions} questions.

    Please return the quiz as a single JSON object with the following structure:
    {{
      "concept": "{concept_name}",
      "difficulty": "{difficulty}",
      "questions": [
        {{
          "question_text": "...",
          "options": ["...", "...", "..."],
          "correct_answer": "..."
        }}
      ]
    }}
    Ensure the JSON is well-formed.
    """

    try:
        response_text = gemini.generate_text(prompt)
        # Clean the response to ensure it's valid JSON
        clean_response = response_text.strip().replace("```json", "").replace("```", "")
        quiz_data = json.loads(clean_response)
        return quiz_data
    except json.JSONDecodeError:
        return {"error": "Failed to parse the quiz from the AI's response."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}