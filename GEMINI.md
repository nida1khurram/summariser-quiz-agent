markdown 
# Study Notes Summarizer & Quiz Generator Agent 
 
## Project Overview 
AI-powered agent that summarizes PDF study materials and generates interactive quizzes 
using Context7 MCP and Gemini. 
 
## Core Features - PDF text extraction using PyPDF - Intelligent summarization using Gemini - Multiple quiz types (MCQs, True/False, Mixed) - Context7 MCP integration for enhanced capabilities - Streamlit web interface - Downloadable summaries and quizzes 
 
## Tech Stack - **Framework**: OpenAgents SDK - **UI**: Streamlit - **PDF Processing**: PyPDF2 - **AI**: Gemini CLI + Context7 MCP - **Language**: Python 3.11+ 
 
## Agent Architecture
Study Notes Agent 
├── PDF Upload & Processing 
├── Text Extraction (PyPDF) 
├── Summary Generation (Gemini) 
├── Quiz Generation (Context7 + Gemini) 
└── Streamlit UI 
text 
## Key Components 
1. **PDF Processor**: Extracts clean text from uploaded PDFs 
2. **Summarizer Agent**: Creates concise, meaningful summaries 
3. **Quiz Generator**: Creates various quiz formats from content 
4. **Context7 Integration**: Enhances AI capabilities 
5. **Streamlit UI**: Clean, user-friendly interface 
 
## UI Design Guidelines - Card-based layout for summaries - Clean, educational color scheme - Responsive design - Progress indicators for long operations - Download buttons for generated content

Step : Structure 
text 
Task-04/ 
├── main.py                 # Streamlit main application 
├── agent/ 
│   ├── __init__.py 
│   ├── summarizer.py      # PDF summarization logic 
│   ├── quiz_generator.py  # Quiz generation logic 
│   └── context7_client.py # Context7 MCP integration 
├── utils/ 
│   ├── __init__.py 
│   ├── pdf_processor.py   # PDF text extraction 
│   └── file_handler.py    # File operations 
├── data/                  # Uploaded PDFs storage 
├── requirements.txt 
└── README.md 