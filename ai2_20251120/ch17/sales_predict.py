import streamlit as st
import pandas as pd
import joblib
st.title("銷售預測應用")
model,scaler = joblib.load(r"C:\Users\xvpow\ai2_20251120\ch17\sales_model_scaler.pkl")
tv_spend = st.number_input("輸入TV廣告支出",min_value=0.0)
radio_spend = st.number_input("輸入Radio廣告支出",min_value=0.0)
newspaper_spend = st.number_input("輸入NewsSaper廣告支出",min_value=0.0)

if st.button("預測銷售"):
    input_data = {
        "TV":tv_spend,
        "radio":radio_spend,
        "newspaper":newspaper_spend
    }
    input_df = pd.DataFrame([input_data])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    st.subheader("預測結果")
    st.write(f"預測的銷售額為:{prediction}")