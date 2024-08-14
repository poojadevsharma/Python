## import libraries

import pandas as pd
import plotly.express as px
import streamlit as st

    
st.set_page_config(page_title='Consoleflare Analytics Portal',page_icon="📊")

##title
st.title(':rainbow[Data Analytics Portal]')

st.subheader(':gray[Explore Data with ease.]',divider='rainbow')

file=st.file_uploader(':blue[upload your file]',type=['csv','xlsx'])
if (file!=None):
    if(file.name.endswith('.csv')):
        data=pd.read_csv(file)
    else:
        data=pd.read_excel(file)
    st.dataframe(data)
    st.info('file is successfully uploaded',icon='✅')


    st.subheader(':rainbow[Basic information of the dataset]',divider='rainbow')
    tab1,tab2,tab3,tab4=st.tabs(['Summary','Top and Bottom','Data Types','Columns'])
    with tab1:
        st.write(f'There are {data.shape[0]} row in dataset and {data.shape[1]} columns in dataset')
        st.subheader(':gray[Statistical summary of the dataset]')
        st.dataframe(data.describe())
    with tab2:
        st.subheader(':gray[Top rows ]')
        toprows=st.slider('Select number of rows you want',min_value=1,max_value=data.shape[0],key='topslider')
        st.dataframe(data.head(toprows))
        st.subheader(':gray[Bottom rows ]')
        bottomrows=st.slider('Select number of rows you want',min_value=1,max_value=data.shape[0],key='bottomslider')
        st.dataframe(data.tail(bottomrows))
    with tab3:
        st.subheader(':gray[Data types of the columns]')
        st.dataframe(data.dtypes)
    with tab4:
        st.subheader(':gray[Column Names in dataset]')
        st.write(list(data.columns))

    st.subheader(':rainbow[Column Values To Count]',divider='rainbow')
    with st.expander('Value Count'):
        col1,col2=st.columns(2)
        with col1:
            column=st.selectbox('Select column',options=list(data.columns))
        with col2:
            toprows=st.number_input('Top rows',min_value=1,step=1)
        count=st.button('Count')
        if count==True:
            result=data[column].value_counts().reset_index().head(toprows)
            st.dataframe(result)
            st.subheader('Visualize',divider='gray')
            fig=px.bar(data_frame=result,x=column,y='count',text='count',template='plotly_white')
            st.plotly_chart(fig)
            fig=px.line(data_frame=result,x=column,y='count',text='count',template='plotly_white',markers='o')
            st.plotly_chart(fig)
            fig=px.pie(data_frame=result,names=column,values='count')
            st.plotly_chart(fig)
        
    st.subheader(':rainbow[Groupby : Simplify your data analysis]',divider='rainbow')
    st.write('The groupby lets you summarize data by specific categories and groups')
    with st.expander('Groupby By Your Columns'):
        col1,col2,col3=st.columns(3)
        with col1:
            groupby_col=st.multiselect('choose column to groupby',options=list(data.columns))
        with col2:
            operation_col=st.selectbox('choose column for operation',options=list(data.columns))
        with col3:
            operation=st.selectbox('choose operation',options=['sum','mean','min','max','count'])

        if (groupby_col):
            result=data.groupby(groupby_col).agg(
            newcol=(operation_col,operation)
                    ).reset_index()
            st.dataframe(result)
            st.subheader(':gray[Data Visualization]',divider='gray')
            graph=st.selectbox('choose your graph',options=['line','bar','scatter','pie','sunburst'])
            if graph=='line':
                x_axis=st.selectbox('Choose x axis',options=list(result.columns))
                y_axis=st.selectbox('Choose y axis',options=list(result.columns))
                color=st.selectbox('Color Information ',options=[None]+list(result.columns))
                fig=px.line(data_frame=result,x=x_axis,y=y_axis,color=color,template='plotly_white',markers='o')
                st.plotly_chart(fig)
            elif graph=='bar':
                x_axis=st.selectbox('Choose x axis',options=list(result.columns))
                y_axis=st.selectbox('Choose y axis',options=list(result.columns))
                color=st.selectbox('Color Information ',options=[None]+list(result.columns))
                facet_col=st.selectbox('Facet Column',options=[None]+list(result.columns))
                fig=px.bar(data_frame=result,x=x_axis,y=y_axis,color=color, facet_col=facet_col,barmode='group')
                st.plotly_chart(fig)
            elif graph=='scatter':
                x_axis=st.selectbox('Choose x axis',options=list(result.columns))
                y_axis=st.selectbox('Choose y axis',options=list(result.columns))
                color=st.selectbox('Color Information ',options=[None]+list(result.columns))
                size=st.selectbox('Size Column',options=[None]+list(result.columns))
                fig=px.scatter(data_frame=result,x=x_axis,y=y_axis,color=color,size=size,template='plotly_white')
                st.plotly_chart(fig)
            elif graph=='pie':
                names=st.selectbox('Choose labels',options=list(result.columns))
                values=st.selectbox('Choose Numerical values',options=list(result.columns))
                fig=px.pie(data_frame=result,names=names,values=values,template='plotly_white')
                st.plotly_chart(fig)
            elif graph=='sunburst':
                path=st.multiselect('Choose your path',options=list(result.columns))
                fig=px.sunburst(data_frame=result,path=path,values='newcol')
                st.plotly_chart(fig)

        
        
        
    


    


