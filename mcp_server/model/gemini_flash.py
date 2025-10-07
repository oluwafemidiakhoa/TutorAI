import os
import google.generativeai as genai

# Configure the Gemini API key
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except KeyError:
    print("Warning: GOOGLE_API_KEY environment variable not set.")
    model = None

def generate_text(prompt: str) -> str:
    """
    Generates text using the Google Gemini Flash model.

    Args:
        prompt: The prompt to send to the model.

    Returns:
        The generated text.
    """
    if model is None:
        return "Error: Gemini API not configured. Please set the GOOGLE_API_KEY."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred with the Gemini API: {e}"