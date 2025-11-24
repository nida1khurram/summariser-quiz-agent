import google.generativeai as genai
import os
import json
import re

class SummarizerAgent:
    """
    An agent that uses Google Gemini Pro to generate structured summaries.
    """
    def __init__(self):
        """
        Initializes the SummarizerAgent and configures the API key.
        """
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Google API Key not found. Please set GOOGLE_API_KEY in your .env file.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name='gemini-2.5-flash')

    def _parse_json_output(self, text: str) -> dict | None:
        """
        Safely parses a JSON string from the model's output.
        """
        # The model might output markdown with a JSON block
        match = re.search(r"```json\n({.*?})\n```", text, re.DOTALL)
        if match:
            json_str = match.group(1)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                return None
        return None

    def summarize(self, text: str) -> dict:
        """
        Generates a structured summary for the given text.
        """
        if len(text.split()) < 50: # Quality control: check for minimum word count
            return {
                "title": "Text too short to summarize",
                "summary": "The provided text is too short for a meaningful summary. Please provide a longer text.",
                "keywords": []
            }
        
        prompt = f"""
        Analyze the following text and provide a structured summary in JSON format.
        The JSON object must contain these three keys:
        1. "title": A concise and informative title (string).
        2. "summary": A comprehensive summary of the key points (string).
        3. "keywords": A list of the 5 most important keywords (list of strings).

        Please enclose the JSON object in a markdown code block.

        Text to analyze:
        ---
        {text}
        ---
        """
        
        try:
            response = self.model.generate_content(prompt)
            parsed_output = self._parse_json_output(response.text)
            
            if parsed_output and all(k in parsed_output for k in ["title", "summary", "keywords"]):
                return parsed_output
            else:
                # Fallback to a simpler summary if JSON parsing fails
                return {
                    "title": "Summary",
                    "summary": response.text,
                    "keywords": []
                }
        except Exception as e:
            return {
                "title": "Error during summarization",
                "summary": f"An error occurred: {e}",
                "keywords": []
            }
