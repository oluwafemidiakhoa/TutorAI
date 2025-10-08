from fastapi import APIRouter
from ..model import gemini_flash

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz Tools"],
)

@router.post("/generate", summary="Generate a quiz for a specific concept")
def generate_quiz_tool(concept: str, difficulty: str = "medium", num_questions: int = 5) -> dict:
    """
    Create a quiz for a specific concept with customizable difficulty.

    :param concept: The educational concept for the quiz.
    :param difficulty: The difficulty level of the quiz (e.g., easy, medium, hard).
    :param num_questions: The number of questions to generate.
    :return: A dictionary representing the generated quiz.
    """
    prompt = f"Generate a {num_questions}-question quiz on the concept of '{concept}' with a difficulty level of '{difficulty}'. Include a mix of multiple-choice and short-answer questions. Format the output as a JSON object with a 'questions' array."

    # In a real application, you would parse the LLM response into a structured format.
    quiz_content = gemini_flash.generate_text(prompt)

    return {
        "concept": concept,
        "difficulty": difficulty,
        "num_questions": num_questions,
        "quiz_content": quiz_content,
    }