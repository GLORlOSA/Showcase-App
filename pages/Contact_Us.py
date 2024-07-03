import streamlit as st

st.set_page_config(layout="wide")



st.title("Contact Us")

st.text("")

with st.form(key="emailform"):
    st.text_input("Enter Your Email Adress", key="usermail")
    st.text_area("Enter Your Message", key="usercontext", height=200)
    st.form_submit_button("Send", use_container_width=100)