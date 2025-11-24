import google.generativeai as genai
import os
import json
import re

class QuizGenerator:
    """
    A class to generate structured quizzes using the Google Gemini Pro model.
    """
    def __init__(self):
        """
        Initializes the QuizGenerator and configures the API key.
        """
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Google API Key not found. Please set GOOGLE_API_KEY in your .env file.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name='gemini-2.5-flash')

    def _parse_json_output(self, text: str) -> list | None:
        """
        Safely parses a JSON string from the model's output.
        """
        # The model might output markdown with a JSON block. This regex finds it.
        match = re.search(r"```json\n(.*)\n```", text, re.DOTALL)
        if match:
            json_str = match.group(1)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                return None
        return None

    def generate_quiz(self, text: str, quiz_type: str, num_questions: int, difficulty: str) -> list[dict] | None:
        """
        Generates a list of quiz questions.
        """
        prompt = f"""
        Based on the following text, generate a quiz with {num_questions} questions.
        The quiz should be of difficulty: {difficulty}.
        The desired question type is: {quiz_type}.
        
        Please return the output as a JSON list of objects. Each object in the list represents a question and must have the following keys:
        - "question": The question text (string).
        - "type": The question type, e.g., "MCQ" or "True/False" (string).
        - "options": A list of 4-5 strings for "MCQ" type, or an empty list for "True/False".
        - "answer": The correct answer. For "MCQ", this is the full text of the correct option (string).
        - "explanation": A brief explanation of why the answer is correct (string).

        Enclose the entire JSON list in a single markdown code block.

        Source Text:
        ---
        {text}
        ---
        """
        
        try:
            response = self.model.generate_content(prompt)
            quiz_data = self._parse_json_output(response.text)
            return quiz_data
        except Exception:
            return None
