import streamlit as st

st.title("シンプル電卓")

a = st.number_input("数字A", value=1.0)
b = st.number_input("数字B", value=2.0)

if st.button("足し算する"):
    st.write("結果：", a + b)

