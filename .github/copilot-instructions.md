<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Portfolio Project - Copilot Instructions

This is a Streamlit-based portfolio website for an AI/ML Software Engineer targeting FAANG companies.

## Project Context

- **Purpose**: Professional portfolio to showcase AI, Computer Vision, NLP, and Software Engineering projects
- **Target Audience**: Recruiters and hiring managers at Google, Microsoft, Amazon, Meta, Apple
- **Tech Stack**: Streamlit, Python, Plotly, Pandas, CSS
- **Specialization**: Artificial Intelligence and Machine Learning

## Code Style Guidelines

- Use clean, professional Python code following PEP 8 standards
- Write clear docstrings for all functions
- Use type hints where appropriate
- Prefer functional programming and modular design
- Include error handling and input validation

## Streamlit Best Practices

- Use `st.cache_data` for expensive computations
- Implement proper state management with `st.session_state`
- Create reusable components and functions
- Optimize performance for large datasets
- Follow responsive design principles

## AI/ML Integration

- When adding ML demos, use lightweight models suitable for web deployment
- Include proper error handling for model predictions
- Show confidence scores and model metrics
- Provide clear explanations of model capabilities and limitations

## Design Principles

- Maintain professional, clean aesthetics suitable for corporate recruiters
- Use consistent color scheme (#1f77b4 primary, complementary colors)
- Ensure mobile responsiveness
- Prioritize fast loading times and smooth interactions
- Include accessibility features

## Project Structure

- `main.py`: Main Streamlit application with navigation and page functions
- `config.py`: Configuration file with project data, skills, and personal information
- `assets/`: Directory for images, CV, and other static files
- `.streamlit/config.toml`: Streamlit configuration for theming and settings

## Content Guidelines

- Emphasize quantifiable achievements (accuracy percentages, performance metrics)
- Showcase technical depth while maintaining accessibility
- Include links to GitHub repositories and live demos
- Highlight technologies relevant to FAANG companies
- Focus on scalability, performance, and real-world applications

## Security Considerations

- Never commit sensitive information (API keys, personal data)
- Use environment variables for configuration
- Implement proper input validation for contact forms
- Follow security best practices for web deployment
