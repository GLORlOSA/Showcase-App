import streamlit as st
import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "efegileren@gmail.com"
password = "uqpj bbbs gbbx tnmd"

receiver = "efegileren@gmail.com"
context = ssl.create_default_context()

message="""
shckjsdbd
sakdlşaskdlş
sakdlkjas
"""

st.set_page_config(layout="wide")



st.title("Contact Us")

st.text("")

with st.form(key="emailform"):
    text_input = st.text_input("Enter Your Email Adress", key="usermail")
    text_area = st.text_area("Enter Your Message", key="usercontext", height=200)
    button = st.form_submit_button("Send", use_container_width=100)
    if button:
        message = st.session_state["usercontext"]
        receiver = st.session_state["usermail"]
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username,receiver,message)
        st.info("Mail have sent successfully")





st.session_state
