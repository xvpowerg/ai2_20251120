from datetime import datetime
import streamlit as st
dataList = ["春","夏","秋","冬"]
option_radio = st.radio(
    "你喜歡的季節",dataList
)
st.write("你的季節:",option_radio)

checkbox = st.checkbox("是否同意")

if checkbox:
    st.write("同意")
else:
    st.write("不同意")
st.write("checkbox:",checkbox)        