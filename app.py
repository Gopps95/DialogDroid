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
user_input = get_input()

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