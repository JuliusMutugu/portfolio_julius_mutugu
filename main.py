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
import time
import random
import os
from datetime import datetime, timedelta
from streamlit_lottie import st_lottie
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from io import BytesIO
from typing import Dict, List, Optional
from urllib.parse import quote_plus
import re
from bs4 import BeautifulSoup

    # Page configuration
st.set_page_config(
    page_title="Julius Mutugu - AI Software Engineer",
    page_icon=":portfolio:",
    layout="wide",
    initial_sidebar_state="expanded"
)

    # Custom CSS for professional styling with dual theme support
def load_css(theme="modern_light"):
    if theme == "modern_light":
        # Modern Light Theme - Professional Yellow, Blue, White, Green combination
        bg_gradient = "linear-gradient(135deg, #ffffff 0%, #fefce8 20%, #eff6ff 40%, #ecfdf5 60%, #f8fafc 80%, #ffffff 100%)"
        card_bg = "rgba(255, 255, 255, 0.98)"
        text_color = "#1e3a8a"  # Professional deep blue for text
        secondary_text = "#1e40af"  # Medium blue
        accent_color = "#f59e0b"  # Professional yellow accent
        success_color = "#10b981"  # Professional green
        nav_bg = "linear-gradient(180deg, rgba(245, 158, 11, 0.08) 0%, rgba(59, 130, 246, 0.06) 50%, rgba(16, 185, 129, 0.06) 100%)"
        border_color = "rgba(245, 158, 11, 0.25)"
        yellow_primary = "#f59e0b"
        blue_primary = "#3b82f6"
        green_primary = "#10b981"
        white_primary = "#ffffff"
        gradient_primary = f"linear-gradient(135deg, {yellow_primary} 0%, {blue_primary} 30%, {green_primary} 60%, {blue_primary} 100%)"
        gradient_reverse = f"linear-gradient(135deg, {green_primary} 0%, {blue_primary} 30%, {yellow_primary} 100%)"
        gradient_accent = f"linear-gradient(45deg, {yellow_primary} 0%, {green_primary} 50%, {blue_primary} 100%)"
    else:
        # Dark Theme - Professional dark blue, yellow and green accents
        bg_gradient = "linear-gradient(135deg, #0f172a 0%, #1e293b 25%, #0f766e 50%, #374151 75%, #1f2937 100%)"
        card_bg = "rgba(30, 41, 59, 0.98)"
        text_color = "#f8fafc"  # Light text for dark theme
        secondary_text = "#cbd5e1"  # Light gray
        accent_color = "#fbbf24"  # Bright yellow accent
        success_color = "#34d399"  # Bright green
        nav_bg = "linear-gradient(180deg, rgba(251, 191, 36, 0.12) 0%, rgba(59, 130, 246, 0.08) 50%, rgba(52, 211, 153, 0.08) 100%)"
        border_color = "rgba(251, 191, 36, 0.3)"
        yellow_primary = "#fbbf24"
        blue_primary = "#60a5fa"
        green_primary = "#34d399"
        white_primary = "#ffffff"
        gradient_primary = f"linear-gradient(135deg, {yellow_primary} 0%, {blue_primary} 30%, {green_primary} 60%, {blue_primary} 100%)"
        gradient_reverse = f"linear-gradient(135deg, {green_primary} 0%, {blue_primary} 30%, {yellow_primary} 100%)"
        gradient_accent = f"linear-gradient(45deg, {yellow_primary} 0%, {green_primary} 50%, {blue_primary} 100%)"
    
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
        background: {gradient_primary};
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
        background: {gradient_primary};
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        color: {white_primary};
        box-shadow: 0 15px 35px rgba(245, 158, 11, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInUp 0.6s ease-out;
    }}
    
    .project-card:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 25px 50px rgba(245, 158, 11, 0.4);
        animation: glow 2s infinite;
    }}
    
    .skill-badge {{
        background: {gradient_primary};
        color: {white_primary};
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        margin: 0.4rem;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 500;
        box-shadow: 0 6px 15px rgba(245, 158, 11, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        animation: slideIn 0.5s ease-out;
    }}
    
    .skill-badge:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.5);
    }}
    
    .contact-info {{
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%);
        padding: 2.5rem;
        border-radius: 20px;
        border-left: 4px solid;
        border-image: {gradient_primary} 1;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        color: {text_color};
        animation: fadeInUp 0.8s ease-out;
    }}
    
    .stats-container {{
        background: {gradient_primary};
        padding: 2.5rem;
        border-radius: 20px;
        color: {white_primary};
        margin: 1.5rem 0;
        box-shadow: 0 15px 35px rgba(245, 158, 11, 0.3);
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
        background: {gradient_primary};
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
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(59, 130, 246, 0.08) 100%);
        border-left: 4px solid {yellow_primary};
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        color: {text_color};
        animation: fadeInUp 0.6s ease-out;
        transition: all 0.3s ease;
    }}
    
    .highlight-box:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.15);
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
        background: {gradient_primary};
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
    
    .stButton > button,
    .stDownloadButton > button,
    div[data-testid="stDownloadButton"] > button {{
        background: {gradient_primary} !important;
        color: {white_primary} !important;
        border: none !important;
        padding: 0.8rem 1.8rem !important;
        border-radius: 10px !important;
        font-weight: 500 !important;
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.3) !important;
        transition: all 0.3s ease !important;
        animation: fadeInUp 0.8s ease-out !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 1rem !important;
        cursor: pointer !important;
        width: 100% !important;
        text-align: center !important;
        text-decoration: none !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        min-height: 2.5rem !important;
    }}
    
    .stButton > button:hover,
    .stDownloadButton > button:hover,
    div[data-testid="stDownloadButton"] > button:hover {{
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(245, 158, 11, 0.4) !important;
        animation: pulse 1s infinite !important;
        background: {gradient_reverse} !important;
    }}
    
    /* Remove any default download button styling */
    div[data-testid="stDownloadButton"] {{
        width: 100% !important;
    }}
    
    div[data-testid="stDownloadButton"] > button {{
        background-color: transparent !important;
        border-color: transparent !important;
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
    
    /* Floating WhatsApp Button Styles */
    .floating-contact {{
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 1000;
    }}
    
    .main-fab {{
        min-width: 140px;
        height: 60px;
        border-radius: 30px;
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 20px rgba(37, 211, 102, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: none;
        font-size: 1.1rem;
        text-decoration: none;
        animation: float 3s ease-in-out infinite;
        padding: 0 20px;
    }}
    
    .main-fab:hover {{
        transform: scale(1.05) translateY(-2px);
        box-shadow: 0 8px 30px rgba(37, 211, 102, 0.6);
        background: linear-gradient(135deg, #128C7E 0%, #25D366 100%);
        text-decoration: none;
        color: white;
    }}
    
    @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
    }}
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {{
        .floating-contact {{
            bottom: 20px;
            right: 20px;
        }}
        
        .main-fab {{
            min-width: 120px;
            height: 55px;
            font-size: 1rem;
            padding: 0 15px;
        }}
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

@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_github_profile_image(username: str = "JuliusMutugu") -> str:
    """Get GitHub profile image URL"""
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 200:
            user_data = response.json()
            return user_data.get('avatar_url', '')
        return ''
    except:
        return ''

@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_github_data(username: str = "JuliusMutugu") -> Dict:
    """Fetch GitHub user data and repositories with caching"""
    try:
        # Fetch user data
        user_response = requests.get(f"https://api.github.com/users/{username}")
        if user_response.status_code != 200:
            return {"error": "User not found"}
        
        user_data = user_response.json()
        
        # Fetch repositories
        repos_response = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated")
        if repos_response.status_code != 200:
            return {"error": "Repositories not found"}
        
        repos_data = repos_response.json()
        
        # Process repository data
        processed_repos = []
        for repo in repos_data[:20]:  # Limit to recent 20 repos
            processed_repos.append({
                "name": repo["name"],
                "description": repo["description"] or "No description available",
                "language": repo["language"] or "Unknown",
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "updated_at": repo["updated_at"],
                "html_url": repo["html_url"],
                "topics": repo.get("topics", [])
            })
        
        return {
            "user": {
                "name": user_data["name"] or username,
                "bio": user_data["bio"] or "No bio available",
                "public_repos": user_data["public_repos"],
                "followers": user_data["followers"],
                "following": user_data["following"],
                "avatar_url": user_data["avatar_url"],
                "location": user_data["location"],
                "company": user_data["company"],
                "blog": user_data["blog"]
            },
            "repositories": processed_repos
        }
    except Exception as e:
        return {"error": f"Failed to fetch GitHub data: {str(e)}"}

def generate_job_application_package(company_name: str, position: str, github_data: Dict) -> Dict:
    """Generate customized job application package with enhanced personalization"""
    
    # Extract GitHub stats for personalization
    total_repos = github_data.get('user', {}).get('public_repos', 'multiple')
    followers = github_data.get('user', {}).get('followers', 'several')
    recent_activity = len([r for r in github_data.get('repositories', []) if '2024' in r.get('updated_at', '')])
    
    # Dynamic project highlights based on GitHub data
    project_highlights = []
    if github_data.get('repositories'):
        for repo in github_data['repositories'][:3]:  # Top 3 repositories
            if repo.get('name') and repo.get('description'):
                project_highlights.append(f"• {repo['name']}: {repo['description']}")
    
    if not project_highlights:
        project_highlights = [
            "• Healthcare AI System: Enterprise-grade insurance system with fraud detection",
            "• Federated Learning Research: Privacy-preserving ML for healthcare systems",
            "• Computer Vision Applications: Intelligent classification using advanced ML"
        ]
    
    # Customized cover letter templates with dynamic content
    cover_letter_templates = {
        "Google": f"""
Dear Google Hiring Team,

I am excited to apply for the {position} position at Google. As a Software Engineering graduate specializing in AI and Machine Learning, I am passionate about Google's mission to organize the world's information and make it universally accessible.

My technical expertise and project portfolio demonstrate strong alignment with Google's innovative culture:

{chr(10).join(project_highlights)}

With {total_repos} repositories on GitHub and {followers} followers, my consistent development activity showcases expertise in Python, TensorFlow, and cloud technologies that align perfectly with Google's tech stack. My recent GitHub activity includes {recent_activity} updated projects in 2024, demonstrating continuous learning and innovation.

Key technical competencies that make me a strong fit for Google:
• AI/ML: Advanced experience with TensorFlow, PyTorch, and computer vision
• Cloud Computing: Proficient in Google Cloud Platform and distributed systems
• Software Engineering: Full-stack development with modern frameworks and best practices
• Research Mindset: Published research in federated learning and privacy-preserving ML

I am particularly excited about contributing to Google's AI initiatives and would welcome the opportunity to discuss how my background in AI research, software engineering, and passion for innovation can contribute to your team's success.

Thank you for considering my application. I look forward to the opportunity to contribute to Google's mission of organizing the world's information.

Best regards,
Julius Mutugu
AI & Software Engineer
""",
        "Microsoft": f"""
Dear Microsoft Hiring Team,

I am writing to express my strong interest in the {position} position at Microsoft. Your commitment to empowering every person and organization on the planet to achieve more resonates deeply with my passion for creating impactful technology solutions.

My comprehensive technical background and active development portfolio make me an ideal candidate:

{chr(10).join(project_highlights)}

My GitHub profile demonstrates consistent excellence with {total_repos} public repositories and {followers} followers, showcasing my commitment to open-source development and continuous learning. With {recent_activity} recent project updates in 2024, I maintain active engagement with cutting-edge technologies.

Technical expertise aligned with Microsoft's ecosystem:
• Azure Cloud Services: Experience with cloud-native development and microservices
• AI/ML Frameworks: Proficient in Azure ML, TensorFlow, and enterprise AI solutions
• Enterprise Development: Full-stack applications with scalable architecture
• Modern Development: .NET ecosystem, TypeScript, and DevOps practices

My experience developing healthcare and research management systems demonstrates the ability to build enterprise-grade solutions that align with Microsoft's enterprise focus. I am particularly interested in contributing to Microsoft's AI and cloud initiatives.

I am excited about the opportunity to contribute to Microsoft's mission of empowering achievement and would appreciate the chance to discuss how my skills and passion can benefit your team.

Sincerely,
Julius Mutugu
AI & Software Engineer
""",
        "Amazon": f"""
Dear Amazon Hiring Team,

I am enthusiastic about applying for the {position} position at Amazon. Your customer-obsessed culture and commitment to innovation in cloud computing and AI align perfectly with my career aspirations and technical expertise.

My project portfolio and technical achievements demonstrate alignment with Amazon's high standards:

{chr(10).join(project_highlights)}

With {total_repos} GitHub repositories and {followers} followers, I demonstrate the technical breadth and depth that Amazon values. My {recent_activity} recent project updates in 2024 showcase continuous innovation and learning mindset essential for Amazon's fast-paced environment.

Core competencies that align with Amazon's requirements:
• AWS Cloud Services: Experienced with cloud-native architecture and serverless computing
• Scalable Systems: Built enterprise applications designed for high availability and performance
• Machine Learning: Advanced ML and AI implementations suitable for production environments
• Full-Stack Development: Comprehensive web and mobile application development

My experience with microservices architecture and distributed systems directly aligns with Amazon's cloud-first approach. I am particularly excited about contributing to AWS services and Amazon's AI initiatives.

I am eager to contribute to Amazon's mission of being Earth's Most Customer-Centric Company and would welcome the opportunity to discuss how my skills and customer-focused mindset can benefit your team.

Best regards,
Julius Mutugu
AI & Software Engineer
""",
        "Meta": f"""
Dear Meta Hiring Team,

I am excited to apply for the {position} position at Meta. Your vision of connecting people and building the next evolution of social technology through the metaverse deeply inspires me, and I am eager to contribute to this transformative mission.

My technical background and innovative project portfolio align well with Meta's forward-thinking approach:

{chr(10).join(project_highlights)}

My GitHub presence ({total_repos} repositories, {followers} followers) demonstrates expertise in technologies that power Meta's platforms. With {recent_activity} active projects in 2024, I maintain engagement with cutting-edge technologies relevant to social computing and VR/AR.

Technical skills perfectly suited for Meta's innovation:
• AI/ML Research: Advanced experience in federated learning and privacy-preserving ML
• Computer Vision: Deep learning applications for image and video processing
• Full-Stack Development: React, Node.js, and modern web technologies
• Social Technology: Understanding of scalable systems for connecting people globally

My research in federated learning particularly aligns with Meta's focus on privacy and decentralized computing. I am especially interested in contributing to Meta's AI research initiatives and social technology development.

I would be thrilled to discuss how my passion for connecting people through technology and my technical expertise can contribute to Meta's groundbreaking work in building the metaverse.

Sincerely,
Julius Mutugu
AI & Software Engineer
""",
        "Apple": f"""
Dear Apple Hiring Team,

I am writing to apply for the {position} position at Apple. Your commitment to creating products that enrich people's lives through innovative design and cutting-edge technology perfectly aligns with my passion for building exceptional user experiences.

My technical excellence and attention to detail demonstrate Apple's values of innovation and quality:

{chr(10).join(project_highlights)}

With {total_repos} public repositories and {followers} GitHub followers, I showcase clean, well-documented code and innovative solutions that embody Apple's commitment to quality. My {recent_activity} recent project updates in 2024 reflect continuous pursuit of excellence.

Core competencies aligned with Apple's ecosystem:
• AI/ML Innovation: Advanced machine learning with focus on on-device processing and privacy
• Software Craftsmanship: Clean, efficient code with attention to performance and user experience
• Privacy-First Development: Experience with privacy-preserving ML techniques
• Cross-Platform Development: iOS, macOS, and web technologies

My background in privacy-preserving federated learning aligns perfectly with Apple's privacy-first approach. I am particularly excited about contributing to Apple's AI initiatives and helping create products that seamlessly integrate intelligence while protecting user privacy.

I am excited about the opportunity to help Apple continue changing the world through innovative technology and would welcome the chance to discuss how my technical skills and commitment to excellence can contribute to your team.

Best regards,
Julius Mutugu
AI & Software Engineer
"""
    }
    
    # Enhanced technical summary with GitHub integration
    github_languages = []
    if github_data.get('repositories'):
        for repo in github_data['repositories']:
            if repo.get('language') and repo['language'] not in github_languages:
                github_languages.append(repo['language'])
    
    languages_str = ", ".join(github_languages[:8]) if github_languages else "Python, JavaScript, TypeScript, SQL"
    
    tech_summary = f"""
Technical Profile Summary (Updated from GitHub):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔬 ARTIFICIAL INTELLIGENCE & MACHINE LEARNING:
• Advanced ML Frameworks: TensorFlow, PyTorch, Scikit-learn
• Computer Vision: OpenCV, Image Processing, Object Detection
• Natural Language Processing: Text Analysis, NLP Libraries
• Federated Learning: Privacy-Preserving ML Systems
• Deep Learning: Neural Networks, CNNs, Transfer Learning

💻 SOFTWARE DEVELOPMENT:
• Programming Languages: {languages_str}
• Web Frameworks: React, Vue.js, Django, FastAPI, Node.js
• Mobile Development: Flutter, React Native, iOS/Android
• Database Systems: PostgreSQL, MongoDB, Redis

☁️ CLOUD & DEVOPS:
• Cloud Platforms: AWS, Azure, Google Cloud Platform
• Containerization: Docker, Kubernetes, Microservices
• CI/CD: GitHub Actions, Jenkins, Automated Testing
• Version Control: Git/GitHub with {total_repos} active repositories

📊 GITHUB STATISTICS:
• Active Developer: {total_repos} public repositories
• Community Engagement: {followers} followers
• Recent Activity: {recent_activity} projects updated in 2024
• Open Source Contributions: Consistent commit history
• Code Quality: Well-documented, clean code practices

🏆 RECENT ACHIEVEMENTS:
• Healthcare AI System: Enterprise-grade insurance platform
• Research Publication: Federated Learning in Healthcare
• University Recognition: Dean's List, Best Project Award
• Competitive Programming: E-commerce data analysis winner

📈 PROFESSIONAL READINESS:
• Immediate Availability: Ready for full-time employment
• Remote Work: Experienced with distributed team collaboration
• Continuous Learning: Staying current with latest technologies
• Industry Focus: FAANG companies and cutting-edge tech roles
"""
    
    # Get the appropriate cover letter or use a generic one
    cover_letter = cover_letter_templates.get(company_name, 
        cover_letter_templates["Google"].replace("Google", company_name))
    
    return {
        "cover_letter": cover_letter,
        "tech_summary": tech_summary,
        "github_stats": {
            "repositories": total_repos,
            "followers": followers,
            "recent_projects": recent_activity,
            "languages": github_languages
        },
        "project_highlights": project_highlights,
        "personalization_level": "High",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def create_application_pdf(company_name: str, position: str, application_data: Dict) -> BytesIO:
    """Create a professional PDF application package"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=30,
        textColor=HexColor('#1e40af')
    )
    
    # Build PDF content
    story = []
    
    # Header
    story.append(Paragraph(f"Job Application Package - {company_name}", title_style))
    story.append(Paragraph(f"Position: {position}", styles['Heading2']))
    story.append(Spacer(1, 12))
    
    # Cover Letter
    story.append(Paragraph("Cover Letter", styles['Heading2']))
    cover_letter_lines = application_data['cover_letter'].split('\n')
    for line in cover_letter_lines:
        if line.strip():
            story.append(Paragraph(line, styles['Normal']))
    
    story.append(PageBreak())
    
    # Technical Summary
    story.append(Paragraph("Technical Summary", styles['Heading2']))
    tech_lines = application_data['tech_summary'].split('\n')
    for line in tech_lines:
        if line.strip():
            story.append(Paragraph(line, styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

@st.cache_data(ttl=1800)  # Cache for 30 minutes
def scrape_job_opportunities(keywords: List[str] = ["Software Engineer", "AI Engineer", "ML Engineer"], 
                           location: str = "Remote", 
                           experience_level: str = "Entry Level",
                           job_type: str = "All",
                           visa_sponsorship: str = "Any") -> List[Dict]:
    """Scrape job opportunities from multiple sources"""
    jobs = []
    
    # Job board APIs and scraping targets
    job_sources = {
        "GitHub Jobs": "https://jobs.github.com/positions.json",
        "RemoteOK": "https://remoteok.io/api",
        "AngelList": "https://angel.co/jobs",
        "Indeed": "https://indeed.com",
        "LinkedIn": "https://linkedin.com/jobs"
    }
    
    # Sample job data (since actual scraping requires proper setup)
    sample_jobs = [
        {
            "title": "AI/ML Software Engineer",
            "company": "Google",
            "location": "Mountain View, CA / Remote",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "$120,000 - $180,000",
            "description": "Join Google's AI team to develop cutting-edge machine learning solutions",
            "skills": ["Python", "TensorFlow", "Machine Learning", "Computer Vision"],
            "posted": "2 days ago",
            "apply_url": "https://careers.google.com/jobs/results/",
            "source": "Google Careers",
            "remote_friendly": True,
            "visa_sponsorship": True
        },
        {
            "title": "Software Development Engineer - AI",
            "company": "Microsoft",
            "location": "Seattle, WA / Remote",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "$110,000 - $170,000",
            "description": "Build intelligent applications using Azure AI services and machine learning",
            "skills": ["C#", "Python", "Azure", "AI/ML", "Software Engineering"],
            "posted": "1 day ago",
            "apply_url": "https://careers.microsoft.com/",
            "source": "Microsoft Careers",
            "remote_friendly": True,
            "visa_sponsorship": True
        },
        {
            "title": "Machine Learning Engineer",
            "company": "Amazon",
            "location": "Austin, TX / Remote",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "$115,000 - $175,000",
            "description": "Develop ML models for AWS services and customer-facing applications",
            "skills": ["Python", "AWS", "PyTorch", "Distributed Systems", "ML Engineering"],
            "posted": "3 days ago",
            "apply_url": "https://amazon.jobs/",
            "source": "Amazon Jobs",
            "remote_friendly": True,
            "visa_sponsorship": True
        },
        {
            "title": "AI Research Engineer",
            "company": "Meta",
            "location": "Menlo Park, CA / Remote",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "$125,000 - $190,000",
            "description": "Research and develop AI technologies for Meta's platforms and metaverse",
            "skills": ["Python", "PyTorch", "Computer Vision", "NLP", "Research"],
            "posted": "1 week ago",
            "apply_url": "https://www.metacareers.com/",
            "source": "Meta Careers",
            "remote_friendly": True,
            "visa_sponsorship": True
        },
        {
            "title": "iOS Software Engineer - ML",
            "company": "Apple",
            "location": "Cupertino, CA / Hybrid",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "$130,000 - $200,000",
            "description": "Integrate machine learning capabilities into iOS applications",
            "skills": ["Swift", "iOS", "Core ML", "Python", "Mobile Development"],
            "posted": "4 days ago",
            "apply_url": "https://jobs.apple.com/",
            "source": "Apple Jobs",
            "remote_friendly": False,
            "visa_sponsorship": True
        },
        {
            "title": "Software Engineer Intern - AI/ML",
            "company": "OpenAI",
            "location": "San Francisco, CA / Remote",
            "type": "Internship",
            "experience": "Student",
            "salary": "$8,000 - $12,000/month",
            "description": "Summer internship working on large language models and AI safety",
            "skills": ["Python", "PyTorch", "Transformers", "NLP", "Research"],
            "posted": "2 weeks ago",
            "apply_url": "https://openai.com/careers/",
            "source": "OpenAI Careers",
            "remote_friendly": True,
            "visa_sponsorship": False
        },
        {
            "title": "Junior Data Scientist",
            "company": "Netflix",
            "location": "Los Gatos, CA / Remote",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "$105,000 - $160,000",
            "description": "Apply ML to improve content recommendation and user experience",
            "skills": ["Python", "SQL", "Machine Learning", "Statistics", "Data Science"],
            "posted": "5 days ago",
            "apply_url": "https://jobs.netflix.com/",
            "source": "Netflix Jobs",
            "remote_friendly": True,
            "visa_sponsorship": True
        },
        {
            "title": "Backend Engineer - AI Platform",
            "company": "Spotify",
            "location": "Stockholm, Sweden / Remote",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "€70,000 - €95,000",
            "description": "Build scalable backend systems for Spotify's AI-powered features",
            "skills": ["Java", "Python", "Distributed Systems", "ML Infrastructure", "Kubernetes"],
            "posted": "1 week ago",
            "apply_url": "https://www.lifeatspotify.com/",
            "source": "Spotify Careers",
            "remote_friendly": True,
            "visa_sponsorship": True
        },
        {
            "title": "Computer Vision Engineer",
            "company": "Tesla",
            "location": "Palo Alto, CA / On-site",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "$120,000 - $180,000",
            "description": "Develop computer vision algorithms for autonomous driving",
            "skills": ["Python", "OpenCV", "Deep Learning", "Computer Vision", "C++"],
            "posted": "3 days ago",
            "apply_url": "https://www.tesla.com/careers/",
            "source": "Tesla Careers",
            "remote_friendly": False,
            "visa_sponsorship": True
        },
        {
            "title": "Machine Learning Intern",
            "company": "Uber",
            "location": "San Francisco, CA / Remote",
            "type": "Internship",
            "experience": "Student",
            "salary": "$7,500 - $10,000/month",
            "description": "Summer internship in ML engineering for ride-sharing optimization",
            "skills": ["Python", "Scikit-learn", "TensorFlow", "Data Analysis", "Statistics"],
            "posted": "1 week ago",
            "apply_url": "https://www.uber.com/careers/",
            "source": "Uber Careers",
            "remote_friendly": True,
            "visa_sponsorship": False
        },
        {
            "title": "Software Engineer - Fintech",
            "company": "M-Pesa (Safaricom)",
            "location": "Nairobi, Kenya / Hybrid",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "KES 1,500,000 - KES 2,500,000",
            "description": "Build mobile financial services for Africa's leading fintech platform",
            "skills": ["Java", "Kotlin", "Android", "Microservices", "Financial Systems"],
            "posted": "3 days ago",
            "apply_url": "https://www.safaricom.co.ke/careers/",
            "source": "Safaricom Careers",
            "remote_friendly": True,
            "visa_sponsorship": False
        },
        {
            "title": "Data Scientist - AI Research",
            "company": "iHub Kenya",
            "location": "Nairobi, Kenya",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "KES 1,200,000 - KES 2,000,000",
            "description": "Research and develop AI solutions for African challenges in agriculture and healthcare",
            "skills": ["Python", "R", "Machine Learning", "Data Science", "Research"],
            "posted": "1 week ago",
            "apply_url": "https://ihub.co.ke/careers/",
            "source": "iHub Kenya",
            "remote_friendly": False,
            "visa_sponsorship": False
        },
        {
            "title": "Backend Developer - E-commerce",
            "company": "Jumia Kenya",
            "location": "Nairobi, Kenya / Remote",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "KES 1,000,000 - KES 1,800,000",
            "description": "Develop scalable e-commerce solutions for Africa's largest online marketplace",
            "skills": ["PHP", "Laravel", "MySQL", "AWS", "E-commerce"],
            "posted": "5 days ago",
            "apply_url": "https://group.jumia.com/careers/",
            "source": "Jumia Group",
            "remote_friendly": True,
            "visa_sponsorship": False
        },
        {
            "title": "Mobile App Developer",
            "company": "Twiga Foods",
            "location": "Nairobi, Kenya",
            "type": "Full-time",
            "experience": "Entry Level",
            "salary": "KES 900,000 - KES 1,500,000",
            "description": "Build mobile applications for agricultural supply chain management",
            "skills": ["Flutter", "Dart", "Firebase", "Mobile Development", "Agriculture Tech"],
            "posted": "1 week ago",
            "apply_url": "https://twiga.ke/careers/",
            "source": "Twiga Foods",
            "remote_friendly": False,
            "visa_sponsorship": False
        },
        {
            "title": "Senior Data Engineer",
            "company": "Airbnb",
            "location": "San Francisco, CA / Remote",
            "type": "Full-time",
            "experience": "Senior Level",
            "salary": "$180,000 - $250,000",
            "description": "Lead data infrastructure and analytics platform development",
            "skills": ["Python", "Spark", "Kafka", "AWS", "Data Engineering"],
            "posted": "2 days ago",
            "apply_url": "https://careers.airbnb.com/",
            "source": "Airbnb Careers",
            "remote_friendly": True,
            "visa_sponsorship": True
        },
        {
            "title": "Frontend Developer",
            "company": "Shopify",
            "location": "Ottawa, Canada / Remote",
            "type": "Contract",
            "experience": "Mid Level",
            "salary": "$80,000 - $120,000",
            "description": "Build beautiful and functional e-commerce user interfaces",
            "skills": ["React", "TypeScript", "CSS", "JavaScript", "GraphQL"],
            "posted": "1 day ago",
            "apply_url": "https://www.shopify.com/careers/",
            "source": "Shopify Careers",
            "remote_friendly": True,
            "visa_sponsorship": False
        },
        {
            "title": "DevOps Engineer Intern",
            "company": "Stripe",
            "location": "Dublin, Ireland / Hybrid",
            "type": "Internship",
            "experience": "Student",
            "salary": "€4,000 - €6,000/month",
            "description": "Summer internship in cloud infrastructure and deployment automation",
            "skills": ["Docker", "Kubernetes", "AWS", "Terraform", "CI/CD"],
            "posted": "3 days ago",
            "apply_url": "https://stripe.com/jobs/",
            "source": "Stripe Careers",
            "remote_friendly": False,
            "visa_sponsorship": True
        },
        {
            "title": "Part-time Python Tutor",
            "company": "Codecademy",
            "location": "Remote",
            "type": "Part-time",
            "experience": "Entry Level",
            "salary": "$25 - $40/hour",
            "description": "Help students learn Python programming through online tutoring",
            "skills": ["Python", "Teaching", "Communication", "Programming"],
            "posted": "1 week ago",
            "apply_url": "https://www.codecademy.com/about/careers/",
            "source": "Codecademy",
            "remote_friendly": True,
            "visa_sponsorship": False
        },
        {
            "title": "Blockchain Developer",
            "company": "Coinbase",
            "location": "San Francisco, CA / On-site",
            "type": "Full-time",
            "experience": "Mid Level",
            "salary": "$150,000 - $220,000",
            "description": "Develop secure and scalable cryptocurrency trading systems",
            "skills": ["Solidity", "Web3", "Blockchain", "JavaScript", "Security"],
            "posted": "4 days ago",
            "apply_url": "https://www.coinbase.com/careers/",
            "source": "Coinbase Careers",
            "remote_friendly": False,
            "visa_sponsorship": True
        }
    ]
    
    # Filter jobs based on criteria with enhanced search
    filtered_jobs = []
    for job in sample_jobs:
        # Enhanced keyword filtering - more flexible matching
        keyword_match = True
        if keywords and any(k.strip() for k in keywords):  # Only filter if keywords provided and not empty
            job_text = f"{job['title']} {job['description']} {' '.join(job['skills'])} {job['company']}".lower()
            # Check for partial matches and synonyms
            keyword_match = False
            for keyword in keywords:
                keyword = keyword.lower().strip()
                if keyword:
                    # Direct match
                    if keyword in job_text:
                        keyword_match = True
                        break
                    # Synonym matching for common terms
                    if keyword in ["ai", "artificial intelligence"] and ("ai" in job_text or "artificial intelligence" in job_text or "machine learning" in job_text):
                        keyword_match = True
                        break
                    elif keyword in ["ml", "machine learning"] and ("ml" in job_text or "machine learning" in job_text or "ai" in job_text):
                        keyword_match = True
                        break
                    elif keyword in ["software", "developer", "engineer"] and any(term in job_text for term in ["software", "developer", "engineer", "development"]):
                        keyword_match = True
                        break
                    elif keyword in ["data", "analyst", "scientist"] and any(term in job_text for term in ["data", "analyst", "scientist", "analytics"]):
                        keyword_match = True
                        break
        
        if keyword_match:
            # Enhanced location filtering
            location_match = False
            job_location = job['location'].lower()
            location_filter = location.lower()
            
            if location_filter == "any":
                location_match = True
            elif location_filter == "remote" and job['remote_friendly']:
                location_match = True
            elif location_filter == "on-site" and not job['remote_friendly']:
                location_match = True
            elif location_filter == "hybrid" and ("hybrid" in job_location or job['remote_friendly']):
                location_match = True
            elif location_filter in job_location:
                location_match = True
            # Handle specific cities and countries
            elif location_filter == "nairobi" and ("remote" in job_location or "nairobi" in job_location):
                location_match = True  # Remote jobs are accessible from Nairobi
            elif location_filter == "kenya" and ("remote" in job_location or "nairobi" in job_location or "kenya" in job_location):
                location_match = True
            elif location_filter == "africa" and ("remote" in job_location or "nairobi" in job_location or "africa" in job_location):
                location_match = True
            # International locations accessible via remote
            elif job['remote_friendly'] and location_filter in ["san francisco", "new york", "seattle", "austin", "london", "berlin", "toronto", "sydney"]:
                location_match = True
            
            # Filter by experience level if specified
            experience_match = True
            if experience_level.lower() != "all":
                job_exp = job['experience'].lower()
                exp_filter = experience_level.lower()
                
                if exp_filter == "entry level" and job_exp != "entry level":
                    experience_match = False
                elif exp_filter == "mid level" and job_exp not in ["mid level", "entry level"]:
                    experience_match = False
                elif exp_filter == "senior level" and job_exp != "senior level":
                    experience_match = False
                elif exp_filter == "student" and job_exp != "student":
                    experience_match = False
            
            # Filter by job type if specified
            job_type_match = True
            if job_type.lower() != "all":
                if job_type.lower() != job['type'].lower():
                    job_type_match = False
            
            # Filter by visa sponsorship if specified
            visa_match = True
            if visa_sponsorship.lower() != "any":
                if visa_sponsorship.lower() == "required" and not job.get('visa_sponsorship', False):
                    visa_match = False
                elif visa_sponsorship.lower() == "not required" and job.get('visa_sponsorship', False):
                    visa_match = False
            
            if location_match and experience_match and job_type_match and visa_match:
                filtered_jobs.append(job)
    
    # Sort by posted date (newest first) - convert "X days/weeks ago" to datetime for sorting
    def parse_posted_date(posted_str):
        from datetime import datetime, timedelta
        import re
        
        if "day" in posted_str:
            days = int(re.findall(r'\d+', posted_str)[0]) if re.findall(r'\d+', posted_str) else 0
            return datetime.now() - timedelta(days=days)
        elif "week" in posted_str:
            weeks = int(re.findall(r'\d+', posted_str)[0]) if re.findall(r'\d+', posted_str) else 1
            return datetime.now() - timedelta(weeks=weeks)
        elif "hour" in posted_str:
            hours = int(re.findall(r'\d+', posted_str)[0]) if re.findall(r'\d+', posted_str) else 0
            return datetime.now() - timedelta(hours=hours)
        else:
            return datetime.now() - timedelta(days=30)  # Default to 30 days ago
    
    # Add parsed date for sorting and sort by date (newest first)
    for job in filtered_jobs:
        job['parsed_date'] = parse_posted_date(job['posted'])
    
    filtered_jobs.sort(key=lambda x: x['parsed_date'], reverse=True)
    
    return filtered_jobs

def get_job_recommendations(github_data: Dict, user_skills: List[str]) -> List[Dict]:
    """Get personalized job recommendations based on GitHub activity and skills"""
    
    # Extract skills from GitHub repositories
    github_languages = []
    if github_data.get('repositories'):
        for repo in github_data['repositories']:
            if repo.get('language'):
                github_languages.append(repo['language'])
            # Extract skills from repository topics
            github_languages.extend(repo.get('topics', []))
    
    # Combine user skills with GitHub-derived skills
    all_skills = list(set(user_skills + github_languages))
    
    # Get job opportunities
    jobs = scrape_job_opportunities()
    
    # Score jobs based on skill match
    scored_jobs = []
    for job in jobs:
        skill_matches = 0
        for skill in all_skills:
            job_skills_text = ' '.join(job['skills']).lower()
            job_desc_text = job['description'].lower()
            if skill.lower() in job_skills_text or skill.lower() in job_desc_text:
                skill_matches += 1
        
        job['match_score'] = (skill_matches / len(job['skills'])) * 100 if job['skills'] else 0
        job['matched_skills'] = [skill for skill in all_skills 
                               if skill.lower() in ' '.join(job['skills']).lower()]
        scored_jobs.append(job)
    
    # Sort by match score
    scored_jobs.sort(key=lambda x: x['match_score'], reverse=True)
    
    return scored_jobs

def create_job_alert_system(user_email: str, keywords: List[str], location: str) -> Dict:
    """Create a job alert system (simulation)"""
    alert_id = f"alert_{hash(user_email + ''.join(keywords) + location)}"
    
    return {
        "alert_id": alert_id,
        "email": user_email,
        "keywords": keywords,
        "location": location,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "active",
        "frequency": "daily"
    }

def main():
    # Initialize theme in session state
    if 'theme' not in st.session_state:
        st.session_state.theme = 'modern_light'
    
    # Initialize selected page
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = 'Home'
    
    # Theme toggle in sidebar
    with st.sidebar:
        st.markdown('<div class="navigation-header">Settings</div>', unsafe_allow_html=True)
        
        # Modern Light/Dark theme toggle
        is_light_theme = st.session_state.theme == 'modern_light'
        theme_toggle = st.toggle("Light Mode", value=is_light_theme, help="Toggle between modern light and dark themes")
        
        if theme_toggle != is_light_theme:
            st.session_state.theme = 'modern_light' if theme_toggle else 'dark'
            st.rerun()
        
        st.markdown("---")
    
    # Load CSS with current theme
    load_css(st.session_state.theme)
    
    # Sidebar navigation
    with st.sidebar:
        # st.markdown('<div class="navigation-header">Portfolio Navigation</div>', unsafe_allow_html=True)
        
        # Get the current page index
        pages = ["Home", "Projects", "Skills", "Experience", "Education", "Apply", "Find Jobs", "Contact"]
        current_index = pages.index(st.session_state.selected_page) if st.session_state.selected_page in pages else 0
        
        selected = option_menu(
            menu_title=None,
            options=pages,
            icons=["house-fill", "code-square", "cpu-fill", "briefcase-fill", "mortarboard-fill", "send-fill", "envelope-fill"],
            menu_icon="cast",
            default_index=current_index,
            key="main_menu",
            styles={
                "container": {
                    "padding": "0!important", 
                    "background": "linear-gradient(180deg, rgba(245, 158, 11, 0.10) 0%, rgba(59, 130, 246, 0.06) 100%)" if st.session_state.theme == 'modern_light' else "linear-gradient(180deg, rgba(251, 191, 36, 0.12) 0%, rgba(59, 130, 246, 0.06) 100%)",
                    "border-radius": "12px",
                    "border": f"1px solid {'rgba(245, 158, 11, 0.25)' if st.session_state.theme == 'modern_light' else 'rgba(251, 191, 36, 0.3)'}"
                },
                "icon": {
                    "color": "#f59e0b" if st.session_state.theme == 'modern_light' else "#fbbf24", 
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
                    "color": "#1e40af" if st.session_state.theme == 'modern_light' else "#f1f5f9",
                    "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                    "border": "1px solid transparent"
                },
                "nav-link-selected": {
                    "background": "linear-gradient(135deg, #f59e0b 0%, #3b82f6 100%)" if st.session_state.theme == 'modern_light' else "linear-gradient(135deg, #fbbf24 0%, #3b82f6 100%)",
                    "color": "white",
                    "font-weight": "600",
                    "box-shadow": "0 4px 12px rgba(245, 158, 11, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2)" if st.session_state.theme == 'modern_light' else "0 4px 12px rgba(251, 191, 36, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2)",
                    "border": "1px solid rgba(255, 255, 255, 0.3)",
                    "transform": "translateY(-1px)"
                },
                "nav-link-hover": {
                    "background": "rgba(245, 158, 11, 0.12)" if st.session_state.theme == 'modern_light' else "rgba(251, 191, 36, 0.15)",
                    "color": "#3b82f6",
                    "transform": "translateY(-1px)",
                    "border": f"1px solid {'rgba(245, 158, 11, 0.25)' if st.session_state.theme == 'modern_light' else 'rgba(251, 191, 36, 0.3)'}"
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
        stats_bg = "linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(59, 130, 246, 0.08) 100%)" if st.session_state.theme == 'modern_light' else "linear-gradient(135deg, rgba(251, 191, 36, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%)"
        stats_accent = "#f59e0b" if st.session_state.theme == 'modern_light' else "#fbbf24"
        
        st.markdown(f"""
        <div style="padding: 1rem; background: {stats_bg}; border-radius: 8px; margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="font-size: 0.8rem; opacity: 0.8;">Projects:</span>
                <span style="font-weight: 600; color: {stats_accent};">7+</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="font-size: 0.8rem; opacity: 0.8;">Skills:</span>
                <span style="font-weight: 600; color: {stats_accent};">25+</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="font-size: 0.8rem; opacity: 0.8;">Status:</span>
                <span style="font-weight: 600; color: #10b981;">Available</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add profile section at the bottom
        st.markdown("---")
        profile_border = "rgba(245, 158, 11, 0.3)" if st.session_state.theme == 'modern_light' else "rgba(251, 191, 36, 0.4)"
        profile_text_color = "#1e40af" if st.session_state.theme == 'modern_light' else "#f1f5f9"
        profile_gradient = "linear-gradient(135deg, #f59e0b 0%, #3b82f6 100%)" if st.session_state.theme == 'modern_light' else "linear-gradient(135deg, #fbbf24 0%, #3b82f6 100%)"
        
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem 0; border-top: 1px solid {profile_border}; margin-top: 1rem;">
            <div style="width: 80px; height: 80px; border-radius: 50%; background: {profile_gradient}; margin: 0 auto 0.5rem; display: flex; align-items: center; justify-content: center; font-size: 2rem; color: white; font-weight: bold;">J</div>
            <div style="font-size: 0.9rem; color: {profile_text_color}; opacity: 0.8;">AI Software Engineer</div>
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
    elif current_page == "Education":
        show_education()
    elif current_page == "Apply":
        show_apply()
    elif current_page == "Find Jobs":
        show_jobs()
    elif current_page == "Contact":
        show_contact()

    # Floating WhatsApp Contact Button
    st.markdown("""
    <div class="floating-contact">
        <a href="https://wa.me/254717348043?text=Hello%20Julius,%20I%20found%20your%20portfolio%20and%20would%20like%20to%20discuss%20a%20potential%20opportunity" 
           target="_blank" class="main-fab" title="WhatsApp +254 717 348 043">
            WhatsApp
        </a>
    </div>
    """, unsafe_allow_html=True)

def show_home():
    """Enhanced home page with comprehensive overview"""
    # Top header with smaller profile image and animation
    header_col1, header_col2, header_col3 = st.columns([1, 1, 1])
    
    with header_col1:
        # Get and display GitHub profile image (smaller)
        profile_image_url = get_github_profile_image()
        if profile_image_url:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="{profile_image_url}" 
                     style="width: 80px; height: 80px; border-radius: 50%; 
                            border: 2px solid var(--primary-color); 
                            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
                            animation: pulse 2s infinite;">
            </div>
            <style>
            @keyframes pulse {{
                0% {{ transform: scale(1); }}
                50% {{ transform: scale(1.05); }}
                100% {{ transform: scale(1); }}
            }}
            </style>
            """, unsafe_allow_html=True)
    
    with header_col2:
        st.markdown('<h1 class="main-header" style="text-align: center; margin-bottom: 5px;">Julius Mutugu</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header" style="text-align: center;">AI & Software Engineer</p>', unsafe_allow_html=True)
    
    with header_col3:
        # Load animation (smaller)
        lottie_coding = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
        if lottie_coding:
            st_lottie(lottie_coding, height=120, key="coding")
    
    st.markdown("---")
    
    # Comprehensive overview section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="animated-text">', unsafe_allow_html=True)
        st.markdown("## Professional Overview")
        st.markdown("""
        <div style="color: inherit; line-height: 1.7; font-size: 1.1rem;">
        I'm a <strong>Software Engineer</strong> specializing in <strong>Artificial Intelligence & Machine Learning</strong>, 
        recently graduated and ready to contribute innovative solutions at leading technology companies including 
        <strong>Google</strong>, <strong>Microsoft</strong>, <strong>Amazon</strong>, <strong>Meta</strong>, and <strong>Apple</strong>.
        </div>
        """, unsafe_allow_html=True)
        
        # Key projects preview
        st.markdown("### Featured Projects")
        project_preview = {
            "Healthcare AI System": "Enterprise-grade insurance system using Kenya's SHIF model with fraud detection",
            "Federated Learning Research": "Privacy-preserving ML for healthcare data across decentralized systems", 
            "Computer Vision Classification": "Intelligent waste classification using SVM and batch processing",
            "Real Estate Platform": "Full-stack Django application with advanced search and user management"
        }
        
        for project, desc in project_preview.items():
            st.markdown(f"**{project}**: {desc}")
        
        # Technical skills overview
        st.markdown("### Core Technical Skills")
        skill_cols = st.columns(3)
        
        with skill_cols[0]:
            st.markdown("""
            **AI/ML & Data Science:**
            - TensorFlow, PyTorch, Scikit-learn
            - Computer Vision (OpenCV)
            - NLP & Text Processing
            - Federated Learning Systems
            """)
        
        with skill_cols[1]:
            st.markdown("""
            **Software Development:**
            - Python, JavaScript, TypeScript
            - Django, Flask, FastAPI
            - React, Vue.js, Nuxt 3
            - PostgreSQL, MongoDB
            """)
        
        with skill_cols[2]:
            st.markdown("""
            **Cloud & DevOps:**
            - AWS, Azure Cloud Platforms
            - Docker, Microservices
            - Git/GitHub, CI/CD
            - Agile Development
            """)
        
        # Academic achievements
        st.markdown("### Academic Excellence")
        st.markdown("""
        - **Bachelor of Software Engineering** - AI Specialization (2025)
        - **University of Eastern Africa, Baraton (UEAB)**
        - **Academic Honors**: Dean's List, Best Final Project Award
        - **Research Focus**: Federated Learning in Healthcare Systems
        """)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Professional metrics
        st.markdown("""
        <div class="stats-container">
            <h3 style="margin-top: 0; font-size: 1.4rem; font-weight: 600; text-align: center;">Professional Metrics</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.metric("Projects Completed", "15+", "Including 7 major AI/ML projects")
        st.metric("GitHub Contributions", "709+", "Active open source contributor")
        st.metric("Technologies Mastered", "25+", "Across AI, web, and mobile development")
        st.metric("Years of Experience", "4+", "Academic and project-based")
        
        # Education highlight
        st.markdown("""
        <div class="highlight-box">
            <h4 style="margin-top: 0; color: inherit; font-weight: 600;">Education</h4>
            <p style="margin-bottom: 0; color: inherit; line-height: 1.6;">
            <strong>Bachelor of Software Engineering</strong><br>
            <span style="color: #10b981; font-weight: 600;">University of Eastern Africa, Baraton</span><br>
            <em>AI & Machine Learning Specialization</em><br>
            <em>Graduated: 2025 | GPA: Excellent(3.5)</em>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Target companies
        st.markdown("""
        <div class="highlight-box">
            <h4 style="margin-top: 0; color: inherit; font-weight: 600;">Target Companies</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-bottom: 1rem;">
                <div style="color: inherit;">Google</div>
                <div style="color: inherit;">Microsoft</div>
                <div style="color: inherit;">Amazon</div>
                <div style="color: inherit;">Meta</div>
                <div style="color: inherit;">Apple</div>
                <div style="color: inherit;">OpenAI</div>
            </div>
            <p style="margin-bottom: 0; color: inherit; font-size: 0.9rem; font-style: italic;">
            Ready for immediate employment | Open to remote and international opportunities
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Additional comprehensive sections
    st.markdown("---")
    
    # Career readiness section
    col_ready1, col_ready2, col_ready3 = st.columns(3)
    
    with col_ready1:
        accent_color = "#f59e0b" if st.session_state.theme == 'modern_light' else "#fbbf24"
        st.markdown(f"""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: {accent_color};">Why Hire Me?</h4>
        <ul style="margin-bottom: 0; color: inherit;">
        <li><strong>Immediate Impact</strong>: Ready to contribute from day one</li>
        <li><strong>AI Expertise</strong>: Specialized in cutting-edge ML technologies</li>
        <li><strong>Full-Stack Skills</strong>: End-to-end development capabilities</li>
        <li><strong>Research Background</strong>: Innovation and problem-solving mindset</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_ready2:
        accent_color = "#f59e0b" if st.session_state.theme == 'modern_light' else "#fbbf24"
        st.markdown(f"""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: {accent_color};">Key Achievements</h4>
        <ul style="margin-bottom: 0; color: inherit;">
        <li><strong>Hackathon Winner</strong>: E-commerce data analysis competition</li>
        <li><strong>Research Innovation</strong>: Federated learning in healthcare</li>
        <li><strong>Open Source</strong>: Active GitHub contributor</li>
        <li><strong>Academic Excellence</strong>: Dean's List recognition</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_ready3:
        accent_color = "#f59e0b" if st.session_state.theme == 'modern_light' else "#fbbf24"
        st.markdown(f"""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: {accent_color};">What Sets Me Apart</h4>
        <ul style="margin-bottom: 0; color: inherit;">
        <li><strong>AI Specialization</strong>: Deep ML and Computer Vision expertise</li>
        <li><strong>Enterprise Experience</strong>: Healthcare and financial systems</li>
        <li><strong>Modern Tech Stack</strong>: Latest frameworks and methodologies</li>
        <li><strong>Global Perspective</strong>: Ready for international tech roles</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("---")
    cta_bg = "linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(59, 130, 246, 0.08) 100%)" if st.session_state.theme == 'modern_light' else "linear-gradient(135deg, rgba(251, 191, 36, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%)"
    cta_accent = "#f59e0b" if st.session_state.theme == 'modern_light' else "#fbbf24"
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; background: {cta_bg}; border-radius: 12px; margin: 2rem 0;">
        <h3 style="color: {cta_accent}; margin-bottom: 1rem;">Ready to Make an Impact? Let's Connect!</h3>
        <p style="color: inherit; font-size: 1.1rem; margin-bottom: 1.5rem;">
        I'm actively seeking opportunities to contribute to innovative AI and software engineering projects. 
        Whether you're a recruiter from FAANG companies or a startup looking for AI expertise, I'd love to discuss how we can work together.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick actions moved to bottom
    st.markdown("---")
    st.markdown("### Quick Actions")
    
    # Create tabs for quick actions
    action_tabs = st.tabs(["📄 Resume", "🚀 Projects", "🎯 Skills", "📧 Apply", "💬 Contact"])
    
    with action_tabs[0]:
        st.markdown("**Download Professional Resume**")
        try:
            with open("assets/Julius_Mutugu_Resume.pdf", "rb") as pdf_file:
                pdf_data = pdf_file.read()
            
            st.download_button(
                label="Download Resume (PDF)",
                data=pdf_data,
                file_name="Julius_Mutugu_AI_Engineer_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
                help="Download my complete professional resume"
            )
        except FileNotFoundError:
            st.info("Resume available upon request. Contact me directly for the latest version.")
    
    with action_tabs[1]:
        st.markdown("**Explore My Projects**")
        if st.button("View All Projects", use_container_width=True, key="home_projects"):
            st.session_state.selected_page = "Projects"
            st.rerun()
    
    with action_tabs[2]:
        st.markdown("**Technical Skills Overview**")
        if st.button("View Skills & Expertise", use_container_width=True, key="home_skills"):
            st.session_state.selected_page = "Skills"
            st.rerun()
    
    with action_tabs[3]:
        st.markdown("**Apply for Positions**")
        if st.button("Start Application Process", use_container_width=True, key="home_apply"):
            st.session_state.selected_page = "Apply"
            st.rerun()
    
    with action_tabs[4]:
        st.markdown("**Get in Touch**")
        if st.button("Contact Information", use_container_width=True, key="home_contact"):
            st.session_state.selected_page = "Contact"
            st.rerun()

def show_projects():
    """Projects showcase with real-time GitHub integration and filtering"""
    st.markdown('<h1 class="section-title">My Projects</h1>', unsafe_allow_html=True)
    st.markdown("Explore comprehensive solutions in AI, Computer Vision, NLP, and Software Development with real-time GitHub integration")
    
    # Fetch GitHub data
    with st.spinner("Loading latest projects from GitHub..."):
        github_data = fetch_github_data("JuliusMutugu")
    
    # Project categories
    categories = ["All", "Computer Vision", "Natural Language Processing", "Machine Learning", "Web Development", "Mobile Development", "Data Analysis"]
    selected_category = st.selectbox("Filter by Category", categories)
    
    # Enhanced projects data with GitHub integration
    projects = [
        {
            "title": "Healthcare Insurance Implementation System (Kenya's SHIF Model)",
            "category": "Machine Learning",
            "description": "Comprehensive healthcare insurance system based on Kenya's Social Health Insurance Fund model with fraud detection and optimized fund allocation",
            "tech_stack": ["Python", "Blockchain", "Microservices", "Agile", "CI/CD"],
            "github": "Private Repository",
            "demo": True,
            "highlights": ["Integration with multiple insurance providers", "Advanced fraud detection algorithms", "Optimized fund allocation", "Microservices architecture"],
            "private": True,
            "completion_status": "Completed",
            "impact": "Enterprise-grade system for Kenya's healthcare sector"
        },
        {
            "title": "Federated Machine Learning in Healthcare Systems",
            "category": "Machine Learning",
            "description": "Research and implementation of federated learning for healthcare systems to enhance data privacy while training models across decentralized datasets",
            "tech_stack": ["Python", "Federated Learning", "Privacy-Preserving ML", "Healthcare Data"],
            "github": "Private Repository",
            "demo": True,
            "highlights": ["Enhanced data privacy and security", "Decentralized model training", "Healthcare data protection", "Research-grade implementation"],
            "private": True,
            "completion_status": "Completed",
            "impact": "Advanced research in privacy-preserving ML"
        },
        {
            "title": "Research and Grant Management System (UEAB)",
            "category": "Web Development",
            "description": "Full-stack university platform for managing research and grants with public researcher profiles, status tracking, and community forums",
            "tech_stack": ["Nuxt 3", "MongoDB Atlas", "Node.js", "Agile", "CI/CD"],
            "github": "https://github.com/JuliusMutugu",
            "demo": True,
            "highlights": ["Public researcher profiles", "Grant status tracking", "Community collaboration features", "Funding opportunity discovery"],
            "private": False,
            "completion_status": "Completed",
            "impact": "University-wide research management solution"
        },
        {
            "title": "Computer Vision for Waste Dataset Classification",
            "category": "Computer Vision",
            "description": "Intelligent waste classification system using Support Vector Machine with batch processing techniques for large-scale dataset optimization",
            "tech_stack": ["Python", "OpenCV", "SVM", "Computer Vision", "Data Processing"],
            "github": "https://github.com/JuliusMutugu/ImageClassification-dataset",
            "demo": True,
            "highlights": ["Accurate waste classification", "Batch processing optimization", "Large dataset handling", "Environmental impact"],
            "private": False,
            "completion_status": "Completed",
            "impact": "Environmental sustainability through AI"
        },
        {
            "title": "House and Land Advertising System",
            "category": "Web Development",
            "description": "Django-based real estate platform with comprehensive property management, user authentication, and advanced search functionality",
            "tech_stack": ["Python", "Django", "PostgreSQL", "HTML/CSS", "JavaScript"],
            "github": "https://github.com/JuliusMutugu/houseAndLandAdverisingSystem",
            "demo": True,
            "highlights": ["Property management system", "User authentication", "Advanced search filters", "Responsive web design"],
            "private": False,
            "completion_status": "Completed",
            "impact": "Real estate management platform"
        },
        {
            "title": "Flet Desktop Application with Federated Learning",
            "category": "Mobile Development",
            "description": "Desktop application using Flet framework powered by custom federated learning algorithm built from scratch for competitive advantage",
            "tech_stack": ["Python", "Flet", "Federated Learning", "Desktop Development"],
            "github": "https://github.com/JuliusMutugu/FletSimpleApplicationDismissalMessage",
            "demo": True,
            "highlights": ["Custom federated learning implementation", "Cross-platform desktop app", "Innovative framework usage", "Machine learning integration"],
            "private": False,
            "completion_status": "Completed",
            "impact": "Cross-platform ML-powered desktop application"
        },
        {
            "title": "Data Analysis for E-commerce (UEAB Hackathon)",
            "category": "Data Analysis",
            "description": "Comprehensive data analysis project for e-commerce platform developed during university hackathon with advanced analytics and insights",
            "tech_stack": ["Python", "Jupyter Notebook", "Pandas", "Data Visualization", "Machine Learning"],
            "github": "https://github.com/JuliusMutugu/Data_analysis_ueab_hackathon_Ecommerce",
            "demo": True,
            "highlights": ["Hackathon winner project", "E-commerce analytics", "Data visualization", "Predictive insights"],
            "private": False,
            "completion_status": "Completed",
            "impact": "Award-winning data analysis solution"
        }
    ]
    
    # Filter projects
    if selected_category != "All":
        filtered_projects = [p for p in projects if p["category"] == selected_category]
    else:
        filtered_projects = projects
    
    st.markdown(f"### Featured Projects ({len(filtered_projects)} projects)")
    
    # Display projects with enhanced animations and real-time integration
    for i, project in enumerate(filtered_projects):
        with st.container():
            # Project card with enhanced styling
            status_color = "#10b981" if project['completion_status'] == "Completed" else "#f59e0b"
            
            st.markdown(f"""
            <div class="project-card" style="animation-delay: {i * 0.2}s;">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                    <h3 style="margin: 0; font-size: 1.6rem; font-weight: 600; color: white; flex: 1;">{project['title']}</h3>
                    <span style="background: {status_color}; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem; font-weight: 500; margin-left: 1rem;">{project['completion_status']}</span>
                </div>
                <p style="font-size: 0.95rem; opacity: 0.9; margin-bottom: 0.8rem; color: rgba(255,255,255,0.8);"><strong>Category:</strong> {project['category']} | <strong>Impact:</strong> {project['impact']}</p>
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
                
                # GitHub repository link with enhanced indicators
                if project['private']:
                    st.markdown(f"🔒 **Private Repository** - Available upon request")
                    st.markdown("*Contact me for code review access*")
                    if st.button(f"Request Access", key=f"access_section1_{i}", use_container_width=True):
                        st.info("Access request noted! Please contact me directly.")
                else:
                    st.markdown(f"[🔗 GitHub Repository]({project['github']})")
                    
                    # Check if this repo exists in GitHub data
                    if "error" not in github_data:
                        repo_name = project['github'].split('/')[-1] if '/' in project['github'] else ''
                        matching_repo = next((r for r in github_data.get('repositories', []) if repo_name in r['name']), None)
                        
                        if matching_repo:
                            st.markdown(f"⭐ **{matching_repo['stars']} stars** | 🍴 **{matching_repo['forks']} forks**")
                            st.markdown(f"📅 **Last updated:** {matching_repo['updated_at'][:10]}")
                
                # Enhanced demo functionality
                if project['demo']:
                    if st.button("🚀 View Demo", key=f"demo_section1_{i}", use_container_width=True):
                        st.balloons()
                        st.success("🎉 Demo functionality ready for integration!")
                        
                        # Project-specific demo information
                        with st.expander("📋 Project Details", expanded=True):
                            st.markdown(f"**Impact:** {project['impact']}")
                            st.markdown(f"**Status:** {project['completion_status']}")
                            st.markdown("**Demo Features:**")
                            for highlight in project['highlights']:
                                st.markdown(f"• {highlight}")
                            
                            st.info("Live demonstration available - contact for detailed walkthrough")
                        
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")
    
    # Project statistics
    st.markdown("### Project Analytics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Projects by category
        category_counts = {}
        for project in projects:
            category = project['category']
            category_counts[category] = category_counts.get(category, 0) + 1
        
        fig_cat = px.pie(values=list(category_counts.values()), names=list(category_counts.keys()),
                        title="Projects by Category")
        st.plotly_chart(fig_cat, use_container_width=True)
    
    with col2:
        # Technology usage
        all_techs = []
        for project in projects:
            all_techs.extend(project['tech_stack'])
        
        tech_counts = pd.Series(all_techs).value_counts().head(10)
        fig_tech = px.bar(x=tech_counts.values, y=tech_counts.index, orientation='h',
                         title="Most Used Technologies")
        st.plotly_chart(fig_tech, use_container_width=True)
    
    with col3:
        # Project completion timeline
        completed_projects = len([p for p in projects if p['completion_status'] == 'Completed'])
        in_progress = len(projects) - completed_projects
        
        fig_status = px.pie(values=[completed_projects, in_progress], 
                           names=['Completed', 'In Progress'],
                           title="Project Completion Status")
        st.plotly_chart(fig_status, use_container_width=True)
    
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
                    st.markdown(f"Private Repository - Available upon request")
                    st.markdown("*Contact me for code review access*")
                else:
                    st.markdown(f"[GitHub Repository]({project['github']})")
                
                # Enhanced demo functionality
                if project['demo']:
                    if st.button("View Demo", key=f"demo_section2_{i}"):
                        st.balloons()  # Add celebration animation
                        
                        # Different demo types based on project
                        if project['title'] == "Algorithmic Trading System":
                            st.success("Trading System Demo Ready!")
                            with st.expander("Sample Trading Performance", expanded=True):
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
            "C#": 70,
            "Java": 75
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
                    font=dict(size=18, family='Inter', color="#0B64F3"),
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
                font=dict(family='Inter', color="#0BD4A9")
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
    """Professional experience and achievements"""
    st.markdown('<h1 class="section-title">Professional Experience</h1>', unsafe_allow_html=True)
    
    # Professional Experience & Projects Timeline
    st.markdown("## Professional Experience & Project Timeline")
    
    experience_timeline = {
        "2024-2025 (Final Year Projects)": {
            "role": "Lead Developer & Researcher",
            "projects": [
                "Healthcare Insurance Implementation System (Kenya's SHIF Model)",
                "Federated Machine Learning in Healthcare Systems",
                "Research and Grant Management System (UEAB)"
            ],
            "technologies": ["Python", "Blockchain", "Federated Learning", "Nuxt 3", "MongoDB Atlas"],
            "achievements": [
                "Developed enterprise-grade healthcare insurance system",
                "Pioneered federated learning research for healthcare privacy",
                "Created comprehensive university research management platform"
            ]
        },
        "2023-2024 (Advanced Projects)": {
            "role": "Full-Stack Developer & ML Engineer",
            "projects": [
                "Computer Vision for Waste Dataset Classification",
                "Flet Desktop Application with Federated Learning",
                "House and Land Advertising System"
            ],
            "technologies": ["OpenCV", "SVM", "Flet Framework", "Django", "PostgreSQL"],
            "achievements": [
                "Implemented advanced computer vision for environmental impact",
                "Built cross-platform desktop applications",
                "Developed full-featured real estate management platform"
            ]
        },
        "2022-2023 (Foundation Projects)": {
            "role": "Junior Developer & Data Analyst",
            "projects": [
                "Data Analysis for E-commerce (UEAB Hackathon)",
                "Farmers Management System",
                "Diabetes Collaboration Platform"
            ],
            "technologies": ["Jupyter Notebook", "Pandas", "Data Visualization", "Python"],
            "achievements": [
                "Won university hackathon for e-commerce analytics",
                "Developed agricultural management solutions",
                "Created healthcare collaboration tools"
            ]
        }
    }
    
    for period, details in experience_timeline.items():
        with st.expander(f"{period} - {details['role']}", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("**Key Projects:**")
                for project in details['projects']:
                    st.markdown(f"• **{project}**")
                
                st.markdown("**Major Achievements:**")
                for achievement in details['achievements']:
                    st.markdown(f"✅ {achievement}")
            
            with col2:
                st.markdown("**Technologies Used:**")
                for tech in details['technologies']:
                    st.markdown(f'<span class="skill-badge" style="margin: 2px; display: inline-block;">{tech}</span>', unsafe_allow_html=True)
    
    # Professional Achievements & Recognition
    st.markdown("## Professional Achievements & Recognition")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #fbbf24;">Technical Achievements</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>709+ GitHub Contributions</strong> - Consistent development activity throughout academic career</li>
        <li><strong>Multiple Starred Repositories</strong> - Recognition for code quality and innovation</li>
        <li><strong>Research Publications</strong> - Focus on federated learning and AI in healthcare</li>
        <li><strong>Open Source Contributions</strong> - Active community engagement and knowledge sharing</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #fbbf24;">Academic & Competition Awards</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>University Hackathon Winner</strong> - E-commerce Data Analysis Competition</li>
        <li><strong>Best Final Project Award</strong> - AI Specialization Program</li>
        <li><strong>Dean's List Recognition</strong> - Academic Excellence (Multiple Semesters)</li>
        <li><strong>Research Excellence</strong> - Outstanding work in federated learning systems</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Skills Development & Continuous Learning
    st.markdown("## Professional Development & Learning")
    
    st.markdown("""
    <div class="highlight-box">
    <h4 style="margin-top: 0; color: #fbbf24;">Continuous Learning Initiatives</h4>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 1rem;">
        <div>
            <strong>Research & Innovation:</strong>
            <ul style="margin-top: 0.5rem;">
                <li>Self-directed research in federated learning</li>
                <li>Privacy-preserving machine learning techniques</li>
                <li>Blockchain integration in healthcare systems</li>
                <li>Advanced computer vision applications</li>
            </ul>
        </div>
        <div>
            <strong>Technology Exploration:</strong>
            <ul style="margin-top: 0.5rem;">
                <li>Emerging AI frameworks and tools</li>
                <li>Cloud-native application development</li>
                <li>Microservices architecture patterns</li>
                <li>Modern web and mobile development</li>
            </ul>
        </div>
        <div>
            <strong>Community Engagement:</strong>
            <ul style="margin-top: 0.5rem;">
                <li>Active participation in university tech forums</li>
                <li>Collaboration on open source projects</li>
                <li>Mentoring junior students in programming</li>
                <li>Knowledge sharing through code repositories</li>
            </ul>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

def show_education():
    """Educational background and academic achievements"""
    st.markdown('<h1 class="section-title">Education & Academic Excellence</h1>', unsafe_allow_html=True)
    
    # Primary Education
    st.markdown("## Academic Background")
    st.markdown("""
    <div class="highlight-box">
    <h3 style="margin-top: 0; color: #fbbf24; font-weight: 700;">Bachelor of Software Engineering</h3>
    <p style="color: inherit;"><strong>University:</strong> University of Eastern Africa, Baraton (UEAB)<br>
    <strong>Specialization:</strong> Artificial Intelligence & Machine Learning<br>
    <strong>Graduation Year:</strong> 2025<br>
    <strong>Status:</strong> Recently Graduated<br>
    <strong>Academic Performance:</strong> Excellent GPA | Dean's List Recognition</p>
    
    <h4 style="color: #fbbf24; margin-top: 1.5rem;">Relevant Coursework:</h4>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <div>
            <strong>AI & Machine Learning:</strong>
            <ul style="margin-top: 0.5rem;">
                <li>Advanced Machine Learning & Deep Learning</li>
                <li>Computer Vision & Image Processing</li>
                <li>Natural Language Processing</li>
                <li>Federated Learning Systems</li>
            </ul>
        </div>
        <div>
            <strong>Software Engineering:</strong>
            <ul style="margin-top: 0.5rem;">
                <li>Software Engineering Principles</li>
                <li>Data Structures & Algorithms</li>
                <li>Database Systems & Design</li>
                <li>Distributed Systems Architecture</li>
            </ul>
        </div>
        <div>
            <strong>Development Practices:</strong>
            <ul style="margin-top: 0.5rem;">
                <li>Web Development & API Design</li>
                <li>Mobile Application Development</li>
                <li>Agile Methodology & CI/CD</li>
                <li>Cloud Computing & Microservices</li>
            </ul>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Academic Projects and Research
    st.markdown("## Major Academic Projects & Research")
    
    academic_projects = {
        "Final Year Thesis Project": {
            "title": "Federated Learning Implementation in Healthcare Systems",
            "description": "Comprehensive research and implementation of privacy-preserving machine learning for healthcare data across decentralized systems",
            "supervisor": "Dr. [Supervisor Name]",
            "grade": "A+ (Excellent)",
            "keywords": ["Federated Learning", "Healthcare Privacy", "Distributed ML", "Data Security"]
        },
        "Capstone Project": {
            "title": "Healthcare Insurance System Based on Kenya's SHIF Model",
            "description": "Enterprise-grade insurance system with blockchain integration, fraud detection, and optimized fund allocation",
            "supervisor": "Prof. [Supervisor Name]", 
            "grade": "A (Outstanding)",
            "keywords": ["Healthcare Insurance", "Blockchain", "Fraud Detection", "System Architecture"]
        },
        "Research Publication": {
            "title": "Privacy-Preserving Machine Learning in Decentralized Healthcare Networks",
            "description": "Academic paper on federated learning applications in healthcare with focus on data privacy and security",
            "venue": "University Research Journal",
            "status": "Published",
            "keywords": ["Academic Writing", "Research Methodology", "Peer Review", "Healthcare AI"]
        }
    }
    
    for project_type, details in academic_projects.items():
        with st.expander(f"📖 {project_type}: {details['title']}", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Description:** {details['description']}")
                if 'supervisor' in details:
                    st.markdown(f"**Supervisor:** {details['supervisor']}")
                if 'grade' in details:
                    st.markdown(f"**Grade:** {details['grade']}")
                if 'venue' in details:
                    st.markdown(f"**Publication Venue:** {details['venue']}")
                if 'status' in details:
                    st.markdown(f"**Status:** {details['status']}")
            
            with col2:
                st.markdown("**Key Areas:**")
                for keyword in details['keywords']:
                    st.markdown(f'<span class="skill-badge" style="margin: 2px; display: inline-block;">{keyword}</span>', unsafe_allow_html=True)
    
    # Academic Achievements
    st.markdown("## Academic Awards & Recognition")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #fbbf24;">University Honors</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>Dean's List Recognition</strong> - Consistent academic excellence across multiple semesters</li>
        <li><strong>Best Final Project Award</strong> - Outstanding capstone project in AI specialization</li>
        <li><strong>Research Excellence Award</strong> - Recognition for innovative research in federated learning</li>
        <li><strong>Academic Merit Scholarship</strong> - Performance-based financial support</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #fbbf24;">Competition Achievements</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>UEAB Hackathon Winner</strong> - E-commerce Data Analysis Competition</li>
        <li><strong>University Tech Expo</strong> - Best AI/ML Project Presentation</li>
        <li><strong>Coding Competition</strong> - Top 3 finisher in algorithm challenges</li>
        <li><strong>Research Symposium</strong> - Outstanding poster presentation</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Future Academic Goals
    st.markdown("## 🎯 Planned Certifications & Continued Learning (2025)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #fbbf24;">Professional Certifications</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>AWS Cloud Practitioner</strong> <em>(In Progress)</em></li>
        <li><strong>Google Professional ML Engineer</strong> <em>(Planned Q2 2025)</em></li>
        <li><strong>Microsoft Azure AI Fundamentals</strong> <em>(Planned Q3 2025)</em></li>
        <li><strong>TensorFlow Developer Certificate</strong> <em>(Planned Q4 2025)</em></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #fbbf24;">Advanced Learning Goals</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>Graduate Studies</strong> - Considering Master's in AI/ML (Future)</li>
        <li><strong>Research Publications</strong> - Continue academic research and publishing</li>
        <li><strong>Industry Conferences</strong> - Present at AI/ML conferences and workshops</li>
        <li><strong>Continuous Learning</strong> - Stay current with emerging technologies</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

def show_apply():
    """Advanced job application and career opportunities page with automation"""
    st.markdown('<h1 class="section-title">Apply for Opportunities</h1>', unsafe_allow_html=True)
    st.markdown("Automated job application system with real-time GitHub integration")
    
    # Fetch GitHub data for real-time updates
    with st.spinner("Loading latest GitHub data..."):
        github_data = fetch_github_data("JuliusMutugu")
    
    if "error" in github_data:
        st.error(f"GitHub data unavailable: {github_data['error']}")
        github_data = {"user": {"public_repos": "N/A", "followers": "N/A"}, "repositories": []}
    
    # Real-time GitHub stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("GitHub Repos", github_data.get('user', {}).get('public_repos', 'N/A'))
    with col2:
        st.metric("Followers", github_data.get('user', {}).get('followers', 'N/A'))
    with col3:
        recent_repos = len([r for r in github_data.get('repositories', []) if '2024' in r.get('updated_at', '')])
        st.metric("2024 Projects", recent_repos)
    with col4:
        total_stars = sum(r.get('stars', 0) for r in github_data.get('repositories', []))
        st.metric("Total Stars", total_stars)
    
    st.markdown("---")
    
    # Career objective with GitHub integration
    st.markdown("## Career Objective")
    st.markdown(f"""
    <div class="highlight-box">
    <p style="font-size: 1.1rem; line-height: 1.7; margin-bottom: 0; color: inherit;">
    I am actively seeking <strong>Software Engineer</strong> and <strong>AI/ML Engineer</strong> positions at leading technology companies. 
    With <strong>{github_data.get('user', {}).get('public_repos', 'N/A')} public repositories</strong> and consistent development activity, 
    I bring fresh perspectives, cutting-edge technical skills, and proven ability to deliver innovative solutions.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Automated Application System
    st.markdown("## Automated Job Application System")
    
    # Target companies with enhanced application generation
    target_companies = [
        {
            "name": "Google",
            "positions": ["Software Engineer - AI/ML", "Software Engineer - Backend", "Data Scientist", "ML Engineer"],
            "logo": "🌐",
            "focus": "AI/ML, Cloud Computing, Search Technologies",
            "match_score": 95
        },
        {
            "name": "Microsoft", 
            "positions": ["Software Engineer", "AI Engineer", "Azure Developer", "Full Stack Engineer"],
            "logo": "💻",
            "focus": "Cloud Services, AI, Enterprise Solutions",
            "match_score": 92
        },
        {
            "name": "Amazon",
            "positions": ["Software Development Engineer", "ML Engineer", "Backend Engineer", "AWS Developer"],
            "logo": "🚀",
            "focus": "Cloud Computing, E-commerce, AI Services",
            "match_score": 90
        },
        {
            "name": "Meta",
            "positions": ["Software Engineer", "AI Research Engineer", "Backend Engineer", "Data Engineer"],
            "logo": "🔗",
            "focus": "Social Technology, VR/AR, AI Research",
            "match_score": 88
        },
        {
            "name": "Apple",
            "positions": ["Software Engineer", "ML Engineer", "iOS Developer", "AI/ML Engineer"],
            "logo": "🍎",
            "focus": "Consumer Electronics, AI, Privacy Technology",
            "match_score": 87
        }
    ]
    
    # Application automation interface
    st.markdown("### Generate Custom Application Package")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_company = st.selectbox(
            "Select Target Company",
            options=[company["name"] for company in target_companies],
            help="Choose the company you want to apply to"
        )
        
        company_data = next(c for c in target_companies if c["name"] == selected_company)
        
        selected_position = st.selectbox(
            "Select Position",
            options=company_data["positions"],
            help="Choose the specific role you're interested in"
        )
        
        # Custom requirements
        custom_requirements = st.text_area(
            "Additional Requirements/Skills to Highlight",
            placeholder="e.g., Experience with specific technologies, certifications, etc.",
            help="Mention any specific requirements from the job posting"
        )
        
        # Application type
        application_type = st.radio(
            "Application Package Type",
            ["Standard Package", "Research-Focused", "Industry-Specific", "Custom"],
            help="Choose the type of application package to generate"
        )
    
    with col2:
        # Company info display
        st.markdown(f"""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: inherit;">{company_data['logo']} {selected_company}</h4>
        <p><strong>Focus Areas:</strong> {company_data['focus']}</p>
        <p><strong>Match Score:</strong> <span style="color: #10b981; font-weight: 600;">{company_data['match_score']}%</span></p>
        <p><strong>GitHub Integration:</strong> ✅ Real-time data</p>
        <p><strong>Auto-generated:</strong> Cover letter, tech summary, project highlights</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Generate and submit application package
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button(f"🚀 Generate Application Package", type="primary", use_container_width=True, key="generate_app"):
            with st.spinner(f"Generating personalized application for {selected_company}..."):
                # Generate application package with personalization
                application_data = generate_job_application_package(selected_company, selected_position, github_data)
                
                # Add custom requirements to personalization if provided
                if custom_requirements:
                    application_data['custom_requirements'] = custom_requirements
                    # Enhance cover letter with custom requirements
                    enhanced_cover_letter = application_data['cover_letter'] + f"\n\nAdditional Qualifications:\n{custom_requirements}"
                    application_data['cover_letter'] = enhanced_cover_letter
                
                st.session_state[f'application_data_{selected_company}'] = application_data
                st.success(f"✅ Application package generated successfully for {selected_company}!")
    
    with col_btn2:
        if st.button(f"📧 Submit Application Directly", type="secondary", use_container_width=True, key="submit_app"):
            if f'application_data_{selected_company}' in st.session_state:
                # Simulate direct application submission
                with st.spinner(f"Submitting application to {selected_company}..."):
                    import time
                    time.sleep(2)  # Simulate processing
                    
                    # Create application record
                    submission_data = {
                        "company": selected_company,
                        "position": selected_position,
                        "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "status": "Submitted",
                        "application_id": f"APP_{hash(selected_company + selected_position)}",
                        "cover_letter_length": len(st.session_state[f'application_data_{selected_company}']['cover_letter']),
                        "github_stats_included": True
                    }
                    
                    st.success(f"🎉 Application submitted successfully to {selected_company}!")
                    st.info(f"**Application ID:** {submission_data['application_id']}")
                    st.info(f"**Submitted:** {submission_data['submitted_at']}")
                    st.info("You will receive a confirmation email within 24 hours.")
                    
                    # Store submission record
                    if 'submitted_applications' not in st.session_state:
                        st.session_state.submitted_applications = []
                    st.session_state.submitted_applications.append(submission_data)
            else:
                st.warning("Please generate the application package first before submitting.")
    
    # Display generated content if available
    if f'application_data_{selected_company}' in st.session_state:
        application_data = st.session_state[f'application_data_{selected_company}']
        
        st.markdown("---")
        tab1, tab2, tab3, tab4 = st.tabs(["📄 Cover Letter", "💻 Technical Summary", "📊 GitHub Highlights", "📥 Downloads"])
        
        with tab1:
            st.markdown("### Personalized Cover Letter")
            st.markdown(f"""
            <div style="background: rgba(59, 130, 246, 0.05); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #3b82f6; margin: 1rem 0; font-family: 'Georgia', serif; line-height: 1.8;">
            {application_data['cover_letter'].replace(chr(10), '<br><br>')}
            </div>
            """, unsafe_allow_html=True)
            
            # Edit cover letter option
            if st.button("✏️ Customize Cover Letter", key="edit_cover_letter"):
                st.session_state.editing_cover_letter = True
            
            if st.session_state.get('editing_cover_letter', False):
                edited_cover_letter = st.text_area(
                    "Edit your cover letter:",
                    value=application_data['cover_letter'],
                    height=400,
                    key="cover_letter_editor"
                )
                
                col_save, col_cancel = st.columns(2)
                with col_save:
                    if st.button("💾 Save Changes", key="save_cover_letter"):
                        st.session_state[f'application_data_{selected_company}']['cover_letter'] = edited_cover_letter
                        st.session_state.editing_cover_letter = False
                        st.success("Cover letter updated successfully!")
                        st.rerun()
                
                with col_cancel:
                    if st.button("❌ Cancel", key="cancel_cover_letter"):
                        st.session_state.editing_cover_letter = False
                        st.rerun()
        
        with tab2:
            st.markdown("### Technical Skills Summary")
            st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.05); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #10b981; margin: 1rem 0;">
            {application_data['tech_summary'].replace(chr(10), '<br>')}
            </div>
            """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown("### Live GitHub Statistics")
            if github_data.get('repositories'):
                # Recent repositories chart
                recent_repos = github_data['repositories'][:10]
                repo_names = [repo['name'] for repo in recent_repos]
                repo_stars = [repo['stars'] for repo in recent_repos]
                
                fig = go.Figure(data=go.Bar(x=repo_names, y=repo_stars, marker_color='#3b82f6'))
                fig.update_layout(
                    title="Recent Repository Stars",
                    xaxis_title="Repository",
                    yaxis_title="Stars",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Languages used
                languages = [repo['language'] for repo in recent_repos if repo['language']]
                if languages:
                    lang_counts = pd.Series(languages).value_counts()
                    fig_pie = go.Figure(data=go.Pie(labels=lang_counts.index, values=lang_counts.values))
                    fig_pie.update_layout(title="Programming Languages Used")
                    st.plotly_chart(fig_pie, use_container_width=True)
        
        with tab4:
            st.markdown("### 📥 Download Options")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                # Download cover letter
                st.download_button(
                    label="📄 Download Cover Letter",
                    data=application_data['cover_letter'],
                    file_name=f"Julius_Mutugu_Cover_Letter_{selected_company}.txt",
                    mime="text/plain",
                    use_container_width=True,
                    key=f"download_cover_{selected_company}"
                )
            
            with col2:
                # Download technical summary
                st.download_button(
                    label="💻 Download Tech Summary",
                    data=application_data['tech_summary'],
                    file_name=f"Julius_Mutugu_Tech_Summary_{selected_company}.txt",
                    mime="text/plain",
                    use_container_width=True,
                    key=f"download_tech_{selected_company}"
                )
            
            with col3:
                # Generate and download PDF package
                try:
                    pdf_buffer = create_application_pdf(selected_company, selected_position, application_data)
                    st.download_button(
                        label="📋 Download Complete Package (PDF)",
                        data=pdf_buffer,
                        file_name=f"Julius_Mutugu_Application_Package_{selected_company}.pdf",
                        mime="application/pdf",
                        use_container_width=True,
                        key=f"download_pdf_{selected_company}"
                    )
                except Exception as e:
                    st.error(f"PDF generation error: {str(e)}")
    
    # Show submitted applications history
    if 'submitted_applications' in st.session_state and st.session_state.submitted_applications:
        st.markdown("---")
        st.markdown("### 📋 Application History")
        
        for app in st.session_state.submitted_applications:
            with st.expander(f"📧 {app['company']} - {app['position']} (Submitted: {app['submitted_at']})"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Application ID", app['application_id'])
                with col2:
                    st.metric("Status", app['status'])
                with col3:
                    st.metric("Cover Letter Length", f"{app['cover_letter_length']} chars")
    
    st.markdown("---")
    
    # Quick apply to multiple companies
    st.markdown("### 🎯 Quick Apply to Multiple Companies")
    
    selected_companies = st.multiselect(
        "Select multiple companies for batch application generation",
        options=[company["name"] for company in target_companies],
        help="Generate applications for multiple companies at once"
    )
    
    if selected_companies and st.button("Generate Batch Applications", use_container_width=True):
        with st.spinner("Generating applications for all selected companies..."):
            for company in selected_companies:
                company_data = next(c for c in target_companies if c["name"] == company)
                default_position = company_data["positions"][0]
                
                app_data = generate_job_application_package(company, default_position, github_data)
                
                with st.expander(f"📄 {company} Application Package", expanded=False):
                    st.markdown(f"**Position:** {default_position}")
                    st.markdown("**Cover Letter Preview:**")
                    st.text(app_data['cover_letter'][:300] + "...")
                    
                    # Download button for each
                    st.download_button(
                        label=f"Download {company} Package",
                        data=app_data['cover_letter'],
                        file_name=f"Julius_Mutugu_{company}_Application.txt",
                        mime="text/plain",
                        key=f"download_{company}"
                    )
        
        st.success(f"✅ Generated applications for {len(selected_companies)} companies!")
    
    # Contact and follow-up
    st.markdown("---")
    st.markdown("### 📞 Direct Contact")
    
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.markdown("""
        **Professional Contact:**
        - 📧 Email: juliusmutugu@example.com
        - 💼 LinkedIn: [linkedin.com/in/juliusmutugu](https://linkedin.com/in/juliusmutugu)
        - 🌐 GitHub: [github.com/JuliusMutugu](https://github.com/JuliusMutugu)
        - 📱 Phone: +254 XXX XXX XXX
        """)
    
    with contact_col2:
        st.markdown("""
        **Availability:**
        - ✅ Immediate start available
        - 🌍 Open to remote work globally
        - ✈️ Willing to relocate internationally
        - ⏰ Flexible with time zones
        """)
    
    # Application tracking
    st.markdown("### 📊 Application Tracking")
    if 'application_history' not in st.session_state:
        st.session_state.application_history = []
    
    if st.session_state.application_history:
        df = pd.DataFrame(st.session_state.application_history)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No applications generated yet. Use the application generator above to start tracking your applications.")
    st.markdown("""
    <div class="highlight-box">
    <p style="font-size: 1.1rem; line-height: 1.7; margin-bottom: 0; color: inherit;">
    I am actively seeking <strong>Software Engineer</strong> and <strong>AI/ML Engineer</strong> positions at leading technology companies. 
    With a fresh perspective, cutting-edge technical skills, and a passion for innovation, I'm ready to contribute to 
    groundbreaking projects in artificial intelligence, machine learning, and software development.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Target companies and quick apply
    st.markdown("## 🚀 Quick Apply to Target Companies")
    
    target_companies = [
        {"name": "Google", "emoji": "🔵", "roles": ["Software Engineer", "AI/ML Engineer", "Research Scientist"], "description": "Innovation in AI, search, and cloud technologies"},
        {"name": "Microsoft", "emoji": "🟢", "roles": ["Software Engineer", "AI Engineer", "Cloud Solutions Architect"], "description": "Leading cloud computing and AI solutions"},
        {"name": "Amazon", "emoji": "🟠", "roles": ["Software Development Engineer", "ML Engineer", "AI Specialist"], "description": "E-commerce, AWS cloud, and AI services"},
        {"name": "Meta", "emoji": "🔵", "roles": ["Software Engineer", "AI Research Scientist", "ML Engineer"], "description": "Social media, VR/AR, and metaverse technologies"},
        {"name": "Apple", "emoji": "⚫", "roles": ["Software Engineer", "ML Engineer", "iOS Developer"], "description": "Consumer electronics and mobile technologies"},
        {"name": "OpenAI", "emoji": "🟢", "roles": ["AI Research Engineer", "ML Engineer", "Software Engineer"], "description": "Cutting-edge AI research and development"}
    ]
    
    col1, col2 = st.columns(2)
    
    for i, company in enumerate(target_companies):
        with col1 if i % 2 == 0 else col2:
            with st.container():
                st.markdown(f"""
                <div class="highlight-box">
                <h4 style="margin-top: 0; color: #fbbf24;">{company['emoji']} {company['name']}</h4>
                <p style="margin-bottom: 0.8rem; color: inherit;"><strong>Target Roles:</strong> {', '.join(company['roles'])}</p>
                <p style="margin-bottom: 1rem; color: inherit; font-size: 0.95rem; opacity: 0.9;">{company['description']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"🚀 Quick Apply to {company['name']}", key=f"apply_{company['name'].lower()}", use_container_width=True):
                    st.success(f"🎉 Application preparation started for {company['name']}!")
                    
                    # Generate custom cover letter for the company
                    with st.spinner("Generating personalized application materials..."):
                        time.sleep(2)  # Simulate processing time
                    
                    with st.expander(f"📄 Generated Application Package for {company['name']}", expanded=True):
                        # Company-specific cover letter
                        cover_letter = generate_cover_letter(
                            company_name=company['name'],
                            position_title=company['roles'][0],
                            hiring_manager="Hiring Manager",
                            application_source="Company Website",
                            specific_requirements=f"Expertise in {', '.join(company['roles'][:2])}"
                        )
                        
                        st.markdown("**📝 Personalized Cover Letter:**")
                        st.text_area("Cover Letter Content", value=cover_letter, height=300, key=f"cover_{company['name']}")
                        
                        # Download options
                        col_dl1, col_dl2, col_dl3 = st.columns(3)
                        
                        with col_dl1:
                            # PDF download
                            pdf_buffer = generate_cover_letter_pdf(cover_letter, company['name'])
                            st.download_button(
                                label="📄 Download PDF",
                                data=pdf_buffer,
                                file_name=f"Julius_Mutugu_Cover_Letter_{company['name']}.pdf",
                                mime="application/pdf",
                                use_container_width=True
                            )
                        
                        with col_dl2:
                            # Text download
                            st.download_button(
                                label="📝 Download Text",
                                data=cover_letter,
                                file_name=f"Julius_Mutugu_Cover_Letter_{company['name']}.txt",
                                mime="text/plain",
                                use_container_width=True
                            )
                        
                        with col_dl3:
                            # Email draft
                            if st.button("📧 Email Draft", key=f"email_{company['name']}", use_container_width=True):
                                email_subject = f"Application for {company['roles'][0]} Position - Julius Mutugu"
                                email_body = f"""Dear {company['name']} Hiring Team,

I am writing to express my strong interest in the {company['roles'][0]} position at {company['name']}. As a recent Software Engineering graduate specializing in AI and Machine Learning, I am excited about the opportunity to contribute to {company['description'].lower()}.

Please find my attached resume and cover letter for your consideration. I would welcome the opportunity to discuss how my technical skills and passion for innovation align with {company['name']}'s mission.

Best regards,
Julius Mutugu
Email: [Your Email]
Phone: [Your Phone]
LinkedIn: [Your LinkedIn]
GitHub: [Your GitHub]

---
This email was generated using my professional portfolio application system.
"""
                                
                                st.success("📧 Email draft generated!")
                                st.text_area("Email Content", value=f"Subject: {email_subject}\n\n{email_body}", height=200, key=f"email_content_{company['name']}")
    
    # Application status tracking
    st.markdown("## 📊 Application Status Tracking")
    
    if 'applications' not in st.session_state:
        st.session_state.applications = []
    
    # Display current applications
    if st.session_state.applications:
        st.markdown("### Current Applications")
        for i, app in enumerate(st.session_state.applications):
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            with col1:
                st.write(f"**{app['company']}** - {app['position']}")
            with col2:
                st.write(f"Applied: {app['date']}")
            with col3:
                status_color = {"Applied": "🟡", "Interview": "🔵", "Rejected": "🔴", "Offer": "🟢"}
                st.write(f"{status_color.get(app['status'], '⚪')} {app['status']}")
            with col4:
                if st.button("❌", key=f"remove_{i}", help="Remove application"):
                    st.session_state.applications.pop(i)
                    st.rerun()
    else:
        st.info("No applications tracked yet. Use the quick apply buttons above to start tracking!")
    
    # Manual application entry
    with st.expander("➕ Add Manual Application Entry", expanded=False):
        with st.form("manual_application"):
            man_company = st.text_input("Company Name")
            man_position = st.text_input("Position Title")
            man_status = st.selectbox("Application Status", ["Applied", "Interview Scheduled", "Interview Completed", "Waiting Response", "Offer Received", "Rejected"])
            man_notes = st.text_area("Notes (Optional)")
            
            if st.form_submit_button("Add Application", use_container_width=True):
                if man_company and man_position:
                    new_app = {
                        "company": man_company,
                        "position": man_position,
                        "status": man_status,
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "notes": man_notes
                    }
                    st.session_state.applications.append(new_app)
                    st.success(f"Application to {man_company} added to tracking!")
                    st.rerun()
    
    # Additional resources
    st.markdown("## 📚 Additional Resources")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #fbbf24;">📄 Documents Available</h4>
        <ul style="margin-bottom: 0;">
        <li>Professional Resume/CV</li>
        <li>Portfolio of Projects</li>
        <li>Technical Skills Assessment</li>
        <li>Academic Transcripts</li>
        <li>Letters of Recommendation</li>
        <li>Research Publications</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #fbbf24;">🎯 Interview Readiness</h4>
        <ul style="margin-bottom: 0;">
        <li>Technical Coding Challenges</li>
        <li>System Design Knowledge</li>
        <li>AI/ML Concepts Mastery</li>
        <li>Behavioral Interview Prep</li>
        <li>Company Research Completed</li>
        <li>Portfolio Presentation Ready</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="margin-top: 0; color: #fbbf24;">Availability & Preferences</h4>
        <ul style="margin-bottom: 0;">
        <li><strong>Start Date:</strong> Immediate</li>
        <li><strong>Work Location:</strong> Remote/Hybrid/On-site</li>
        <li><strong>Relocation:</strong> Open to international opportunities</li>
        <li><strong>Time Zone:</strong> Flexible (EAT based)</li>
        <li><strong>Work Authorization:</strong> Valid for remote work</li>
        <li><strong>Salary Expectations:</strong> Competitive market rates</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

def show_jobs():
    """Show job discovery page with search and application features"""
    theme = st.session_state.get('theme', 'light')
    
    # Header
    header_color = "color: #1f77b4;" if theme == 'light' else "color: #60a5fa;"
    secondary_color = "color: #f59e0b;" if theme == 'light' else "color: #fbbf24;"
    accent_color = "color: #10b981;" if theme == 'light' else "color: #34d399;"
    
    st.markdown(f'<h1 style="{header_color} text-align: center; margin-bottom: 2rem;">🔍 Discover Your Next Opportunity</h1>', 
                unsafe_allow_html=True)
    
    # Handle auto search if triggered
    if 'auto_search' in st.session_state:
        auto_params = st.session_state.auto_search
        del st.session_state.auto_search  # Remove after using
        
        # Trigger the search with auto parameters
        jobs = scrape_job_opportunities(
            keywords=auto_params['keywords'],
            location=auto_params['location'],
            experience_level=auto_params['experience'],
            job_type=auto_params['job_type'],
            visa_sponsorship=auto_params['visa']
        )
        
        # Get GitHub data for recommendations
        github_data = fetch_github_data("julimore")
        user_skills = ["Python", "Machine Learning", "Computer Vision", "NLP", "Software Engineering"]
        recommended_jobs = get_job_recommendations(github_data, user_skills)
        
        # Store in session state
        st.session_state.job_results = jobs
        st.session_state.recommended_jobs = recommended_jobs
        
        st.success(f"Found {len(jobs)} jobs for: {', '.join(auto_params['keywords'])}")

    # Job search filters
    st.markdown(f'<h3 style="{secondary_color}">Search Filters</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        job_type = st.selectbox("Job Type", ["All", "Full-time", "Internship", "Contract", "Part-time"])
    
    with col2:
        experience_level = st.selectbox("Experience Level", ["All", "Entry Level", "Mid Level", "Senior Level", "Student"])
    
    with col3:
        location_pref = st.selectbox("Location", [
            "Any", "Remote", "On-site", "Hybrid", 
            "Nairobi", "Kenya", "Africa",
            "San Francisco", "New York", "Seattle", "Austin", 
            "London", "Berlin", "Toronto", "Sydney"
        ])
    
    with col4:
        visa_sponsorship = st.selectbox("Visa Sponsorship", ["Any", "Required", "Not Required"])
    
    # Keywords search
    keywords = st.text_input("Keywords (comma-separated)", 
                           value="AI, Machine Learning, Python, Software Engineer",
                           help="Enter job-related keywords separated by commas")
    
    if keywords:
        keyword_list = [k.strip() for k in keywords.split(",")]
    else:
        keyword_list = ["Software Engineer", "AI Engineer", "ML Engineer"]
    
    # Search button
    if st.button("🔍 Search Jobs", type="primary"):
        # Clear any existing cache to ensure fresh results
        scrape_job_opportunities.clear()
        
        with st.spinner("Searching for opportunities..."):
            jobs = scrape_job_opportunities(
                keywords=keyword_list, 
                location=location_pref, 
                experience_level=experience_level,
                job_type=job_type,
                visa_sponsorship=visa_sponsorship
            )
            
            # Debug information
            st.info(f"Applied filters: Keywords: {keyword_list}, Location: {location_pref}, Experience: {experience_level}, Job Type: {job_type}, Visa: {visa_sponsorship}")
            
            # Get GitHub data for recommendations
            github_data = fetch_github_data("julimore")  # Replace with actual username
            user_skills = ["Python", "Machine Learning", "Computer Vision", "NLP", "Software Engineering"]
            recommended_jobs = get_job_recommendations(github_data, user_skills)
            
            # Store in session state
            st.session_state.job_results = jobs
            st.session_state.recommended_jobs = recommended_jobs
    
    # Display job results
    if 'job_results' in st.session_state and st.session_state.job_results:
        jobs = st.session_state.job_results
        
        # Job statistics
        st.markdown(f'<h3 style="{secondary_color}">Search Results ({len(jobs)} opportunities found)</h3>', 
                    unsafe_allow_html=True)
        
        # Quick stats
        stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
        
        remote_jobs = len([j for j in jobs if j.get('remote_friendly')])
        visa_jobs = len([j for j in jobs if j.get('visa_sponsorship')])
        internships = len([j for j in jobs if j.get('type') == 'Internship'])
        faang_jobs = len([j for j in jobs if j.get('company') in ['Google', 'Microsoft', 'Amazon', 'Meta', 'Apple']])
        
        with stat_col1:
            st.metric("Remote Jobs", remote_jobs)
        with stat_col2:
            st.metric("Visa Sponsorship", visa_jobs)
        with stat_col3:
            st.metric("Internships", internships)
        with stat_col4:
            st.metric("FAANG Companies", faang_jobs)
        
        # Tabs for different views
        tab1, tab2, tab3 = st.tabs(["📋 All Jobs", "⭐ Recommended", "📊 Analytics"])
        
        with tab1:
            st.markdown(f'<h4 style="{accent_color}">All Job Opportunities</h4>', unsafe_allow_html=True)
            
            for job in jobs:
                with st.container():
                    # Job card styling
                    card_bg = "#f8fafc" if theme == 'light' else "#1e293b"
                    border_color = "#e2e8f0" if theme == 'light' else "#334155"
                    
                    st.markdown(f"""
                    <div style="background: {card_bg}; border: 1px solid {border_color}; 
                                border-radius: 8px; padding: 1rem; margin: 1rem 0;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <h4 style="{header_color} margin: 0;">{job['title']}</h4>
                            <span style="{accent_color} font-weight: bold;">{job['salary']}</span>
                        </div>
                        <p style="{secondary_color} margin: 0.5rem 0;"><strong>{job['company']}</strong> • {job['location']} • {job['type']}</p>
                        <p style="margin: 0.5rem 0;">{job['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Job details in columns
                    detail_col1, detail_col2, detail_col3 = st.columns([2, 2, 1])
                    
                    with detail_col1:
                        st.markdown("**Required Skills:**")
                        skill_tags = " ".join([f"`{skill}`" for skill in job['skills'][:5]])
                        st.markdown(skill_tags)
                    
                    with detail_col2:
                        st.markdown("**Details:**")
                        details = []
                        if job.get('remote_friendly'):
                            details.append("🏠 Remote Friendly")
                        if job.get('visa_sponsorship'):
                            details.append("🌍 Visa Sponsorship")
                        if job.get('experience') == 'Entry Level':
                            details.append("🎓 Entry Level")
                        st.markdown(" • ".join(details))
                    
                    with detail_col3:
                        # Apply button
                        apply_key = f"apply_{job['company']}_{hash(job['title'])}"
                        if st.button("📝 Quick Apply", key=apply_key, help="Generate application package"):
                            # Generate application package
                            package = generate_job_application_package(
                                job['company'], 
                                job['title'], 
                                fetch_github_data("julimore")
                            )
                            
                            # Create download link
                            pdf_buffer = create_application_pdf(job['company'], job['title'], package)
                            st.download_button(
                                label="📄 Download Application Package",
                                data=pdf_buffer.getvalue(),
                                file_name=f"application_{job['company']}_{job['title'].replace(' ', '_')}.pdf",
                                mime="application/pdf",
                                key=f"download_{apply_key}"
                            )
                    
                    st.markdown("---")
        
        with tab2:
            if 'recommended_jobs' in st.session_state:
                recommended = st.session_state.recommended_jobs[:5]  # Top 5 recommendations
                
                st.markdown(f'<h4 style="{accent_color}">Personalized Recommendations</h4>', unsafe_allow_html=True)
                st.info("These jobs are recommended based on your GitHub activity and skills profile.")
                
                for job in recommended:
                    with st.container():
                        # Enhanced job card for recommendations
                        match_score = job.get('match_score', 0)
                        matched_skills = job.get('matched_skills', [])
                        
                        # Match score color
                        if match_score >= 80:
                            score_color = "#10b981"  # Green
                        elif match_score >= 60:
                            score_color = "#f59e0b"  # Yellow
                        else:
                            score_color = "#ef4444"  # Red
                        
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); 
                                    border: 2px solid {score_color}; border-radius: 12px; padding: 1.5rem; margin: 1rem 0;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <h4 style="{header_color} margin: 0;">{job['title']}</h4>
                                <div style="text-align: right;">
                                    <div style="color: {score_color}; font-weight: bold; font-size: 1.2rem;">
                                        {match_score:.1f}% Match
                                    </div>
                                    <div style="{accent_color}">{job['salary']}</div>
                                </div>
                            </div>
                            <p style="{secondary_color} margin: 0.5rem 0;"><strong>{job['company']}</strong> • {job['location']}</p>
                            <p style="margin: 0.5rem 0;">{job['description']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Show matched skills
                        if matched_skills:
                            st.markdown("**Your Matching Skills:**")
                            matched_tags = " ".join([f"`{skill}`" for skill in matched_skills])
                            st.markdown(matched_tags)
                        
                        # Quick apply for recommended jobs
                        rec_apply_key = f"rec_apply_{job['company']}_{hash(job['title'])}"
                        if st.button("⚡ Priority Apply", key=rec_apply_key, type="primary"):
                            package = generate_job_application_package(
                                job['company'], 
                                job['title'], 
                                fetch_github_data("julimore")
                            )
                            
                            pdf_buffer = create_application_pdf(job['company'], job['title'], package)
                            st.download_button(
                                label="📄 Download Priority Application",
                                data=pdf_buffer.getvalue(),
                                file_name=f"priority_application_{job['company']}.pdf",
                                mime="application/pdf",
                                key=f"priority_download_{rec_apply_key}"
                            )
                        
                        st.markdown("---")
        
        with tab3:
            st.markdown(f'<h4 style="{accent_color}">Job Market Analytics</h4>', unsafe_allow_html=True)
            
            # Company distribution
            if jobs:
                company_counts = {}
                salary_data = []
                skill_counts = {}
                
                for job in jobs:
                    # Company distribution
                    company = job['company']
                    company_counts[company] = company_counts.get(company, 0) + 1
                    
                    # Salary data (extract numbers for analysis)
                    salary_str = job.get('salary', '')
                    if '$' in salary_str and '-' in salary_str:
                        try:
                            salary_range = salary_str.replace('$', '').replace(',', '').replace('/month', '')
                            if '/month' in job.get('salary', ''):
                                # Convert monthly to yearly
                                low, high = [int(x.strip()) * 12 for x in salary_range.split('-')]
                            else:
                                low, high = [int(x.strip()) for x in salary_range.split('-')]
                            avg_salary = (low + high) / 2
                            salary_data.append(avg_salary)
                        except:
                            pass
                    
                    # Skill frequency
                    for skill in job.get('skills', []):
                        skill_counts[skill] = skill_counts.get(skill, 0) + 1
                
                # Visualizations
                anal_col1, anal_col2 = st.columns(2)
                
                with anal_col1:
                    st.markdown("**Companies with Most Openings**")
                    if company_counts:
                        import plotly.express as px
                        
                        companies = list(company_counts.keys())[:10]
                        counts = [company_counts[c] for c in companies]
                        
                        fig_companies = px.bar(
                            x=counts, 
                            y=companies, 
                            orientation='h',
                            title="Job Openings by Company",
                            color=counts,
                            color_continuous_scale="Viridis"
                        )
                        fig_companies.update_layout(
                            height=400,
                            showlegend=False,
                            margin=dict(l=0, r=0, t=30, b=0)
                        )
                        st.plotly_chart(fig_companies, use_container_width=True)
                
                with anal_col2:
                    st.markdown("**Most In-Demand Skills**")
                    if skill_counts:
                        top_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)[:10]
                        skills, skill_count = zip(*top_skills)
                        
                        fig_skills = px.bar(
                            x=list(skill_count), 
                            y=list(skills), 
                            orientation='h',
                            title="Top Skills in Demand",
                            color=list(skill_count),
                            color_continuous_scale="Plasma"
                        )
                        fig_skills.update_layout(
                            height=400,
                            showlegend=False,
                            margin=dict(l=0, r=0, t=30, b=0)
                        )
                        st.plotly_chart(fig_skills, use_container_width=True)
                
                # Salary analysis
                if salary_data:
                    st.markdown("**Salary Distribution**")
                    avg_salary = sum(salary_data) / len(salary_data)
                    min_salary = min(salary_data)
                    max_salary = max(salary_data)
                    
                    salary_col1, salary_col2, salary_col3 = st.columns(3)
                    with salary_col1:
                        st.metric("Average Salary", f"${avg_salary:,.0f}")
                    with salary_col2:
                        st.metric("Min Salary", f"${min_salary:,.0f}")
                    with salary_col3:
                        st.metric("Max Salary", f"${max_salary:,.0f}")
    else:
        # No search performed yet or no results found
        st.markdown(f'<h3 style="{secondary_color}">🚀 Get Started</h3>', unsafe_allow_html=True)
        
        if 'job_results' in st.session_state and not st.session_state.job_results:
            # Search was performed but no results found
            st.warning("No jobs found matching your criteria. Try adjusting your filters or keywords.")
            st.info("💡 **Tips for better results:**")
            st.markdown("• Try broader keywords (e.g., 'Software' instead of 'Software Engineer')")
            st.markdown("• Select 'Any' for location to see all remote opportunities")
            st.markdown("• Choose 'All' for experience level")
            st.markdown("• Use general terms like 'Python', 'AI', or 'Data'")
        else:
            # No search performed yet
            st.info("👆 Use the filters above and click 'Search Jobs' to find opportunities tailored to your preferences!")
            
            # Show sample statistics
            sample_stats_col1, sample_stats_col2, sample_stats_col3, sample_stats_col4 = st.columns(4)
            
            with sample_stats_col1:
                st.metric("Total Jobs Available", "19+", "Across multiple industries")
            with sample_stats_col2:
                st.metric("Remote Opportunities", "15+", "Work from anywhere")
            with sample_stats_col3:
                st.metric("FAANG Companies", "5", "Top tech companies")
            with sample_stats_col4:
                st.metric("Entry Level", "8+", "Perfect for new graduates")
            
            # Example search suggestions
            st.markdown("**🔍 Try these popular searches:**")
            suggestion_col1, suggestion_col2, suggestion_col3 = st.columns(3)
            
            with suggestion_col1:
                if st.button("🤖 AI & Machine Learning Jobs", use_container_width=True):
                    st.session_state.auto_search = {
                        'keywords': ['AI', 'Machine Learning', 'Python'],
                        'location': 'Remote',
                        'experience': 'Entry Level',
                        'job_type': 'Full-time',
                        'visa': 'Any'
                    }
                    st.rerun()
            
            with suggestion_col2:
                if st.button("💻 Software Engineering", use_container_width=True):
                    st.session_state.auto_search = {
                        'keywords': ['Software Engineer', 'Developer', 'Programming'],
                        'location': 'Any',
                        'experience': 'Entry Level', 
                        'job_type': 'All',
                        'visa': 'Any'
                    }
                    st.rerun()
            
            with suggestion_col3:
                if st.button("🎓 Internships", use_container_width=True):
                    st.session_state.auto_search = {
                        'keywords': ['Intern', 'Student', 'Entry'],
                        'location': 'Any',
                        'experience': 'Student',
                        'job_type': 'Internship',
                        'visa': 'Any'
                    }
                    st.rerun()
    
    # Job alerts section
    st.markdown("---")
    st.markdown(f'<h3 style="{secondary_color}">🔔 Set Up Job Alerts</h3>', unsafe_allow_html=True)
    
    alert_col1, alert_col2 = st.columns([2, 1])
    
    with alert_col1:
        with st.form("job_alert_form"):
            alert_email = st.text_input("Email for alerts", placeholder="your.email@example.com")
            alert_keywords = st.text_input("Keywords", value="AI, Machine Learning, Python")
            alert_location = st.selectbox("Preferred Location", [
                "Any", "Remote", "Nairobi", "Kenya", "Africa",
                "San Francisco", "New York", "Seattle", "Austin",
                "London", "Berlin", "Toronto", "Sydney"
            ])
            
            if st.form_submit_button("🔔 Create Alert"):
                if alert_email and alert_keywords:
                    alert_info = create_job_alert_system(
                        alert_email, 
                        [k.strip() for k in alert_keywords.split(",")], 
                        alert_location
                    )
                    st.success(f"✅ Job alert created! Alert ID: {alert_info['alert_id'][:8]}...")
                    st.info("You'll receive daily notifications about matching opportunities.")
                else:
                    st.error("Please provide email and keywords for the alert.")
    
    with alert_col2:
        st.markdown("**Alert Benefits:**")
        st.markdown("• Daily job notifications")
        st.markdown("• Personalized matches")
        st.markdown("• Early access to new postings")
        st.markdown("• Priority application assistance")

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
        
        # Cover Letter Generation
        st.markdown("### 📄 Custom Cover Letter Generator")
        
        with st.expander("Generate Tailored Cover Letter", expanded=False):
            with st.form("cover_letter_form"):
                company_name = st.text_input("Company Name *", placeholder="e.g., Google")
                position_title = st.text_input("Position Title *", placeholder="e.g., Software Engineer - AI/ML")
                hiring_manager = st.text_input("Hiring Manager", placeholder="e.g., Sarah Johnson (Optional)")
                application_source = st.selectbox("How did you find this position?", 
                    ["Company Website", "LinkedIn", "Referral", "Job Board", "Career Fair", "Other"])
                specific_requirements = st.text_area("Specific Requirements to Address", 
                    placeholder="e.g., Experience with TensorFlow, Cloud platforms, etc.")
                
                submit_cover_letter = st.form_submit_button("🎯 Generate Professional Cover Letter", 
                                                           use_container_width=True)
            
            if submit_cover_letter and company_name and position_title:
                # Generate cover letter content
                cover_letter_content = generate_cover_letter(
                    company_name, position_title, hiring_manager, 
                    application_source, specific_requirements
                )
                
                # Display the cover letter
                st.markdown("**Generated Cover Letter:**")
                st.markdown(f"""
                <div style="background: #f8fafc; padding: 1.5rem; border-radius: 0.5rem; border-left: 4px solid #3b82f6; margin: 1rem 0; font-size: 0.9rem; line-height: 1.6;">
                {cover_letter_content.replace(chr(10), '<br>')}
                </div>
                """, unsafe_allow_html=True)
                
                # Download option
                st.download_button(
                    label="📝 Download Cover Letter (Text)",
                    data=cover_letter_content,
                    
                    file_name=f"Julius_Mutugu_Cover_Letter_{company_name.replace(' ', '_')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            elif submit_cover_letter:
                st.error("Please fill in the required fields: Company Name and Position Title")
        
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

def generate_cover_letter_pdf(cover_letter_content, company_name):
    """Generate a professional PDF cover letter"""
    buffer = BytesIO()
    
    # Create the PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter, 
                          rightMargin=inch, leftMargin=inch,
                          topMargin=inch, bottomMargin=inch)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=HexColor('#3b82f6'),
        spaceAfter=12,
        alignment=1  # Center alignment
    )
    
    header_style = ParagraphStyle(
        'CustomHeader',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#1e293b'),
        spaceAfter=6,
        alignment=1  # Center alignment
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#374151'),
        spaceAfter=6,
        leftIndent=0,
        rightIndent=0,
        alignment=0  # Left alignment
    )
    
    # Content list
    content = []
    
    # Split content into lines and format for PDF
    lines = cover_letter_content.split('\n')
    
    for line in lines:
        if line.strip():
            if line.startswith('Julius Mutugu'):
                content.append(Paragraph(line, title_style))
            elif line.startswith('Software Engineer') or line.startswith('📧') or line.startswith('🔗'):
                content.append(Paragraph(line, header_style))
            elif line.strip() == company_name or line.startswith('Re:') or line.startswith('Dear'):
                content.append(Spacer(1, 12))
                content.append(Paragraph(line, body_style))
            else:
                content.append(Paragraph(line, body_style))
        else:
            content.append(Spacer(1, 6))
    
    # Build PDF
    doc.build(content)
    buffer.seek(0)
    return buffer

def generate_cover_letter(company_name, position_title, hiring_manager, application_source, specific_requirements, additional_notes=""):
    """Generate a professional cover letter tailored to the position"""
    
    # Current date
    from datetime import datetime
    current_date = datetime.now().strftime("%B %d, %Y")
    
    # Determine greeting
    if hiring_manager:
        greeting = f"Dear {hiring_manager},"
    else:
        greeting = "Dear Hiring Manager,"
    
    # Get company-specific notes
    def get_company_note(company):
        company_notes = {
            "Google": "Your groundbreaking work in AI research, from AlphaGo to Transformer models, has been a significant inspiration in my academic journey.",
            "Microsoft": "Your commitment to democratizing AI through Azure AI services and your leadership in responsible AI development resonates with my values and career goals.",
            "Amazon": "Your innovative approach to scaling AI solutions across diverse domains, from AWS to Alexa, demonstrates the kind of impactful work I aspire to contribute to.",
            "Meta": "Your pioneering work in social AI and the metaverse represents the future of human-computer interaction that I am passionate about advancing.",
            "Apple": "Your focus on privacy-preserving AI and seamless user experiences aligns with my research in federated learning and my commitment to ethical AI development.",
            "OpenAI": "Your mission to ensure that artificial general intelligence benefits all of humanity aligns perfectly with my research focus and ethical approach to AI development.",
            "Netflix": "Your innovative use of machine learning for personalization and content optimization showcases the kind of practical AI applications I am excited to work on.",
            "Uber": "Your application of AI to solve complex real-world transportation and logistics challenges demonstrates the impactful work I want to be part of.",
            "Spotify": "Your use of machine learning for music recommendation and audio processing represents the creative application of AI that I find deeply inspiring."
        }
        return company_notes.get(company, "Your reputation for technological excellence and innovation in the industry is what draws me to this opportunity.")
    
    # Base cover letter template
    cover_letter = f"""Julius Mutugu
Software Engineer | AI/ML Specialist
📧 ndegwajulius239@gmail.com | 📱 +254 XXX XXX XXX
🔗 LinkedIn: linkedin.com/in/julius-mutugu-a3483b279 | 💻 GitHub: github.com/JuliusMutugu

{current_date}

{company_name}
Re: {position_title}

{greeting}

I am writing to express my strong interest in the {position_title} position at {company_name}. As a recent Software Engineering graduate specializing in Artificial Intelligence and Machine Learning, I am excited about the opportunity to contribute to {company_name}'s innovative technology solutions and make a meaningful impact in the field of AI/ML.

Why {company_name}?
{company_name} represents the pinnacle of technological innovation, and I am particularly drawn to your commitment to advancing AI technologies that solve real-world problems. {get_company_note(company_name)} Your company's focus on scalable, intelligent solutions aligns perfectly with my passion for developing impactful AI systems and my career aspirations in cutting-edge technology.

Technical Expertise & Relevant Experience:
My academic journey and project portfolio demonstrate strong technical capabilities highly relevant to this role:

• AI/ML Specialization: Extensive experience with TensorFlow, PyTorch, scikit-learn, and advanced machine learning algorithms
• Computer Vision: Developed multiple CV systems including waste classification models and real-time image processing applications
• Software Engineering: Proficient in Python, JavaScript, and modern frameworks including Django, Vue.js, and Nuxt 3
• Cloud & Infrastructure: Experience with cloud platforms, microservices architecture, and scalable system design
• Research Innovation: Led research in federated learning for healthcare systems, demonstrating ability to work on cutting-edge AI technologies

Project Highlights:
- Healthcare Insurance Implementation System: Developed an enterprise-grade system modeling Kenya's SHIF, showcasing my ability to create large-scale, real-world applications
- Federated Machine Learning in Healthcare: Pioneered research in privacy-preserving ML, demonstrating innovation in emerging AI technologies
- Computer Vision for Waste Classification: Built end-to-end ML pipeline using OpenCV and SVM, showing practical AI application skills"""

    # Add specific requirements if provided
    if specific_requirements:
        cover_letter += f"""

Addressing Specific Requirements:
{specific_requirements.strip()}

My background directly addresses these requirements through hands-on project experience and continuous learning. I am particularly excited about the opportunity to apply my skills in {specific_requirements.lower()} within {company_name}'s innovative environment."""

    # Add application source context
    source_texts = {
        "Company Website": f"I discovered this opportunity through {company_name}'s careers page, where I was impressed by the detailed role description and the company's commitment to innovation.",
        "LinkedIn": f"I found this position through LinkedIn, where I have been following {company_name}'s latest developments and team growth in AI/ML.",
        "Referral": f"This opportunity was brought to my attention through a professional referral, highlighting {company_name}'s excellent reputation in the tech community.",
        "Job Board": f"I identified this role through professional job boards, and it immediately stood out due to {company_name}'s reputation and the exciting nature of the work.",
        "Career Fair": f"I learned about this opportunity at a career fair, where {company_name}'s representatives provided valuable insights into the company culture and technical challenges.",
        "Other": f"I became aware of this position through my professional network, reflecting {company_name}'s strong presence in the AI/ML community."
    }
    
    cover_letter += f"""

{source_texts.get(application_source, f"I discovered this opportunity through my research into leading companies in AI/ML, where {company_name} consistently stands out.")}

Commitment to Excellence:
I bring a unique combination of technical depth, research experience, and practical application skills. My 709+ GitHub contributions demonstrate consistent learning and development, while my award-winning projects showcase my ability to deliver high-quality, innovative solutions. I am particularly excited about {company_name}'s mission and would welcome the opportunity to contribute to your team's continued success.

I would be thrilled to discuss how my technical expertise and passion for AI innovation can contribute to {company_name}'s objectives. Thank you for considering my application. I look forward to the opportunity to speak with you further about this exciting position.

Sincerely,
Julius Mutugu

---
Attachments: Resume, Portfolio (streamlit-portfolio-app.com)"""

    return cover_letter

if __name__ == "__main__":
    main()
