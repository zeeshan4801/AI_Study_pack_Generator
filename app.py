import streamlit as st
from workflow import generate_study_pack

st.set_page_config(page_title="AI Study Pack Generator", layout="wide")

st.title("🎓 AI Personalized Study Pack Generator")
st.write("Workflow: Planning → Content → Assessment → Review → Refinement")

subject = st.text_input("Subject")
topic = st.text_input("Topic")
grade = st.text_input("Class / Grade")
level = st.selectbox("Difficulty", ["Beginner","Intermediate","Advanced"])

if st.button("Generate Study Pack"):
    if not subject or not topic:
        st.warning("Please enter subject and topic.")
    else:
        student = {
            "subject": subject,
            "topic": topic,
            "grade": grade,
            "level": level
        }

        with st.spinner("AI workflow running..."):
            result = generate_study_pack(student)

        tabs = st.tabs(["Plan","Content","Assessment","Review","Final Pack"])

        with tabs[0]:
            st.write(result["plan"])
        with tabs[1]:
            st.write(result["content"])
        with tabs[2]:
            st.write(result["assessment"])
        with tabs[3]:
            st.write(result["review"])
        with tabs[4]:
            st.write(result["final"])
            st.download_button("Download", result["final"], "study_pack.txt")
