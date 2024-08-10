import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title='Data analysis',page_icon=':bar_chart:',layout='wide')
st.title(':green[Student Performance Analysis]')

df=pd.read_excel('student details.xlsx',sheet_name='Student Routine')
st.write(df)

st.header(':blue[Average Time Spent On Sleeping And Social Media]')

avg_sleep=df['Sleep Time'].mean()
avg_social=df['Social Media'].mean()
st.write(f'Average sleep:', avg_sleep)
st.write(f'Average social:', avg_social)

st.header('Test Prepration Pie Chart' )

test_prep=df['Test Prep'].value_counts().reset_index()
st.write(test_prep)
fig=px.pie(data_frame=test_prep,names='Test Prep',values='count',title='Test Preparation')
st.write(fig)