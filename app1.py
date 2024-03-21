import streamlit as st
from hugchat import hugchat

streamlit_style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;1,100&display=swap');

        .hotel-bold {
            font-weight: 600;
        }

        .hotel-font {
            font-size: 20px;
            background-color: #e6f9ff;
        }

        label.css-1p2iens.effi0qh3{
            font-size: 18px;
        }

        p{
            font-size: 18px;
        }
        li{
            font-size: 18px;
        }		
        #MainMenu{
            visibility: hidden;
        }	  
        button.css-135zi6y.edgvbvh9{
            font-size: 18px;
            font-weight: 600;
        }

        /* Add this CSS to position the input container at the bottom */
        .input-container {
            position: fixed;
            bottom: 20px;
            left: 0;
            right: 0;
            padding: 10px;
            background-color: white;
            box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
"""

st.set_page_config(page_title="DialogDroid")


if 'bot_response' not in st.session_state:
    st.session_state['bot_response'] = ["I'm Sunny kuttan, How may I help you?"]

if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ['Hi!']

def get_input():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    response = chatbot.chat(prompt)
    return response

# Create a container for the chat history
chat_container = st.container()

# Create a container for the text input box
input_container = st.container()

# Render the chat history
with chat_container:
    for i in range(len(st.session_state['user_input'])):
        st.write(f"User: {st.session_state['user_input'][i]}")
        st.write(f"DialogDroid: {st.session_state['bot_response'][i]}")

# Render the text input box
with input_container:
    user_input = get_input()
    if user_input:
        response = generate_response(user_input)
        st.session_state.user_input.append(user_input)
        st.session_state.bot_response.append(response)

# Add the custom CSS
st.markdown(streamlit_style, unsafe_allow_html=True)