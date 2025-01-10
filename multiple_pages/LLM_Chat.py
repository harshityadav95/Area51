import streamlit as st

def app():
    st.title('LLM Chat')
    st.write('This is the `LLM Chat` page of the multi-page app')
    
    ## Add a dropdown in sidebar to choose LLM Model frop dropdown
    st.sidebar.markdown('## Configuration')
    model = st.sidebar.selectbox("Choose LLM Model", ["GPT-4o", "GPT-3", "T5"])


