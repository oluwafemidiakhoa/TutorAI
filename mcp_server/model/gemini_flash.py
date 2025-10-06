"""
Google Gemini Flash Model Integration

This module provides the integration with the Google Gemini Flash model,
which is used for various AI-powered tasks such as content generation
and contextualized tutoring.
"""
import os
import google.generativeai as genai
from typing import Union, List, Dict

class GeminiFlash:
    """
    A wrapper class for the Google Gemini Flash model.
    """
    def __init__(self):
        """
        Initializes the GeminiFlash model client.
        Requires the GOOGLE_API_KEY environment variable to be set.
        """
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_text(self, prompt: Union[str, List[Dict]]) -> str:
        """
        Generates text using the Gemini Flash model. Can accept a single
        string prompt or a conversation history.

        Args:
            prompt: The input prompt or conversation history.

        Returns:
            The generated text as a string.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating text with Gemini: {e}")
            return "Error: Could not generate a response."

    def start_chat(self, history: list = None):
        """
        Starts a chat session with the Gemini model.

        Args:
            history: An optional list of previous messages to start the chat with.

        Returns:
            A ChatSession object.
        """
        return self.model.start_chat(history=history or [])

# Example of how to use the class
if __name__ == '__main__':
    # This is for testing purposes.
    # Make sure to set your GOOGLE_API_KEY in your environment.
    gemini = GeminiFlash()
    test_prompt = "Explain the concept of photosynthesis in simple terms."
    generated_text = gemini.generate_text(test_prompt)
    print(f"Prompt: {test_prompt}")
    print(f"Generated Text: {generated_text}")