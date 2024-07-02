import streamlit as st
import pandas

st.set_page_config(layout="wide")

# col1, col2 = st.columns(2, gap="small")


# with col1:
   # st.image("imgs/8.png", width=300)

# with col2:
st.title("Mehmet Eren Efegil")
info_content = """
Learn Python from zero to complete by building real programs to gain the skills needed to land an entry-level job.
Learn Python from zero to complete by building real programs to gain the skills needed to land an entry-level job.
Learn Python from zero to complete by building real programs to gain the skills needed to land an entry-level job.
Learn Python from zero to complete by building real programs to gain the skills needed to land an entry-level job.
Learn Python from zero to complete by building real programs to gain the skills needed to land an entry-level job.
Learn Python from zero to complete by building real programs to gain the skills needed to land an entry-level job.
"""
st.info(info_content)

col3, col4 = st.columns(2)


text_content = """
Learn Python from zero to complete Learn Python from zero to complete 
"""
st.text(text_content)

with col3:
    for index, row in pandas.read_csv("data.csv", sep=";")[::2].iterrows():
        st.subheader(row["title"])

with col4:
    for index, row in pandas.read_csv("data.csv", sep=";")[1::2].iterrows():
        st.subheader(row["title"])