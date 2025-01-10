import streamlit as st
import multiple_pages.Data_Ingestion
import multiple_pages.LLM_Chat

# Set the page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":rocket:",
    layout="centered",
    initial_sidebar_state="expanded",
    #toolbar_mode="developer"  # Change this to "viewer", "minimal", or "auto" as needed
)
def intro():
    import streamlit as st

    st.write("# Welcome to Area51 👋")
    st.sidebar.success("Select a Module above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
        """
    )


def Data_Ingestion():
    multiple_pages.Data_Ingestion.app()

def LLM_Chat():
    multiple_pages.LLM_Chat.app()

page_names_to_funcs = {
    "—": intro,
    "Data Ingestion": Data_Ingestion,
    "LLM Chat": LLM_Chat
    # "DataFrame Demo": data_frame_demo
}


# Add an image in sidebar that is alligned in center
st.sidebar.image("static/Area.png", use_container_width=True, caption="")

# Add Sidebar
demo_name = st.sidebar.selectbox("Choose a Module", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()





# Add a Footer in sidebar
st.sidebar.markdown(
    """
    <hr>
    <p style="color:grey; font-size:10px; text-align:center;">
    Made by <a href="https://harshity.in/">Harshit Yadav</a>
    </p>
    """,
    unsafe_allow_html=True,
)



