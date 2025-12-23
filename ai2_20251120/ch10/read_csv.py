import streamlit as st
import pandas as pd
st.title("讀取CSV檔案")
upload_file = st.file_uploader("上傳CSV檔")
#print(upload_file)
if upload_file:
    df = pd.read_csv(upload_file)
    st.subheader("原始數據")
    st.dataframe(df)
    st.subheader("資料描述")
    st.dataframe(df.describe())
    st.subheader("資料圖表")
    st.line_chart(df)


    columns = st.selectbox("選擇顯示列數",df.columns)
    st.dataframe(df[columns])
    