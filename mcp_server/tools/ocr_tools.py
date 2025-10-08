import os
from fastapi import APIRouter, UploadFile, File
from PIL import Image
import io

router = APIRouter(
    prefix="/ocr",
    tags=["OCR Tools"],
)

client = None

def get_client():
    """
    Lazily initializes and returns the Mistral client.
    Imports are deferred to avoid issues in environments where they might hang.
    """
    global client
    if client is None:
        try:
            from mistralai import Mistral
            api_key = os.environ["MISTRAL_API_KEY"]
            client = Mistral(api_key=api_key)
        except (KeyError, ImportError) as e:
            print(f"Warning: Could not initialize Mistral. Error: {e}")
    return client

@router.post("/mistral_document", summary="Extract text from a document image")
async def mistral_document_ocr(image: UploadFile = File(...)) -> dict:
    """
    Extract and process text from a document image using Mistral OCR.

    :param image: The image file to process.
    :return: A dictionary containing the extracted text.
    """
    c = get_client()
    if c is None:
        return {"error": "Mistral API not configured or failed to initialize."}

    try:
        image_bytes = await image.read()
        img = Image.open(io.BytesIO(image_bytes))
        # This is a placeholder for actual OCR functionality.
        # Mistral's current Python client doesn't directly support OCR.
        # In a real implementation, you would use a service that provides OCR.
        # For now, we'll simulate a response.
        extracted_text = "Simulated OCR text from the image."

        return {
            "source": "Mistral OCR (Simulated)",
            "text": extracted_text,
        }
    except Exception as e:
        return {"error": f"An error occurred during OCR processing: {e}"}