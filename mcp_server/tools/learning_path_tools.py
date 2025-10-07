from ..mcp_instance import mcp
from ..resources import concept_graph

@mcp.tool("tutorx/learning_path/get")
def get_learning_path(student_id: str, target_concept: str) -> dict:
    """
    Generate a personalized learning path for a student to reach a target concept.

    :param student_id: The ID of the student.
    :param target_concept: The concept the student wants to learn.
    :return: A dictionary representing the personalized learning path.
    """
    # This is a simplified path generation based on dependencies.
    # A real system would be more sophisticated, considering the student's current knowledge.
    path = []

    def find_path(concept):
        if concept not in path:
            dependencies = concept_graph.get_dependencies(concept)
            for dep in dependencies:
                find_path(dep)
            path.append(concept)

    find_path(target_concept)

    return {
        "student_id": student_id,
        "target_concept": target_concept,
        "learning_path": path,
    }