markdown 
# Day 6: Streamlit Web Interface 
 
## Today's Goal 
Create beautiful, responsive Streamlit interface for the study agent. 
 
## Learning Focus - Streamlit components and layout - User experience design - Responsive web design - Interactive elements 
 
## UI Design Specifications 
 
### 1. Page Layout - **Sidebar**: File upload, settings, navigation - **Main Area**: Content display, summaries, quizzes - **Header**: App title, user guide - **Footer**: Status, credits 
 
### 2. Color Scheme 
```python 
COLOR_THEME = { 
    "primary": "#4B8BBE",    # Blue - learning 
    "secondary": "#306998",  # Dark blue 
    "accent": "#FFD43B",     # Yellow - highlight 
    "success": "#50C878",    # Green - correct 
    "danger": "#DC143C",     # Red - incorrect 
    "background": "#F0F2F6", # Light gray 
    "card": "#FFFFFF"        # White cards 
}