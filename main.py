import streamlit as st
from utils.pdf_processor.pdf_processor import PDFProcessor
from dotenv import load_dotenv
import os
from agent.summarizer.summarizer import SummarizerAgent
from agent.context7_client.context7_client import Context7Client
from agent.quiz_generator.quiz_generator import QuizGenerator
from agent.content_analyzer.content_analyzer import ContentAnalyzer
from agent.optimization.simulated_optimizer import SimulatedOptimizer # New import

# --- Configuration and Initialization ---
load_dotenv()

# Color Scheme from ui/GEMINI.md
COLOR_THEME = {
    "primary": "#4B8BBE",    # Blue - learning
    "secondary": "#306998",  # Dark blue
    "accent": "#FFD43B",     # Yellow - highlight
    "success": "#50C878",    # Green - correct
    "danger": "#DC143C",     # Red - incorrect
    "background": "#F0F2F6", # Light gray
    "card": "#FFFFFF"        # White cards
}

def apply_custom_css():
    st.markdown(
        f"""
        <style>
        .reportview-container .main .block-container {{
            background-color: {COLOR_THEME["background"]};
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }}
        .sidebar .sidebar-content {{
            background-color: {COLOR_THEME["secondary"]};
            color: {COLOR_THEME["card"]};
        }}
        .stButton>button {{
            background-color: {COLOR_THEME["primary"]};
            color: {COLOR_THEME["card"]};
            border-radius: 0.5rem;
            border: none;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
        }}
        .stButton>button:hover {{
            background-color: {COLOR_THEME["accent"]};
            color: {COLOR_THEME["secondary"]};
        }}
        .st-expander {{
            background-color: {COLOR_THEME["card"]};
            border-radius: 0.5rem;
            padding: 1rem;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            transition: 0.3s;
        }}
        .st-expander:hover {{
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        }}
        .st-success {{
            background-color: {COLOR_THEME["success"]} !important;
            color: white !important;
        }}
        .st-error {{
            background-color: {COLOR_THEME["danger"]} !important;
            color: white !important;
        }}
        .st-warning {{
            background-color: {COLOR_THEME["accent"]} !important;
            color: black !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    st.set_page_config(
        page_title="Study Notes Agent",
        page_icon="📚",
        layout="centered", # or "wide"
        initial_sidebar_state="expanded",
    )
    apply_custom_css()

    st.sidebar.title("📚 Study Agent")
    st.sidebar.header("Upload & Settings")

    # --- Sidebar: File Upload ---
    uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")
    
    # --- Sidebar: Navigation/Settings Placeholder ---
    st.sidebar.markdown("---")
    st.sidebar.subheader("Navigation")
    st.sidebar.info("Features below will appear in the main area once a PDF is processed.")
    # Add more navigation links here if needed
    st.sidebar.markdown("---")
    st.sidebar.subheader("Settings")
    if st.sidebar.button("Reset Session", help="Clear all processed data"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


    # --- Main Area: Header ---
    st.header("Welcome to Summarizer & Quiz Agent!")
    st.markdown("Upload your study notes (PDF) to get summaries, generate quizzes, and explore enhanced explanations.")

    # --- Initialization ---
    try:
        if "summarizer_agent" not in st.session_state:
            st.session_state.summarizer_agent = SummarizerAgent()
        summarizer_agent = st.session_state.summarizer_agent

        if "quiz_generator" not in st.session_state:
            st.session_state.quiz_generator = QuizGenerator()
        quiz_generator = st.session_state.quiz_generator

        if "c7_client" not in st.session_state:
            client = Context7Client(base_url="http://mock.mcp.server")
            client.connect()
            st.session_state.c7_client = client
        c7_client = st.session_state.c7_client

        if "content_analyzer" not in st.session_state: # New initialization
            st.session_state.content_analyzer = ContentAnalyzer()
        content_analyzer = st.session_state.content_analyzer
        
        if "simulated_optimizer" not in st.session_state: # New initialization
            st.session_state.simulated_optimizer = SimulatedOptimizer()
        simulated_optimizer = st.session_state.simulated_optimizer

    except ValueError as e:
        st.error(f"Initialization Failed: {e}")
        return

    pdf_processor = PDFProcessor()
    
    # --- Main Area: Content Sections ---
    if uploaded_file is not None:
        if "cleaned_text" not in st.session_state or st.session_state.get("file_id") != uploaded_file.file_id:
            st.session_state.file_id = uploaded_file.file_id
            with st.spinner("Processing PDF..."):
                raw_text = pdf_processor.extract_text(uploaded_file)
                st.session_state.cleaned_text = pdf_processor.clean_text(raw_text) if raw_text else None
                
                # New: Analyze content type
                if st.session_state.cleaned_text:
                    st.session_state.content_type = content_analyzer.analyze_content(st.session_state.cleaned_text)
                else:
                    st.session_state.content_type = "N/A"
                
                # Reset quiz and summary if a new PDF is uploaded
                if 'quiz_data' in st.session_state:
                    del st.session_state.quiz_data
                if 'summary_data' in st.session_state:
                    del st.session_state.summary_data

        if st.session_state.get("cleaned_text"):
            st.subheader("Extracted Text & Analysis")
            st.info(f"**Content Type:** {st.session_state.content_type}") # Display content type
            with st.expander("Click to view extracted text", expanded=False):
                st.text_area("Extracted Text", st.session_state.cleaned_text, height=250, disabled=True)

            # --- Summarization Section ---
            st.subheader("Generate Summary")
            if st.button("Generate Summary", key="generate_summary_btn"):
                with st.spinner("Generating summary..."):
                    summary_data = summarizer_agent.summarize(st.session_state.cleaned_text)
                    st.session_state.summary_data = summary_data
            
            if "summary_data" in st.session_state:
                with st.expander("Summary", expanded=True):
                    summary_data = st.session_state.summary_data
                    st.markdown(f"### {summary_data.get('title', 'Summary')}")
                    st.write(summary_data.get("summary", "No summary generated."))
                    keywords = summary_data.get("keywords", [])
                    if keywords:
                        st.write("**Keywords:**", ", ".join(keywords))
            
            st.markdown("---")

            # --- Quiz Generation Section ---
            st.subheader("Generate a Quiz")
            col1, col2, col3 = st.columns(3)
            with col1:
                quiz_type = st.selectbox("Quiz Type", ["MCQ", "True/False", "Mixed"], key="quiz_type_select")
            with col2:
                num_questions = st.number_input("Number of Questions", min_value=1, max_value=10, value=5, key="num_questions_input")
            with col3:
                difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"], key="difficulty_select")

            if st.button("Generate Quiz", key="generate_quiz_btn"):
                with st.spinner("Generating quiz..."):
                    quiz_data = quiz_generator.generate_quiz(st.session_state.cleaned_text, quiz_type, num_questions, difficulty)
                    if quiz_data:
                        st.session_state.quiz_data = quiz_data
                        st.session_state.current_question_index = 0
                        st.session_state.user_answers = {}
                        st.session_state.score = 0
                        st.session_state.feedback = ""
                        st.session_state.quiz_finished = False # Initialize quiz_finished flag
                    else:
                        st.error("Failed to generate quiz. Please try again or with a different text.")

        else:
            st.error("Could not extract text from the PDF. The file may be corrupted, empty, or unreadable.")
    else:
        st.info("Upload a PDF file from the sidebar to begin processing your study notes.")
                        
    # --- Interactive Quiz Display ---
    if "quiz_data" in st.session_state and st.session_state.quiz_data:
        st.markdown("---")
        st.header("Interactive Quiz")

        index = st.session_state.current_question_index
        quiz_data = st.session_state.quiz_data
        
        if index < len(quiz_data):
            question = quiz_data[index]
            st.markdown(f"#### Question {index + 1}/{len(quiz_data)}")
            st.markdown(f"**{question['question']}**")

            options = question.get('options', [])
            if question['type'] == 'True/False':
                options = ["True", "False"]
            
            # Use st.radio outside form for immediate interaction if preferred, or inside for form submission
            user_choice = st.radio("Select your answer:", options, key=f"radio_{index}")
            
            if st.button("Check Answer", key=f"check_answer_btn_{index}"):
                if user_choice == question['answer']:
                    st.session_state.score += 1
                    st.success("Correct! 🎉")
                else:
                    st.error(f"Incorrect. The correct answer was: {question['answer']} 😞")
                st.info(f"**Explanation:** {question['explanation']}")
            
            # Navigation buttons
            col_nav1, col_nav2 = st.columns(2)
            with col_nav1:
                if index > 0 and st.button("Previous Question", key=f"prev_q_btn_{index}"):
                    st.session_state.current_question_index -= 1
                    st.rerun()
            with col_nav2:
                if index < len(quiz_data) - 1:
                    if st.button("Next Question", key=f"next_q_btn_{index}"):
                        st.session_state.current_question_index += 1
                        st.rerun()
                else: # On the last question
                    if st.button("Finish Quiz", key=f"finish_quiz_btn_{index}"):
                        st.session_state.current_question_index += 1
                        st.session_state.quiz_finished = True
                        st.session_state.show_balloons = True # Set flag
                        st.rerun()
        
        else: # This block handles the case after all questions have been displayed
            if 'view_score_clicked' not in st.session_state:
                st.session_state.view_score_clicked = False
            
            if st.session_state.get('quiz_finished') and not st.session_state.view_score_clicked:
                st.markdown("---")
                st.info("You have completed the quiz!")

                # Check for and show balloons
                if st.session_state.get('show_balloons'):
                    st.balloons()
                    st.session_state.show_balloons = False # Unset flag

                if st.button("View Score", key="view_score_btn"):
                    st.session_state.view_score_clicked = True
                    st.rerun()
            else:
                st.success(f"Quiz Finished! Your final score is: {st.session_state.score}/{len(quiz_data)}")
                if st.button("Restart Quiz", key="restart_quiz_btn"):
                    # Clean up all session state variables related to the quiz
                    keys_to_delete = ['quiz_data', 'quiz_finished', 'view_score_clicked', 'current_question_index', 'user_answers', 'score', 'feedback']
                    for key in keys_to_delete:
                        if key in st.session_state:
                            del st.session_state[key]
                    st.rerun()
        
    # --- Context7 Enhanced Content Section ---
    st.markdown("---")
    with st.expander("Enhanced Educational Content (Context7 MCP)", expanded=False):
        if c7_client.connected:
            topic = st.text_input("Enter a topic for an enhanced explanation:", "Mitochondria", key="c7_topic_input")
            if st.button("Get Enhanced Explanation", key="c7_get_explanation_btn"):
                with st.spinner(f"Fetching enhanced explanation..."):
                    explanation = c7_client.get_enhanced_explanation(topic)
                    related_topics = c7_client.get_related_topics(topic)
                
                st.markdown(f"#### Enhanced Explanation for '{topic}'")
                st.write(explanation)
                if related_topics:
                    st.write("**Related Topics:**", ", ".join(related_topics))
        else:
            st.warning("Context7 MCP server is unavailable. Enhanced features are disabled.")
    
    # --- LLM Parameter Optimization (Simulation) Section ---
    st.markdown("---")
    with st.expander("LLM Parameter Optimization (Simulation)", expanded=False):
        st.subheader("Simulate finding optimal LLM parameters")
        st.markdown("Adjust the parameters below and run a simulation to see how they might affect an LLM's performance score.")

        temp = st.slider("Temperature (creativity)", min_value=0.0, max_value=1.0, value=0.7, step=0.05)
        top_p = st.slider("Top_P (diversity)", min_value=0.0, max_value=1.0, value=0.9, step=0.05)
        iters = st.slider("Iterations (stability)", min_value=1, max_value=5, value=3)

        if st.button("Run Optimization Simulation", key="run_optimization_btn"):
            with st.spinner("Running simulation..."):
                sim_results = simulated_optimizer.run_optimization_simulation(temp, top_p, iters)
            
            st.write("---")
            st.markdown(f"**Simulated Performance Score:** `{sim_results['simulated_score']}`")
            st.markdown(f"**Message:** `{sim_results['message']}`")
            st.markdown(f"**Initial Parameters:** `{sim_results['initial_parameters']}`")
            st.markdown(f"**Best Found Parameters (Simulated):** `{sim_results['best_found_parameters']}`")
            st.write("---")

    # --- Footer ---
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: gray;'>Study Notes Agent built with Streamlit & Google Gemini-cli</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; color: gray;'>Developed by Nida Khurram</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
