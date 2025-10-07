"""
Integration Tests for MCP Tools

This module contains integration tests that verify the functionality
of the various MCP tools.
"""
import unittest
import json
from unittest.mock import patch, MagicMock
from mcp_server.tools import concept_tools, quiz_tools, ai_tutor_tools
import uuid

# Patch the getter functions in each tool module
@patch('mcp_server.tools.quiz_tools.get_gemini_client')
@patch('mcp_server.tools.ai_tutor_tools.get_gemini_client')
class TestToolsIntegration(unittest.TestCase):
    """
    Test suite for MCP tool integration.
    """
    def test_get_concept_tool(self, mock_get_ai_tutor_gemini, mock_get_quiz_gemini):
        """
        Test the get_concept_tool to ensure it returns valid data.
        """
        result = concept_tools.get_concept_tool(concept_name="photosynthesis")
        self.assertIn("dependencies", result)
        self.assertIn("unlocks", result)

    def test_generate_quiz_tool_dynamic(self, mock_get_ai_tutor_gemini, mock_get_quiz_gemini):
        """
        Test the AI-powered generate_quiz_tool to ensure it returns a valid quiz structure.
        """
        # Configure the mock for the quiz tool
        mock_gemini_instance = MagicMock()
        quiz_json = {
            "concept": "mitochondria",
            "difficulty": "medium",
            "questions": [
                {"question_text": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria"], "correct_answer": "Mitochondria"},
                {"question_text": "What is ATP?", "options": ["Energy", "Waste"], "correct_answer": "Energy"}
            ]
        }
        mock_gemini_instance.generate_text.return_value = json.dumps(quiz_json)
        mock_get_quiz_gemini.return_value = mock_gemini_instance

        num_questions = 2
        result = quiz_tools.generate_quiz_tool(concept_name="mitochondria", num_questions=num_questions)

        self.assertNotIn("error", result, f"AI returned an error: {result.get('error')}")
        self.assertEqual(result.get("concept"), "mitochondria")
        self.assertEqual(len(result["questions"]), num_questions)
        self.assertEqual(result["questions"][0]["question_text"], "What is the powerhouse of the cell?")

    def test_ai_tutor_chat_session(self, mock_get_ai_tutor_gemini, mock_get_quiz_gemini):
        """
        Test the full flow of an AI tutor chat session.
        """
        # Configure the mock for the AI tutor tool
        mock_gemini_instance = MagicMock()
        mock_chat_session = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "This is a mock AI response."
        mock_chat_session.send_message.return_value = mock_response
        mock_gemini_instance.start_chat.return_value = mock_chat_session
        mock_get_ai_tutor_gemini.return_value = mock_gemini_instance

        student_id = str(uuid.uuid4())
        topic = "Python decorators"

        # 1. Start the session
        start_result = ai_tutor_tools.start_tutoring_session(student_id=student_id, topic=topic)
        self.assertNotIn("error", start_result)
        session_id = start_result["session_id"]

        # 2. Send a message and get a response
        chat_result = ai_tutor_tools.ai_tutor_chat(session_id=session_id, message="What is a decorator?")
        self.assertNotIn("error", chat_result)
        self.assertEqual(chat_result["response"], "This is a mock AI response.")

    def test_get_nonexistent_concept(self, mock_get_ai_tutor_gemini, mock_get_quiz_gemini):
        """
        Test that requesting a non-existent concept returns an error.
        """
        result = concept_tools.get_concept_tool(concept_name="nonexistent")
        self.assertIn("error", result)

if __name__ == '__main__':
    unittest.main()