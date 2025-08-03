import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Esha Pandey | Portfolio", page_icon="💻")

# ----- Sidebar -----
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "AI/ML Projects", "DevOps Projects", "Resume", "Contact"])

# ----- About -----
if page == "About Me":
    st.title("👋 Hi, I'm Esha Pandey")
    st.write("🎓 BCA Final Year Student | AI & DevOps Enthusiast")
    st.write("""
    - 📍 Based in Kathmandu, Nepal  
    - 💡 Interested in NLP, LLMs, RAG, and cloud automation  
    - 💻 Experienced with Python, Terraform, Ansible, Docker, GitHub Actions  
    - 🧠 Built projects across DevOps and AI/ML domains
    """)

# ----- AI Projects -----
elif page == "AI/ML Projects":
    st.title("🧠 AI & ML Projects")
    st.markdown(Path("projects/ai_projects.md").read_text())

# ----- DevOps Projects -----
elif page == "DevOps Projects":
    st.title("⚙️ DevOps Projects")
    st.markdown(Path("projects/devops_projects.md").read_text())

# ----- Resume -----
elif page == "Resume":
    st.title("📄 My Resume")
    with open("resume.pdf", "rb") as f:
        st.download_button("Download Resume", f, "Esha_Pandey_Resume.pdf", "application/pdf")

# ----- Contact -----
elif page == "Contact":
    st.title("📬 Contact Me")
    st.markdown("""
    - 💌 Email: [your-email@example.com](mailto:your-email@example.com)  
    - 🧑‍💻 GitHub: [github.com/yourusername](https://github.com/yourusername)  
    - 🔗 LinkedIn: [linkedin.com/in/yourusername](https://linkedin.com/in/yourusername)
    """)

