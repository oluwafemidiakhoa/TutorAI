# In-memory representation of a simple concept graph.
# In a real application, this would likely be loaded from a database or a file.

concept_graph = {
    "algebra": {
        "definition": "A branch of mathematics that substitutes letters for numbers.",
        "dependencies": ["arithmetic"],
        "unlocks": ["linear_algebra", "calculus"],
    },
    "calculus": {
        "definition": "The mathematical study of continuous change.",
        "dependencies": ["algebra", "trigonometry"],
        "unlocks": ["differential_equations"],
    },
    "trigonometry": {
        "definition": "A branch of mathematics that studies relationships between side lengths and angles of triangles.",
        "dependencies": ["geometry", "algebra"],
        "unlocks": ["calculus"],
    },
    "geometry": {
        "definition": "A branch of mathematics concerned with properties of space.",
        "dependencies": ["arithmetic"],
        "unlocks": ["trigonometry"],
    },
    "arithmetic": {
        "definition": "The branch of mathematics dealing with the properties and manipulation of numbers.",
        "dependencies": [],
        "unlocks": ["algebra", "geometry"],
    },
}

def get_concept(name: str) -> dict:
    """
    Retrieves a concept from the graph.
    """
    return concept_graph.get(name, {})

def get_dependencies(name: str) -> list:
    """
    Retrieves the dependencies for a concept.
    """
    return concept_graph.get(name, {}).get("dependencies", [])