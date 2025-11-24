import google.generativeai as genai
import os

class ContentAnalyzer:
    """
    A class to analyze content type using the Google Gemini Pro model.
    """
    def __init__(self):
        """
        Initializes the ContentAnalyzer and configures the API key.
        """
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Google API Key not found. Please set GOOGLE_API_KEY in your .env file.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name='gemini-2.5-flash')

    def analyze_content(self, text: str) -> str:
        """
        Analyzes the given text and classifies its content type.
        """
        if len(text.split()) < 50:
            return "Text too short for analysis."

        prompt = f"""
        Analyze the following text and determine its primary content type.
        Choose from these categories: "Academic Paper", "News Article", "Technical Documentation", "Blog Post", "General Text", "Creative Writing", "Other".
        Return only the category name.

        Text to analyze:
        ---
        {text}
        ---
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error analyzing content: {e}"
