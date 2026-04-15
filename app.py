import streamlit as st

st.title("⚙️ FlowSync - Workflow Automation")

task = st.text_input("Enter Task")
if st.button("Run Workflow"):
    st.success(f"Task '{task}' executed successfully!")
