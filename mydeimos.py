# Importing the necessary modules from the Streamlit and LangChain packages
import streamlit as st
from langchain.llms import OpenAI

# Setting the title of the Streamlit application
st.title('The Crown Prince of Kremnos, Mydeimos, at your service.')

# Creating a sidebar input widget for the OpenAI API key, input type is password for security
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Defining a function to generate a response using the OpenAI lanuage model
def generate_response(input_text):
	# Initializing the OpenAI language model with a specified temperature and API key
	llm = OpenAI(temperature=0.0, openai_api_key=openai_api_key)
	# Displaying the generated response as an informational message in the Streamlit app
	st.info(llm(input_text))

# Creating a form in the Streamlit app for user input
with st.form('my_form'):
    # Adding a text area for user input
    text = st.text_area('Enter text:', '')
    # Adding a submit button for the form
    submitted = st.form_submit_button('Submit')
    # Displaying a warning if the entered API key does not start with 'sk-'
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    # If the form is submitted and the API key is valid, generate a response
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
