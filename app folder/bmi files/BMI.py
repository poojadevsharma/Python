import streamlit as st


st.set_page_config(page_title= "My BMI Analysi", page_icon=":tada:")

st.title(":red[BMI Calculator App]")

weight=st.number_input("Enter your weight (in kgs)")
height=st.number_input("Enter your height (in meters)")

click=st.button("Calculate BMI")

if click==True:
    bmi=weight/(height**2)
    st.write("Your BMI is",bmi)


