import streamlit as st

st.title("Hello Streamlit")
user_input = st.text_input("請入訊息")
st.write(f"你輸入的內容:{user_input}")
