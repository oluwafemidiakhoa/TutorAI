from ..mcp_instance import mcp
from ..model import gemini_flash

@mcp.tool("tutorx/content/generate_interactive_exercise")
def generate_interactive_exercise(topic: str) -> dict:
    """
    Create an engaging interactive exercise with multiple components.

    :param topic: The topic for the exercise.
    :return: A dictionary containing the exercise content.
    """
    prompt = f"Generate an interactive exercise on the topic of '{topic}'. The exercise should include a mix of questions, a small simulation or scenario, and a self-assessment component. Format as a JSON object."
    content = gemini_flash.generate_text(prompt)
    return {"topic": topic, "exercise": content}

@mcp.tool("tutorx/content/generate_adaptive_sequence")
def generate_adaptive_content_sequence(topic: str, student_level: str) -> dict:
    """
    Build an adaptive content sequence that adjusts to student performance.

    :param topic: The topic for the content sequence.
    :param student_level: The initial level of the student (e.g., beginner, intermediate).
    :return: The first piece of content in the adaptive sequence.
    """
    prompt = f"Create the first part of an adaptive content sequence on '{topic}' for a '{student_level}' student. Include a question to gauge understanding. Based on the answer, the next step would be easier or harder. Describe the branching logic. Format as a JSON object."
    content = gemini_flash.generate_text(prompt)
    return {"topic": topic, "student_level": student_level, "sequence_start": content}

@mcp.tool("tutorx/content/generate_scenario_learning")
def generate_scenario_based_learning(topic: str) -> dict:
    """
    Create a realistic scenario-based learning experience.

    :param topic: The topic for the scenario.
    :return: A dictionary containing the scenario.
    """
    prompt = f"Design a scenario-based learning experience for the topic '{topic}'. The scenario should present a real-world problem and guide the user through solving it. Include decision points. Format as a JSON object."
    content = gemini_flash.generate_text(prompt)
    return {"topic": topic, "scenario": content}

@mcp.tool("tutorx/content/generate_multimodal")
def generate_multimodal_content(topic: str, modalities: list) -> dict:
    """
    Generate content for different learning modalities (e.g., text, visual ideas, audio script).

    :param topic: The topic for the content.
    :param modalities: A list of modalities to generate content for.
    :return: A dictionary with content for each requested modality.
    """
    prompt = f"Generate educational content about '{topic}'. Provide content for the following modalities: {', '.join(modalities)}. For 'visual', describe an image or diagram. For 'audio', write a short script. Format as a JSON object."
    content = gemini_flash.generate_text(prompt)
    return {"topic": topic, "modalities": modalities, "content": content}

@mcp.tool("tutorx/content/generate_adaptive_assessment")
def generate_adaptive_assessment(topic: str) -> dict:
    """
    Create an assessment that adapts based on student responses.

    :param topic: The topic for the assessment.
    :return: The first question of the adaptive assessment.
    """
    prompt = f"Create the first question for an adaptive assessment on '{topic}'. The question should be multiple choice. For each answer, specify the difficulty of the next question (e.g., easier, harder, same). Format as a JSON object."
    content = gemini_flash.generate_text(prompt)
    return {"topic": topic, "assessment_start": content}

@mcp.tool("tutorx/content/generate_gamified")
def generate_gamified_content(topic: str) -> dict:
    """
    Generate game-based learning content with mechanics like points and badges.

    :param topic: The topic for the gamified content.
    :return: A description of the gamified activity.
    """
    prompt = f"Design a simple, gamified learning activity for the topic '{topic}'. Describe the rules, how a player would earn points, and what badges they could unlock. Format as a JSON object."
    content = gemini_flash.generate_text(prompt)
    return {"topic": topic, "game_description": content}

@mcp.tool("tutorx/content/validate")
def validate_generated_content(content: str, topic: str) -> dict:
    """
    Perform a quality-check and validation of educational content.

    :param content: The AI-generated content to validate.
    :param topic: The intended topic of the content.
    :return: A validation report.
    """
    prompt = f"Please validate the following educational content, which is supposed to be about '{topic}'. Check for factual accuracy, clarity, and age-appropriateness. Content: '{content}'. Provide a validation report with a 'status' (e.g., 'approved', 'needs_review') and 'comments'. Format as a JSON object."
    report = gemini_flash.generate_text(prompt)
    return {"content_to_validate": content, "validation_report": report}