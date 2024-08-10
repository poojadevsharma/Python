import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px


st.title('Retail Data Analysis')

df=pd.read_csv('retail_data.csv')

st.header('Total Number of Transactions')
##total number of transactions

ndf=df.loc[df['Transaction_ID'].isnull()]
tt=ndf['Phone'].nunique(dropna=True)+df['Transaction_ID'].nunique(dropna=True)

st.metric(tt)