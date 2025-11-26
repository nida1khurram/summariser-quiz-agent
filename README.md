# Study Notes Summarizer & Quiz Generator Agent

A powerful AI agent by **Muhammad Adnan** that summarizes PDF study materials and generates interactive quizzes—perfect for students and learners! This tool leverages the Gemini API and is designed for easy use with a Streamlit web interface.

## 🚀 Core Features

-   **Intelligent Summarization**: Generates concise, detailed, or bullet-point summaries from your PDF notes.
-   **Interactive Quizzes**: Creates multiple-choice and true/false questions based on the document content.
-   **PDF Text Extraction**: Utilizes PyPDF2 to accurately extract and clean text from uploaded PDF files.
-   **Clean Web Interface**: A beautiful and responsive UI built with Streamlit, featuring a card-based layout and an educational color scheme.
-   **(Optional) Enhanced Capabilities**: Designed to integrate with Context7 MCP for deeper educational content analysis.
-   **Downloadable Content**: Allows you to download generated summaries and quizzes.

## 🛠️ Tech Stack

-   **Language**: Python 3.11+
-   **UI**: Streamlit
-   **PDF Processing**: PyPDF2
-   **AI**: Google Gemini
-   **Environment Management**: `uv`

## ⚙️ Setup & Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

Make sure you have Python 3.11+ and `uv` installed. If you don't have `uv`, you can install it via pip or PowerShell:

```bash
# Install via pip
pip install uv

# Or install via PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd study-notes-agent
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the virtual environment
    uv venv

    # Activate the environment
    # On Windows
    .venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    The project `requirements.txt` and `uv.lock` files should contain all dependencies. Use `uv sync` to install them.
    ```bash
    uv sync
    ```

## ▶️ How to Run

With your virtual environment activated and dependencies installed, run the Streamlit application:

```bash
streamlit run main.py
```

Now, open your web browser and navigate to **http://localhost:8501** to start using the agent!

## Usage

1.  **Upload a PDF**: Use the sidebar to upload your study notes in PDF format.
2.  **Generate Summary**: After the PDF is processed, click the "Generate Summary" button.
3.  **Create a Quiz**: Select your desired quiz type, number of questions, and difficulty, then click "Generate Quiz".
4.  **Interact**: Take the quiz directly in the app and get instant feedback.

---

*This project was inspired by a 7-day AI Agent learning journey.*