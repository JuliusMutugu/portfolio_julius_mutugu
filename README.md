# AI Software Engineer Portfolio

A professional portfolio website built with Streamlit to showcase AI, Machine Learning, and Software Engineering projects.

## 🚀 Features

- **Interactive Project Showcase**: Filter and explore projects by category
- **Skills Visualization**: Interactive charts showing technical proficiency
- **Professional Design**: Clean, modern interface optimized for recruiters
- **Contact Form**: Direct communication channel
- **CV Download**: Easy access to resume/CV
- **Responsive Design**: Works on all devices
- **SEO Optimized**: Better visibility for online presence

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly, Pandas
- **Styling**: Custom CSS
- **Animations**: Lottie files
- **Icons**: Streamlit-option-menu

## 📁 Project Structure

```
portfolio/
├── main.py                 # Main Streamlit application
├── config.py              # Configuration and data
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── assets/                # Images, CV, and other assets
└── README.md             # This file
```

## 🚦 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

The application will open in your browser at `http://localhost:8501`

## 📝 Customization

### 1. Update Your Information

Edit `config.py` to add your personal information:

- **Projects**: Add your GitHub projects with descriptions, tech stacks, and links
- **Skills**: Update your technical skills and proficiency levels
- **Contact Info**: Add your email, phone, LinkedIn, GitHub links
- **Education**: Update your educational background

### 2. Add Your Projects

For each project in `config.py`, include:

- Title and description
- Category (AI, Computer Vision, NLP, Web Development, etc.)
- Tech stack used
- GitHub repository link
- Live demo link (if available)
- Key highlights and achievements
- Technical details (accuracy, performance metrics, etc.)

### 3. Add Assets

Place the following in the `assets/` folder:

- **CV/Resume**: `cv.pdf`
- **Project Images**: `project1.png`, `project2.png`, etc.
- **Profile Photo**: `profile.jpg` (optional)

### 4. Customize Styling

Modify the CSS in `main.py` to match your preferred color scheme and design.

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click

### Other Platforms

- **Heroku**: Use the provided `requirements.txt`
- **AWS/Azure**: Deploy as a containerized application
- **Vercel/Netlify**: For static deployment with build steps

## 🎯 FAANG Application Tips

This portfolio is designed to impress recruiters at top tech companies:

### ✅ What Makes It Stand Out

- **Technical Depth**: Showcases both AI expertise and full-stack capabilities
- **Interactive Demos**: Proves your projects actually work
- **Clean Design**: Professional appearance that's easy to navigate
- **Quantified Results**: Includes metrics like accuracy, performance, etc.
- **Comprehensive Skills**: Shows breadth across multiple technologies

### 📈 Optimization for Recruiters

- **Quick Overview**: Home page summarizes your value proposition
- **Project Focus**: Emphasizes AI/ML projects with real-world applications
- **Technical Details**: Includes the depth that technical interviewers want to see
- **Contact Integration**: Makes it easy for recruiters to reach out

## 🔧 Advanced Features

### Adding Interactive Demos

You can integrate live demos of your projects:

```python
# Example: Add a simple ML model demo
if st.button("Try Live Demo"):
    # Your model inference code here
    result = your_model.predict(user_input)
    st.success(f"Prediction: {result}")
```

### Analytics Integration

Add Google Analytics or other tracking:

```python
# In main.py, add tracking code
st.components.v1.html("""
<!-- Google Analytics code -->
""", height=0)
```

## 📞 Support

If you need help customizing this portfolio:

1. Check the [Streamlit Documentation](https://docs.streamlit.io)
2. Review the code comments for guidance
3. Create an issue on GitHub for bugs or feature requests

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built with ❤️ for aspiring FAANG engineers**

Ready to showcase your AI expertise and land that dream job at Google, Microsoft, Amazon, or any top tech company!
