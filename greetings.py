import streamlit as st
 
st.title("Dialogroid")
st.write("Your new virtual assistant")
name = st.text_input(label="",placeholder="Enter your name", max_chars=50)
if st.button('Submit'):
    st.write('Hi ' + name + ". How can I assist you today ?")
