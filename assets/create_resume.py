from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os

def create_modern_resume():
    filename = "Julius_Mutugu_Resume.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, 
                          rightMargin=0.5*inch, leftMargin=0.5*inch,
                          topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    # Define colors
    primary_blue = HexColor('#3b82f6')
    dark_blue = HexColor('#1d4ed8')
    light_gray = HexColor('#f8fafc')
    text_gray = HexColor('#4a5568')
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=primary_blue,
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=text_gray,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=text_gray,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=primary_blue,
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontSize=10,
        textColor=text_gray,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    project_title_style = ParagraphStyle(
        'ProjectTitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=black,
        spaceAfter=4,
        fontName='Helvetica-Bold'
    )
    
    # Build the document content
    content = []
    
    # Header section
    content.append(Paragraph("JULIUS MUTUGU", title_style))
    content.append(Paragraph("AI Software Engineer | Machine Learning Specialist | Full-Stack Developer", subtitle_style))
    
    # Contact info
    contact_info = """
    📧 ndegwajulius239@gmail.com  |  🌐 github.com/JuliusMutugu  |  💼 linkedin.com/in/julius-mutugu  |  📍 Nairobi, Kenya
    """
    content.append(Paragraph(contact_info, contact_style))
    
    # Add a line separator
    content.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=primary_blue))
    
    # Professional Summary
    content.append(Paragraph("PROFESSIONAL SUMMARY", section_title_style))
    summary_text = """
    Innovative Software Engineer with specialized expertise in AI, Machine Learning, and Full-Stack Development. 
    Proven track record in developing healthcare systems, implementing federated learning solutions, and creating 
    data-driven applications. Strong foundation in computer vision, blockchain technology, and microservices 
    architecture. Passionate about leveraging technology to solve real-world problems in healthcare, agriculture, 
    and financial sectors.
    """
    content.append(Paragraph(summary_text, body_style))
    
    # Education
    content.append(Paragraph("EDUCATION", section_title_style))
    education_text = """
    <b>Bachelor of Software Engineering</b><br/>
    University of Eastern Africa, Baraton (UEAB) | 2025<br/>
    Specialization: Artificial Intelligence & Machine Learning<br/>
    Focus: Advanced AI technologies, federated learning, and software engineering principles
    """
    content.append(Paragraph(education_text, body_style))
    
    # Technical Skills
    content.append(Paragraph("TECHNICAL SKILLS", section_title_style))
    
    skills_data = [
        ['Programming Languages:', 'Python, JavaScript, Java, SQL, R'],
        ['AI/ML Technologies:', 'TensorFlow, PyTorch, OpenCV, Federated Learning, Computer Vision, SVM'],
        ['Web Development:', 'Nuxt 3, Node.js, Django, RESTful APIs, HTML/CSS, Flask'],
        ['Mobile & Desktop:', 'Flutter, Flet Framework, React Native, Cross-platform Development'],
        ['Databases & Cloud:', 'MongoDB Atlas, MySQL, PostgreSQL, Microservices Architecture'],
        ['Tools & Practices:', 'Git/GitHub, Agile Methodology, CI/CD, Power BI, Docker']
    ]
    
    skills_table = Table(skills_data, colWidths=[2*inch, 4.5*inch])
    skills_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 0), (0, -1), primary_blue),
        ('TEXTCOLOR', (1, 0), (1, -1), text_gray),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    content.append(skills_table)
    content.append(Spacer(1, 12))
    
    # Key Projects
    content.append(Paragraph("KEY PROJECTS & ACHIEVEMENTS", section_title_style))
    
    projects = [
        {
            'title': 'Healthcare Insurance Implementation System (Kenya\'s SHIF Model)',
            'description': 'Comprehensive healthcare insurance system based on Kenya\'s Social Health Insurance Fund model with advanced fraud detection and optimized fund allocation mechanisms.',
            'tech': 'Python, Blockchain, Microservices, Agile, CI/CD',
            'highlights': ['Integration with multiple insurance providers', 'Advanced fraud detection algorithms', 'Microservices architecture implementation']
        },
        {
            'title': 'Federated Machine Learning in Healthcare Systems',
            'description': 'Research and implementation of federated learning for healthcare systems to enhance data privacy while training models across decentralized datasets.',
            'tech': 'Python, Federated Learning, Privacy-Preserving ML, Healthcare Data',
            'highlights': ['Enhanced data privacy and security', 'Decentralized model training', 'Research-grade implementation']
        },
        {
            'title': 'Research and Grant Management System (UEAB)',
            'description': 'Full-stack university platform for managing research and grants with public researcher profiles, status tracking, and community forums.',
            'tech': 'Nuxt 3, MongoDB Atlas, Node.js, Agile, CI/CD',
            'highlights': ['Public researcher profiles', 'Grant status tracking', 'Community collaboration features']
        },
        {
            'title': 'Computer Vision for Waste Dataset Classification',
            'description': 'Intelligent waste classification system using Support Vector Machine with batch processing techniques for large-scale dataset optimization.',
            'tech': 'Python, OpenCV, SVM, Computer Vision, Data Processing',
            'highlights': ['Accurate waste classification', 'Batch processing optimization', 'Environmental impact focus']
        }
    ]
    
    for project in projects:
        content.append(Paragraph(project['title'], project_title_style))
        content.append(Paragraph(project['description'], body_style))
        content.append(Paragraph(f"<b>Technologies:</b> {project['tech']}", body_style))
        
        highlights_text = "<b>Key Achievements:</b><br/>"
        for highlight in project['highlights']:
            highlights_text += f"• {highlight}<br/>"
        content.append(Paragraph(highlights_text, body_style))
        content.append(Spacer(1, 8))
    
    # Professional Achievements
    content.append(Paragraph("PROFESSIONAL ACHIEVEMENTS", section_title_style))
    achievements_text = """
    • <b>709+ GitHub Contributions:</b> Demonstrating consistent development activity and open source engagement<br/>
    • <b>Multiple Starred Repositories:</b> Recognition for quality code and innovative solutions<br/>
    • <b>University Hackathon Participation:</b> Active engagement in competitive programming and data analysis<br/>
    • <b>Research Publications:</b> Focus on federated learning and privacy-preserving machine learning<br/>
    • <b>Industry-Ready Projects:</b> Healthcare, agriculture, and financial technology solutions
    """
    content.append(Paragraph(achievements_text, body_style))
    
    # Career Objectives
    content.append(Paragraph("CAREER OBJECTIVES", section_title_style))
    objectives_text = """
    Seeking opportunities at leading technology companies (Google, Microsoft, Amazon, Meta) to contribute 
    innovative AI solutions and full-stack development expertise. Passionate about leveraging technology 
    for social impact, particularly in healthcare and sustainable development initiatives. Ready to tackle 
    complex challenges in enterprise-scale AI and software engineering projects.
    """
    content.append(Paragraph(objectives_text, body_style))
    
    # Build the PDF
    doc.build(content)
    print(f"Modern resume created: {filename}")
    return filename

if __name__ == "__main__":
    create_modern_resume()
