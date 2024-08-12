import streamlit as st
import wikipedia as wiki


st.set_page_config(page_title="Wikipedia Search", page_icon=":mag:", layout="wide")

st.title(":blue[Search Anything With Me]")

topic=st.text_input(":green[Search Anything]")
click=st.button("Search")

if click==True:
    result=wiki.summary(topic)
    st.write(result)