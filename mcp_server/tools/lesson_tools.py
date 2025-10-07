from ..mcp_instance import mcp
from ..model import gemini_flash

@mcp.tool("tutorx/lesson/generate")
def generate_lesson_tool(concept: str, learning_style: str = "visual") -> dict:
    """
    Create a complete lesson plan for a given concept, tailored to a specific learning style.

    :param concept: The educational concept for the lesson.
    :param learning_style: The preferred learning style (e.g., visual, auditory, kinesthetic).
    :return: A dictionary containing the generated lesson plan.
    """
    prompt = f"Generate a detailed lesson plan for the concept of '{concept}'. The lesson should be tailored for a '{learning_style}' learner. Include learning objectives, activities, and assessment methods. Format the output as a JSON object."

    lesson_content = gemini_flash.generate_text(prompt)

    return {
        "concept": concept,
        "learning_style": learning_style,
        "lesson_plan": lesson_content,
    }