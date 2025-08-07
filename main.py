"""
Professional Portfolio Website
Built with Streamlit for AI/ML Software Engineer

Author: Julimore
Specialization: AI, Computer Vision, NLP, Software Engineering
"""

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import json
import requests
from streamlit_lottie import st_lottie

# Page configuration
st.set_page_config(
    page_title="Julius Mutugu - AI Software Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling with theme support
def load_css(theme="dark"):
    if theme == "dark":
        bg_gradient = "linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%)"
        card_bg = "rgba(30, 41, 59, 0.95)"
        text_color = "#ffffff"
        secondary_text = "#94a3b8"
        accent_color = "#3b82f6"
        nav_bg = "linear-gradient(180deg, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0.05) 100%)"
    else:
        bg_gradient = "linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #cbd5e1 100%)"
        card_bg = "rgba(255, 255, 255, 0.95)"
        text_color = "#1e293b"
        secondary_text = "#64748b"
        accent_color = "#3b82f6"
        nav_bg = "linear-gradient(180deg, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0.05) 100%)"
    
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {{
        background: {bg_gradient};
        min-height: 100vh;
        color: {text_color};
        transition: all 0.3s ease;
    }}
    
    .main .block-container {{
        background: {card_bg};
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 2.5rem;
        margin: 1rem;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.1);
        animation: fadeInUp 0.8s ease-out;
        color: {text_color};
    }}
    
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes slideIn {{
        from {{
            opacity: 0;
            transform: translateX(-20px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes pulse {{
        0%, 100% {{
            transform: scale(1);
        }}
        50% {{
            transform: scale(1.05);
        }}
    }}
    
    @keyframes glow {{
        0%, 100% {{
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
        }}
        50% {{
            box-shadow: 0 0 30px rgba(59, 130, 246, 0.6);
        }}
    }}
    
    .main-header {{
        font-family: 'Inter', sans-serif;
        font-size: 3.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 50%, #1e40af 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
        animation: slideIn 1s ease-out;
    }}
    
    .sub-header {{
        font-family: 'Inter', sans-serif;
        font-size: 1.3rem;
        color: {secondary_text};
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 400;
        animation: slideIn 1.2s ease-out;
    }}
    
    .project-card {{
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 70%, #1e40af 100%);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        color: white;
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInUp 0.6s ease-out;
    }}
    
    .project-card:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 25px 50px rgba(59, 130, 246, 0.5);
        animation: glow 2s infinite;
    }}
    
    .skill-badge {{
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        margin: 0.4rem;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 500;
        box-shadow: 0 6px 15px rgba(59, 130, 246, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        animation: slideIn 0.5s ease-out;
    }}
    
    .skill-badge:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.6);
    }}
    
    .contact-info {{
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(147, 197, 253, 0.1) 100%);
        padding: 2.5rem;
        border-radius: 20px;
        border-left: 4px solid;
        border-image: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) 1;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        color: {text_color};
        animation: fadeInUp 0.8s ease-out;
    }}
    
    .stats-container {{
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        padding: 2.5rem;
        border-radius: 20px;
        color: white;
        margin: 1.5rem 0;
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.4);
        animation: pulse 3s infinite;
    }}
    
    .navigation-header {{
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        font-weight: 600;
        color: {text_color};
        margin-bottom: 1.5rem;
        animation: slideIn 0.6s ease-out;
    }}
    
    .section-title {{
        font-family: 'Inter', sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 50%, #1e40af 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem;
        animation: slideIn 0.8s ease-out;
    }}
    
    .theme-toggle {{
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        padding: 0.8rem;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
        animation: fadeInUp 1s ease-out;
    }}
    
    .theme-toggle:hover {{
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5);
    }}
    
    .highlight-box {{
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(147, 197, 253, 0.1) 100%);
        border-left: 4px solid #3b82f6;
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        color: {text_color};
        animation: fadeInUp 0.6s ease-out;
        transition: all 0.3s ease;
    }}
    
    .highlight-box:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.2);
    }}
    
    .chart-container {{
        background: {card_bg};
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.1);
        animation: fadeInUp 0.8s ease-out;
    }}
    
    .animated-text {{
        animation: slideIn 1s ease-out;
    }}
    
    .stTabs [data-baseweb="tab-list"] button {{
        transition: all 0.3s ease;
        animation: slideIn 0.5s ease-out;
    }}
    
    .stTabs [data-baseweb="tab-list"] button:hover {{
        transform: translateY(-2px);
    }}
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        animation: glow 2s infinite;
    }}
    
    .stMetric {{
        animation: fadeInUp 0.6s ease-out;
        transition: all 0.3s ease;
    }}
    
    .stMetric:hover {{
        transform: translateY(-2px);
    }}
    
    .stSelectbox {{
        animation: slideIn 0.8s ease-out;
    }}
    
    .stButton > button {{
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        padding: 0.8rem 1.8rem;
        border-radius: 10px;
        font-weight: 500;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
        animation: fadeInUp 0.8s ease-out;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.5);
        animation: pulse 1s infinite;
    }}
    
    /* Sidebar styling */
    .sidebar .stSelectbox label {{
        color: {text_color};
        font-weight: 600;
    }}
    
    /* Form styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {{
        background: {card_bg};
        color: {text_color};
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px;
        animation: slideIn 0.6s ease-out;
    }}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {{
        width: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: rgba(255, 255, 255, 0.1);
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        border-radius: 4px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: linear-gradient(135deg, #1d4ed8 0%, #3b82f6 100%);
    }}
    </style>
    """, unsafe_allow_html=True)

def load_lottie_url(url: str):
    """Load Lottie animation from URL"""
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def main():
    # Initialize theme in session state
    if 'theme' not in st.session_state:
        st.session_state.theme = 'dark'
    
    # Initialize selected page
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = 'Home'
    
    # Theme toggle in sidebar
    with st.sidebar:
        st.markdown('<div class="navigation-header">Settings</div>', unsafe_allow_html=True)
        
        # Dark/Light theme toggle
        is_dark_theme = st.session_state.theme == 'dark'
        theme_toggle = st.toggle("🌙 Dark Mode", value=is_dark_theme, help="Toggle between dark and light themes")
        
        if theme_toggle != is_dark_theme:
            st.session_state.theme = 'dark' if theme_toggle else 'light'
            st.rerun()
        
        st.markdown("---")
    
    # Load CSS with current theme
    load_css(st.session_state.theme)
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown('<div class="navigation-header">Portfolio Navigation</div>', unsafe_allow_html=True)
        
        # Add a small profile section
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0; border-bottom: 1px solid rgba(59, 130, 246, 0.3); margin-bottom: 1rem;">
            <div style="width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); margin: 0 auto 0.5rem; display: flex; align-items: center; justify-content: center; font-size: 2rem; color: white; font-weight: bold;">J</div>
            <div style="font-size: 0.9rem; opacity: 0.8;">AI Software Engineer</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Get the current page index
        pages = ["Home", "Projects", "Skills", "Experience", "Contact"]
        current_index = pages.index(st.session_state.selected_page) if st.session_state.selected_page in pages else 0
        
        selected = option_menu(
            menu_title=None,
            options=pages,
            icons=["house-fill", "code-square", "cpu-fill", "briefcase-fill", "envelope-fill"],
            menu_icon="cast",
            default_index=current_index,
            key="main_menu",
            styles={
                "container": {
                    "padding": "0!important", 
                    "background": "linear-gradient(180deg, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0.05) 100%)",
                    "border-radius": "12px",
                    "border": "1px solid rgba(59, 130, 246, 0.2)"
                },
                "icon": {
                    "color": "#3b82f6", 
                    "font-size": "18px",
                    "margin-right": "8px"
                },
                "nav-link": {
                    "font-family": "Inter, sans-serif",
                    "font-size": "15px", 
                    "font-weight": "500",
                    "text-align": "left", 
                    "margin": "3px 8px",
                    "padding": "14px 18px",
                    "border-radius": "10px",
                    "color": "#ffffff" if st.session_state.theme == 'dark' else "#374151",
                    "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                    "border": "1px solid transparent"
                },
                "nav-link-selected": {
                    "background": "linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)",
                    "color": "white",
                    "font-weight": "600",
                    "box-shadow": "0 4px 12px rgba(59, 130, 246, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2)",
                    "border": "1px solid rgba(255, 255, 255, 0.3)",
                    "transform": "translateY(-1px)"
                },
                "nav-link-hover": {
                    "background": "rgba(59, 130, 246, 0.15)",
                    "color": "#3b82f6",
                    "transform": "translateY(-1px)",
                    "border": "1px solid rgba(59, 130, 246, 0.3)"
                }
            }
        )
        
        # Update session state when navigation changes
        if selected != st.session_state.selected_page:
            st.session_state.selected_page = selected
            st.rerun()
        
        # Add quick stats in sidebar
        st.markdown("---")
        st.markdown('<div class="navigation-header">Quick Stats</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="padding: 1rem; background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(147, 197, 253, 0.1) 100%); border-radius: 8px; margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="font-size: 0.8rem; opacity: 0.8;">Projects:</span>
                <span style="font-weight: 600; color: #3b82f6;">7+</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="font-size: 0.8rem; opacity: 0.8;">Skills:</span>
                <span style="font-weight: 600; color: #3b82f6;">25+</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="font-size: 0.8rem; opacity: 0.8;">Status:</span>
                <span style="font-weight: 600; color: #10b981;">Available</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main content based on navigation
    current_page = st.session_state.selected_page
    if current_page == "Home":
        show_home()
    elif current_page == "Projects":
        show_projects()
    elif current_page == "Skills":
        show_skills()
    elif current_page == "Experience":
        show_experience()
    elif current_page == "Contact":
        show_contact()

def show_home():
    """Home page with introduction and overview"""
    # Hero section with animations
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<h1 class="main-header">Julius Mutugu</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">AI & Software Engineer</p>', unsafe_allow_html=True)
        
        # Load animation
        lottie_coding = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
        if lottie_coding:
            st_lottie(lottie_coding, height=350, key="coding")
    
    st.markdown("---")
    
    # Introduction with animations
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="animated-text">', unsafe_allow_html=True)
        st.markdown("## Welcome to My Portfolio")
        st.markdown("""
        <div style="color: inherit; line-height: 1.7; font-size: 1.1rem;">
        I'm a <strong>Software Engineer</strong> with specialized expertise in <strong>Artificial Intelligence</strong>, recently graduated and prepared to contribute to innovative solutions at leading technology companies including <strong>Google</strong>, <strong>Microsoft</strong>, and <strong>Amazon</strong>.
        </div>
        
        <div style="margin-top: 2rem;">
        <h3 style="color: inherit; margin-bottom: 1rem;">Core Competencies</h3>
        <ul style="color: inherit; line-height: 1.8; font-size: 1rem;">
        <li><strong>Artificial Intelligence & Machine Learning</strong>: Developing intelligent systems that address complex real-world challenges</li>
        <li><strong>Computer Vision</strong>: Building applications capable of visual data interpretation and analysis</li>
        <li><strong>Natural Language Processing</strong>: Creating systems for human language understanding and generation</li>
        <li><strong>Full-Stack Development</strong>: Comprehensive application development using modern frameworks and architectures</li>
        </ul>
        </div>
        
        <div style="margin-top: 2rem;">
        <h3 style="color: inherit; margin-bottom: 1rem;">Professional Readiness</h3>
        <p style="color: inherit; line-height: 1.7; font-size: 1.1rem;">
        With a solid foundation in computer science theory and extensive practical development experience, I'm equipped to tackle sophisticated challenges in AI and software engineering at enterprise scale.
        </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stats-container">
            <h3 style="margin-top: 0; font-size: 1.4rem; font-weight: 600; text-align: center;">Professional Metrics</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Animated metrics
        st.metric("Projects Completed", "15+", "Recent: 3", help="Comprehensive projects across AI, ML, and web development")
        st.metric("AI Models Deployed", "8", "Production: 2", help="Machine learning models in real-world applications")
        st.metric("GitHub Contributions", "500+", "Active", help="Open source contributions and personal projects")
        
        st.markdown("""
        <div class="highlight-box">
            <h4 style="margin-top: 0; color: inherit; font-weight: 600;">Education</h4>
            <p style="margin-bottom: 0; color: inherit; line-height: 1.6;">
            <strong>Bachelor of Software Engineering</strong><br>
            <span style="color: #10b981; font-weight: 600;">University of Eastern Africa, Baraton (UEAB)</span><br>
            <em>Specialization: Artificial Intelligence & Machine Learning</em><br>
            <em>Graduated: 2025</em>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Add a call-to-action
        try:
            with open("assets/Julius_Mutugu_Resume.pdf", "rb") as pdf_file:
                pdf_data = pdf_file.read()
        
            st.download_button(
                label="📄 Download My Resume",
                data=pdf_data,
                file_name="Julius_Mutugu_AI_Engineer_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
                help="Download my complete resume in PDF format"
            )
        except FileNotFoundError:
            st.error("Resume file not found. Please contact me directly for the latest version.")
        
        if st.button("💼 Explore Projects", use_container_width=True):
            # Set session state to navigate to projects
            st.session_state.selected_page = "Projects"
            st.rerun()

def show_projects():
    """Projects showcase with filtering and interactive demos"""
    st.markdown('<h1 class="section-title">My Projects</h1>', unsafe_allow_html=True)
    st.markdown("Explore comprehensive solutions in AI, Computer Vision, NLP, and Software Development")
    
    # Project categories
    categories = ["All", "Computer Vision", "Natural Language Processing", "Machine Learning", "Web Development", "Mobile Development"]
    selected_category = st.selectbox("Filter by Category", categories)
    
    # Sample projects data (Julius Mutugu's actual projects)
    projects = [
        {
            "title": "Healthcare Insurance Implementation System (Kenya's SHIF Model)",
            "category": "Machine Learning",
            "description": "Comprehensive healthcare insurance system based on Kenya's Social Health Insurance Fund model with fraud detection and optimized fund allocation",
            "tech_stack": ["Python", "Blockchain", "Microservices", "Agile", "CI/CD"],
            "github": "Private Repository",
            "demo": True,
            "highlights": ["Integration with multiple insurance providers", "Advanced fraud detection algorithms", "Optimized fund allocation", "Microservices architecture"],
            "private": True
        },
        {
            "title": "Federated Machine Learning in Healthcare Systems",
            "category": "Machine Learning",
            "description": "Research and implementation of federated learning for healthcare systems to enhance data privacy while training models across decentralized datasets",
            "tech_stack": ["Python", "Federated Learning", "Privacy-Preserving ML", "Healthcare Data"],
            "github": "Private Repository",
            "demo": True,
            "highlights": ["Enhanced data privacy and security", "Decentralized model training", "Healthcare data protection", "Research-grade implementation"],
            "private": True
        },
        {
            "title": "Research and Grant Management System (UEAB)",
            "category": "Web Development",
            "description": "Full-stack university platform for managing research and grants with public researcher profiles, status tracking, and community forums",
            "tech_stack": ["Nuxt 3", "MongoDB Atlas", "Node.js", "Agile", "CI/CD"],
            "github": "https://github.com/JuliusMutugu",
            "demo": True,
            "highlights": ["Public researcher profiles", "Grant status tracking", "Community collaboration features", "Funding opportunity discovery"],
            "private": False
        },
        {
            "title": "Computer Vision for Waste Dataset Classification",
            "category": "Computer Vision",
            "description": "Intelligent waste classification system using Support Vector Machine with batch processing techniques for large-scale dataset optimization",
            "tech_stack": ["Python", "OpenCV", "SVM", "Computer Vision", "Data Processing"],
            "github": "https://github.com/JuliusMutugu/ImageClassification-dataset",
            "demo": True,
            "highlights": ["Accurate waste classification", "Batch processing optimization", "Large dataset handling", "Environmental impact"],
            "private": False
        },
        {
            "title": "Flet Desktop Application with Federated Learning",
            "category": "Mobile Development",
            "description": "Desktop application using Flet framework powered by custom federated learning algorithm built from scratch for competitive advantage",
            "tech_stack": ["Python", "Flet", "Federated Learning", "Desktop Development"],
            "github": "https://github.com/JuliusMutugu/FletSimpleApplicationDismissalMessage",
            "demo": True,
            "highlights": ["Custom federated learning implementation", "Cross-platform desktop app", "Innovative framework usage", "Machine learning integration"],
            "private": False
        },
        {
            "title": "House and Land Advertising System",
            "category": "Web Development",
            "description": "Django-based real estate platform with comprehensive property management, user authentication, and advanced search functionality",
            "tech_stack": ["Python", "Django", "PostgreSQL", "HTML/CSS", "JavaScript"],
            "github": "https://github.com/JuliusMutugu/houseAndLandAdverisingSystem",
            "demo": True,
            "highlights": ["Property management system", "User authentication", "Advanced search filters", "Responsive web design"],
            "private": False
        },
        {
            "title": "Data Analysis for E-commerce (UEAB Hackathon)",
            "category": "Machine Learning",
            "description": "Comprehensive data analysis project for e-commerce platform developed during university hackathon with advanced analytics and insights",
            "tech_stack": ["Python", "Jupyter Notebook", "Pandas", "Data Visualization", "Machine Learning"],
            "github": "https://github.com/JuliusMutugu/Data_analysis_ueab_hackathon_Ecommerce",
            "demo": True,
            "highlights": ["Hackathon winner project", "E-commerce analytics", "Data visualization", "Predictive insights"],
            "private": False
        }
    ]
    
    # Filter projects
    if selected_category != "All":
        filtered_projects = [p for p in projects if p["category"] == selected_category]
    else:
        filtered_projects = projects
    
    # Display projects with enhanced animations
    for i, project in enumerate(filtered_projects):
        with st.container():
            # Add staggered animation delay
            st.markdown(f"""
            <div class="project-card" style="animation-delay: {i * 0.2}s;">
                <h3 style="margin-top: 0; font-size: 1.6rem; font-weight: 600; color: white;">{project['title']}</h3>
                <p style="font-size: 0.95rem; opacity: 0.9; margin-bottom: 0.8rem; color: rgba(255,255,255,0.8);"><strong>Category:</strong> {project['category']}</p>
                <p style="font-size: 1.05rem; line-height: 1.6; margin-bottom: 0; color: white;">{project['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown('<div class="animated-text">', unsafe_allow_html=True)
                st.markdown("**Key Achievements:**")
                for j, highlight in enumerate(project['highlights']):
                    st.markdown(f'<div style="animation-delay: {(i * 0.2) + (j * 0.1)}s; animation: slideIn 0.6s ease-out both;">• {highlight}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="animated-text">', unsafe_allow_html=True)
                st.markdown("**Technology Stack:**")
                for j, tech in enumerate(project['tech_stack']):
                    st.markdown(f'<span class="skill-badge" style="animation-delay: {(i * 0.2) + (j * 0.1)}s;">{tech}</span>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col3:
                st.markdown('<div class="animated-text">', unsafe_allow_html=True)
                st.markdown("**Resources:**")
                
                # GitHub repository link with private indicator
                if project['private']:
                    st.markdown(f"🔒 **Private Repository** - Available upon request")
                    st.markdown("*Contact me for code review access*")
                else:
                    st.markdown(f"[🔗 GitHub Repository]({project['github']})")
                
                # Enhanced demo functionality
                if project['demo']:
                    if st.button("🚀 View Demo", key=f"demo_{i}"):
                        st.balloons()  # Add celebration animation
                        
                        # Different demo types based on project
                        if project['title'] == "Algorithmic Trading System":
                            st.success("🎉 Trading System Demo Ready!")
                            with st.expander("📊 Sample Trading Performance", expanded=True):
                                # Create a sample trading chart
                                import random
                                import datetime
                                dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
                                returns = [random.uniform(-0.02, 0.03) for _ in range(len(dates))]
                                cumulative_returns = (1 + pd.Series(returns)).cumprod()
                                
                                fig = go.Figure()
                                fig.add_trace(go.Scatter(x=dates, y=cumulative_returns, 
                                                       mode='lines', name='Portfolio Value',
                                                       line=dict(color='#84cc16', width=2)))
                                fig.update_layout(title="Sample Trading Performance (2024)",
                                                xaxis_title="Date", yaxis_title="Cumulative Returns",
                                                height=300, showlegend=False)
                                st.plotly_chart(fig, use_container_width=True)
                                
                        elif project['title'] == "Medical Insurance Mobile App":
                            st.success("🎉 Mobile App Demo Ready!")
                            with st.expander("📱 App Screenshots & Features", expanded=True):
                                col_demo1, col_demo2 = st.columns(2)
                                with col_demo1:
                                    st.markdown("**Key Features:**")
                                    st.markdown("• Policy Management Dashboard")
                                    st.markdown("• Claim Status Tracking")
                                    st.markdown("• Healthcare Provider Locator")
                                    st.markdown("• Secure Document Upload")
                                with col_demo2:
                                    st.markdown("**Technical Highlights:**")
                                    st.markdown("• React Native Cross-Platform")
                                    st.markdown("• Real-time Notifications")
                                    st.markdown("• Biometric Authentication")
                                    st.markdown("• HIPAA Compliant Security")
                        else:
                            st.success("🎉 Demo functionality ready for integration!")
                            with st.spinner('Loading demo...'):
                                import time
                                time.sleep(1)
                            st.info("Live demonstration available - contact for detailed walkthrough")
                        
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")

def show_skills():
    """Skills visualization and technical expertise"""
    st.markdown('<h1 class="section-title">Technical Skills</h1>', unsafe_allow_html=True)
    
    # Skills data
    skills_data = {
        "Programming Languages": {
            "Python": 95,
            "JavaScript": 85,
            "TypeScript": 80,
            "SQL": 85,
            "C++": 70,
            "R": 75
        },
        "AI/ML Frameworks": {
            "TensorFlow": 90,
            "PyTorch": 85,
            "Scikit-learn": 95,
            "OpenCV": 90,
            "NLTK/spaCy": 85
        },
        "Trading & Finance": {
            "Algorithmic Trading": 90,
            "Quantitative Analysis": 85,
            "Risk Management": 80,
            "Portfolio Optimization": 85,
            "Technical Analysis": 88,
            "Options Trading": 75
        },
        "Web Development": {
            "React": 85,
            "Vue.js": 80,
            "Next.js": 80,
            "FastAPI": 90,
            "Django": 85,
            "Flask": 90
        },
        "Mobile Development": {
            "React Native": 85,
            "Flutter": 80,
            "Android Development": 75,
            "iOS Development": 70,
            "Mobile UI/UX": 85
        },
        "Tools & Technologies": {
            "Docker": 85,
            "Git/GitHub": 95,
            "AWS": 75,
            "PostgreSQL": 85,
            "MongoDB": 80,
            "Redis": 75
        }
    }
    
    # Create tabs for different skill categories
    tabs = st.tabs(list(skills_data.keys()))
    
    for i, (category, skills) in enumerate(skills_data.items()):
        with tabs[i]:
            # Create a horizontal bar chart with professional styling
            colors = ['#667eea', '#764ba2', '#10b981', '#3b82f6', '#8b5cf6']
            
            fig = go.Figure(go.Bar(
                x=list(skills.values()),
                y=list(skills.keys()),
                orientation='h',
                marker=dict(
                    color=[colors[j % len(colors)] for j in range(len(skills))],
                    line=dict(color='rgba(255,255,255,0.8)', width=1)
                ),
                text=[f"{v}%" for v in skills.values()],
                textposition='inside',
                textfont=dict(color='white', size=12, family='Inter')
            ))
            
            fig.update_layout(
                title=dict(
                    text=f"{category} Proficiency",
                    font=dict(size=18, family='Inter', color='#374151'),
                    x=0.5
                ),
                xaxis=dict(
                    title="Proficiency Level (%)",
                    showgrid=True,
                    gridcolor='rgba(0,0,0,0.1)',
                    range=[0, 100]
                ),
                yaxis=dict(
                    title="Technologies",
                    showgrid=False
                ),
                height=400,
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', color='#374151')
            )
            
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Experience summary
    st.markdown("## Technical Expertise Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #065f46;">Artificial Intelligence & Machine Learning</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>Computer Vision</strong>: Image classification, object detection, facial recognition systems</li>
        <li><strong>Natural Language Processing</strong>: Sentiment analysis, text classification, language models</li>
        <li><strong>Machine Learning</strong>: Predictive modeling, recommendation systems, data analysis pipelines</li>
        <li><strong>Algorithmic Trading</strong>: Quantitative analysis, portfolio optimization, risk management</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #065f46;">Full-Stack & Mobile Development</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>Frontend Technologies</strong>: React, Vue.js, Next.js, responsive design principles</li>
        <li><strong>Backend Development</strong>: FastAPI, Django, Flask, RESTful API design</li>
        <li><strong>Mobile Development</strong>: React Native, Flutter, cross-platform applications</li>
        <li><strong>Database Management</strong>: PostgreSQL, MongoDB, data modeling and optimization</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #065f46;">DevOps & Financial Technology</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>Cloud Platforms</strong>: AWS, Azure, scalable deployment strategies</li>
        <li><strong>Containerization</strong>: Docker, microservices architecture</li>
        <li><strong>Version Control</strong>: Git, GitHub, collaborative development workflows</li>
        <li><strong>Trading Systems</strong>: Real-time data processing, automated execution</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

def show_experience():
    """Professional experience and education"""
    st.markdown('<h1 class="section-title">Experience & Education</h1>', unsafe_allow_html=True)
    
    # Education
    st.markdown("## Academic Background")
    st.markdown("""
    <div class="highlight-box">
    <h3 style="margin-top: 0; color: #065f46;">Bachelor of Software Engineering</h3>
    <p><strong>Specialization:</strong> Artificial Intelligence<br>
    <strong>Graduation:</strong> 2025<br>
    <strong>Focus:</strong> Advanced AI technologies and software engineering principles</p>
    
    <h4 style="color: #065f46;">Relevant Coursework:</h4>
    <ul style="margin-bottom: 0;">
    <li>Advanced Machine Learning & Deep Learning</li>
    <li>Computer Vision & Image Processing</li>
    <li>Natural Language Processing</li>
    <li>Software Engineering Principles</li>
    <li>Data Structures & Algorithms</li>
    <li>Database Systems & Design</li>
    <li>Web Development & API Design</li>
    <li>Distributed Systems Architecture</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Projects & Research
    st.markdown("## Project Development Timeline")
    
    project_timeline = {
        "2024-2025": [
            "AI-Powered Image Classification System",
            "Computer Vision Game Controller",
            "Sentiment Analysis API"
        ],
        "2023-2024": [
            "Predictive Maintenance ML Model",
            "Financial Analytics Dashboard",
            "E-commerce Recommendation System"
        ],
        "2022-2023": [
            "Social Media Analytics Tool",
            "Automated Testing Framework",
            "Mobile Application Development"
        ]
    }
    
    for year, projects in project_timeline.items():
        with st.expander(f"{year} - Key Development Projects"):
            for project in projects:
                st.markdown(f"• **{project}**")
    
    # Certifications & Skills
    st.markdown("## Professional Development")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #065f46;">Certifications</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>AWS Cloud Practitioner</strong> <em>(In Progress)</em></li>
        <li><strong>Google AI/ML Certification</strong> <em>(Planned)</em></li>
        <li><strong>Microsoft Azure Fundamentals</strong> <em>(Planned)</em></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #065f46;">Academic Achievements</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>Dean's List</strong> - Academic Excellence Recognition</li>
        <li><strong>Best Final Project</strong> - AI Specialization Program</li>
        <li><strong>Hackathon Winner</strong> - University Technology Competition</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

def show_contact():
    """Contact information and CV download"""
    st.markdown('<h1 class="section-title">Professional Contact</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## Contact Form")
        
        with st.form("contact_form"):
            name = st.text_input("Full Name *")
            email = st.text_input("Professional Email *")
            company = st.text_input("Company/Organization")
            subject = st.selectbox(
                "Inquiry Type *",
                ["Job Opportunity", "Technical Consultation", "Collaboration Proposal", "General Inquiry"]
            )
            message = st.text_area("Message *", height=150, placeholder="Please provide details about your inquiry...")
            
            submitted = st.form_submit_button("Send Message", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    st.success("Message sent successfully. I will respond within 24 hours.")
                    # Here you would integrate with an email service
                else:
                    st.error("Please complete all required fields.")
    
    with col2:
        st.markdown("## Resources & Links")
        
        # CV Download button
        st.markdown("### Resume/CV")
        
        try:
            with open("assets/Julius_Mutugu_Resume.pdf", "rb") as pdf_file:
                pdf_data = pdf_file.read()
            
            st.download_button(
                label="📄 Download CV (PDF)",
                data=pdf_data,
                file_name="Julius_Mutugu_AI_Engineer_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
                help="Download my complete resume with project details"
            )
        except FileNotFoundError:
            if st.button("📄 Download CV (PDF)", use_container_width=True):
                st.error("Resume file not found. Please contact me directly for the latest version.")
        
        st.markdown("*Updated: August 2025*")
        
        # Social links
        st.markdown("### Professional Networks")
        
        # GitHub link (updated with actual links)
        st.markdown("**GitHub:** [JuliusMutugu](https://github.com/JuliusMutugu)")
        st.markdown("**LinkedIn:** [Julius Mutugu](https://ke.linkedin.com/in/julius-mutugu-a3483b279)")
        st.markdown("**Email:** ndegwajulius239@gmail.com")
        st.markdown("**Location:** Nairobi, Kenya")
        
        # Contact info card
        st.markdown("""
        <div class="contact-info">
            <h4 style="margin-top: 0; color: #374151;">Target Opportunities</h4>
            <ul style="margin-bottom: 1rem;">
                <li><strong>Google</strong> - AI/ML Engineer</li>
                <li><strong>Microsoft</strong> - Software Engineer</li>
                <li><strong>Amazon</strong> - AI Specialist</li>
                <li><strong>Meta</strong> - ML Engineer</li>
                <li><strong>Apple</strong> - Software Engineer</li>
            </ul>
            
            <h4 style="color: #374151;">Availability</h4>
            <p style="margin-bottom: 1rem;">Open to remote work and relocation opportunities</p>
            
            <h4 style="color: #374151;">Status</h4>
            <p style="margin-bottom: 0;">Available for immediate employment</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
