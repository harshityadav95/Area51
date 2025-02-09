import streamlit as st
import google.generativeai as gpt
from lib_google.lib_gemini import *

def app():

    ## Add a dropdown in sidebar to choose LLM Model frop dropdown
    # st.sidebar.markdown('## Configuration')
    # model = st.sidebar.selectbox("Choose LLM Model", ["GPT-4o", "Gemini", "Phi-4"])
    # genai.configure(api_key=st.secrets["google"]["gemini"].get("gemini_key"))
    # model = genai.GenerativeModel("gemini-1.5-flash")
    # response = model.generate_content("Explain how AI works")
    # st.write(response.text)

    API_KEY = st.secrets["google"]["gemini"].get("gemini_key")

    # Set up Google Gemini-Pro AI model
    gpt.configure(api_key=API_KEY)
    model = gpt.GenerativeModel('gemini-1.5-flash')

    # Initialize chat session in Streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # Display the chatbot's title on the page
    st.title("🤖 Chat with Gemini-Pro")

    # Display the chat history
    for msg in st.session_state.chat_session.history:
        with st.chat_message(map_role(msg["role"])):
            st.markdown(msg["content"])

    # Input field for user's message
    user_input = st.chat_input("Ask Gemini-Pro...")
    if user_input:
        # Add user's message to chat and display it
        st.chat_message("user").markdown(user_input)

        # Send user's message to Gemini and get the response
        gemini_response = fetch_gemini_response(user_input)

        # Display Gemini's response
        with st.chat_message("assistant"):
            st.markdown(gemini_response)

        # Add user and assistant messages to the chat history
        st.session_state.chat_session.history.append({"role": "user", "content": user_input})
        st.session_state.chat_session.history.append({"role": "model", "content": gemini_response})

