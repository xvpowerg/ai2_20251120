import streamlit as st
import pandas as pd
from datetime import  datetime
st.title("選擇元素測試")

option_selectbox = st.selectbox(
    "你喜歡的顏色是甚麼?",
    ["紅","綠","藍"]
)
st.write("你選了:",option_selectbox)

option_mult = st.multiselect("你喜歡的水果",["蘋果","香蕉","西瓜"])
st.write("你選了:",option_mult)