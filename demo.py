"""
Quick Demo Script to Test Portfolio
"""

import streamlit as st
import subprocess
import sys

def main():
    st.set_page_config(
        page_title="Portfolio Demo",
        page_icon="🚀",
        layout="wide"
    )
    
    st.title("🚀 Portfolio Demo Launcher")
    st.markdown("This is a quick demo to test your portfolio functionality.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎨 Features Included")
        st.markdown("""
        - ✅ **Dark/Light Theme Toggle**
        - ✅ **Smooth Animations**
        - ✅ **Modern Gradient Design**
        - ✅ **Professional Color Scheme**
        - ✅ **Interactive Elements**
        - ✅ **Responsive Layout**
        - ✅ **White Text on Dark Theme**
        - ✅ **Hover Effects**
        """)
    
    with col2:
        st.markdown("### 🛠️ Tech Stack")
        st.markdown("""
        - **Frontend**: Streamlit
        - **Styling**: Custom CSS with animations
        - **Charts**: Plotly
        - **Icons**: Bootstrap Icons
        - **Animations**: CSS keyframes + Lottie
        - **Theme**: Dynamic Dark/Light mode
        """)
    
    st.markdown("---")
    
    if st.button("🚀 Launch Full Portfolio", use_container_width=True):
        st.success("✅ Portfolio is ready! Run `streamlit run main.py` in your terminal.")
        st.balloons()
    
    st.markdown("### 📋 Next Steps")
    st.markdown("""
    1. **Customize Your Data**: Update the projects, skills, and contact info in `main.py`
    2. **Add Your GitHub Link**: Replace placeholder URLs with your actual repositories
    3. **Upload Your CV**: Add your resume file to the assets folder
    4. **Add Project Images**: Include screenshots of your projects
    5. **Deploy**: Host on Streamlit Cloud, Heroku, or your preferred platform
    """)

if __name__ == "__main__":
    main()
