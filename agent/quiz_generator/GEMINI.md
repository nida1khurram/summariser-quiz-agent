# Quiz Generation Engine

## Overview
This document outlines the implementation of an intelligent quiz generation engine. The engine uses the Google Gemini Pro model to create quizzes from provided text, with support for multiple formats and difficulty levels.

## File: `agent/quiz_generator.py`

## Class: `QuizGenerator`

### Description
A class responsible for generating structured quizzes.

### Methods

- **`__init__(self)`**
  - Initializes the QuizGenerator and the Gemini model.

- **`generate_quiz(self, text: str, quiz_type: str, num_questions: int, difficulty: str) -> list[dict] | None:`**
  - **Description**: Generates a list of quiz questions based on the input parameters.
  - **Parameters**:
    - `text`: The source text for the quiz.
    - `quiz_type`: "MCQ", "True/False", or "Mixed".
    - `num_questions`: The number of questions to generate.
    - `difficulty`: "Easy", "Medium", or "Hard".
  - **Output Format**: The method should prompt the Gemini model to return a valid JSON object which is a list of dictionaries. Each dictionary represents a single question and must contain the following keys:
    - `question` (str): The question text.
    - `type` (str): The question type ("MCQ" or "True/False").
    - `options` (list[str]): A list of 4-5 choices for "MCQ" type, empty for "True/False".
    - `answer` (str): The correct answer. For "MCQ", this should be the text of the correct option.
    - `explanation` (str): A brief explanation of why the answer is correct.
  - **Returns**: A list of question dictionaries, or `None` if generation fails.

- **`_parse_json_output(self, text: str) -> list | None:`**
  - A private helper method to safely parse the JSON output from the Gemini model. It should handle cases where the model response is not perfect JSON.

## Interactive Features (in `main.py`)

The Streamlit UI should be updated to support an interactive quiz experience:
-   **Quiz State Management**: Use `st.session_state` to keep track of the current quiz data, the current question index, user answers, and the score.
-   **One-at-a-Time Display**: Show one question at a time with its options.
-   **User Input**: Use `st.radio` for capturing user answers.
-   **Feedback**: After a user submits an answer, show whether it was correct or incorrect and display the explanation.
-   **Navigation**: Use buttons to move to the next question or finish the quiz.
-   **Scoring**: Calculate and display the final score at the end.
