import streamlit as st

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2, gap="small")

with col1:
    st.image("imgs/8.png")

with col2:
    st.subheader("Mehmet Eren Efegil")
    info_content = """
    Learn Python from zero to complete by building real programs to gain the skills needed to land an entry-level job.
    """
    st.info(info_content)