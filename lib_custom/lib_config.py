import streamlit as st
import json


def config_ingest():
    # List of accepted file formats
    accepted_formats = ['json']

    # Streamlit file uploader
    uploaded_file = st.file_uploader("Upload a Config file for the Storage", type=accepted_formats, accept_multiple_files=False)

    if uploaded_file:
        try:
            # Load the JSON file
            data = json.load(uploaded_file)
            st.write("✅ File uploaded successfully!")

            # Extract key-value pairs
            key_value_pairs = [(key, value) for key, value in data.items()]
            # st.write("Key-Value Pairs:", key_value_pairs)
            return key_value_pairs
        except json.JSONDecodeError:
            st.write("❌ Invalid JSON file. Please upload a valid JSON file.")
            return []
    else:
        st.write("Please upload a .json file.")
        return []

# def config_load():
