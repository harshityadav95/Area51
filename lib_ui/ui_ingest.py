import streamlit as st


def app():
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("Filename:", uploaded_file.name)
            st.write(bytes_data)