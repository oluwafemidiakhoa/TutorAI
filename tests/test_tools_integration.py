import pytest
from fastapi.testclient import TestClient
from mcp_server.server import app
from mcp_server.model import gemini_flash

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_gemini(monkeypatch):
    """
    Mock the gemini_flash.generate_text function to avoid actual API calls during tests.
    """
    def mock_generate_text(prompt: str):
        return f"Mocked response for prompt: {prompt}"
    monkeypatch.setattr(gemini_flash, "generate_text", mock_generate_text)


def test_get_concept_tool_endpoint():
    """
    Test the get_concept_tool endpoint to ensure it retrieves data correctly.
    """
    response = client.get("/tutorx/concept/get?concept_name=algebra")
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert "definition" in data
    assert data["definition"] == "A branch of mathematics that substitutes letters for numbers."

def test_get_learning_path_tool_endpoint():
    """
    Test the get_learning_path tool endpoint to ensure it generates a valid path.
    """
    response = client.get("/tutorx/learning_path/get?student_id=test_student&target_concept=calculus")
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert "learning_path" in data
    # The path should include dependencies in the correct order
    expected_path = ["arithmetic", "algebra", "geometry", "trigonometry", "calculus"]
    assert data["learning_path"] == expected_path

def test_generate_quiz_tool_endpoint():
    """
    Test the generate_quiz_tool endpoint.
    This is a basic test to ensure the endpoint is reachable.
    """
    response = client.post("/tutorx/quiz/generate?concept=algebra&difficulty=easy&num_questions=3")
    assert response.status_code == 200
    data = response.json()
    assert data["concept"] == "algebra"
    assert "quiz_content" in data
    assert "Mocked response" in data["quiz_content"]