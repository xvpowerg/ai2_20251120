import streamlit as st
st.title("測試計算")
num1 = st.number_input("請輸入第一個數字",value=0.0)
num2 = st.number_input("請輸入第二個數字",value=0.0)
sum_result = num1 + num2
st.write(f"Sum:{sum_result:.2f}")