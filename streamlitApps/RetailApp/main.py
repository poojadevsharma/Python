import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px


st.title(':blue[Retail Data Analysis]')

df=pd.read_csv("\retail_data.csv")

st.header('Total Number of Transactions')
##total number of transactions

ndf=df.loc[df['Transaction_ID'].isnull()]
tt=ndf['Phone'].nunique(dropna=True)+df['Transaction_ID'].nunique(dropna=True)


## Total sales sum
df['Sales']=df['Amount']*df['Total_Purchases']
ts=df['Sales'].sum()


##average sales

ndf=df.loc[df['Sales'].notnull()]


q1,q3=np.percentile(ndf['Sales'],(25,75))
iqr=q3-q1
ux=q3+1.5*iqr

ndf=ndf.loc[ndf['Sales']<ux]
avg_sales=ndf['Sales'].mean()


col1,col2,col3=st.columns(3)
with col1:
    st.metric('Total Number Of Transations',round(tt))
with col2:
    st.metric('Total Sales',round(ts))
with col3:
    st.metric('Average Sales',round(avg_sales))


## Gender wise customer base
st.header('Gender wise Customer base')

ndf=df['Gender'].value_counts().reset_index()
st.write(ndf)

fig=px.pie(data_frame=ndf,values='count',names='Gender')
st.plotly_chart(fig)





