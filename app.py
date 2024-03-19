import streamlit as st
from hugchat import hugchat

st.set_page_config(page_title="DialogDroid")

# Generate empty lists for bot_response and user_input.
## bot_response stores AI generated responses
if 'bot_response' not in st.session_state:
    st.session_state['bot_response'] = ["I'm Sunny kuttan, How may I help you?"]
## user_input stores User's questions
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ['Hi!']

# User input
def get_input():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
user_input = get_input()

# Response output
def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    response = chatbot.chat(prompt)
    return response

if user_input:
    response = generate_response(user_input)
    st.session_state.user_input.append(user_input)
    st.session_state.bot_response.append(response)

for i in range(len(st.session_state['user_input'])):
    st.write(f"User: {st.session_state['user_input'][i]}")
    st.write(f"DialogDroid: {st.session_state['bot_response'][i]}")