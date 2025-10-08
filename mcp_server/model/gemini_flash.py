import os

model = None

def get_model():
    """
    Lazily initializes and returns the Gemini model client.
    Imports are deferred to avoid issues in environments where they might hang.
    """
    global model
    if model is None:
        try:
            import google.generativeai as genai
            genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
            model = genai.GenerativeModel('gemini-1.5-flash')
        except (KeyError, ImportError) as e:
            print(f"Warning: Could not initialize Gemini. Error: {e}")
    return model

def generate_text(prompt: str) -> str:
    """
    Generates text using the Google Gemini Flash model.
    """
    m = get_model()
    if m is None:
        return "Error: Gemini API not configured or failed to initialize."
    try:
        response = m.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred with the Gemini API: {e}"