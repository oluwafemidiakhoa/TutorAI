# In-memory representation of curriculum standards.
# In a real application, this would be a more complex system.

curriculum_standards = {
    "us": {
        "math": {
            "grade_9": ["algebra_1", "geometry"],
            "grade_10": ["algebra_2", "trigonometry"],
            "grade_11": ["pre_calculus"],
            "grade_12": ["calculus_ap"],
        }
    },
    "uk": {
        "math": {
            "gcse": ["algebra", "geometry", "statistics"],
            "a_level": ["calculus", "mechanics", "statistics"],
        }
    },
}

def get_standards(country_code: str, subject: str) -> dict:
    """
    Retrieves curriculum standards for a given country and subject.
    """
    return curriculum_standards.get(country_code, {}).get(subject, {})