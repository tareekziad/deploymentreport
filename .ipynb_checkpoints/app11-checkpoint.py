
import pandas as pd 
import streamlit as st
import plotly.express as px 

df = px.data.tips()

def box_plot():
    time = st.sidebar.radio('select time' , df['time'].unique())
    sub_df = df[df['time'] == time]
    st.plotly_chart(px.box(data_frame=sub_df , x = 'total_bill'))
    
def histogram():
    sex = st.sidebar.radio('select sex' , df['sex'].unique())
    sub_df = df[df['sex'] == sex]
    st.plotly_chart(px.histogram(data_frame=sub_df , x = 'total_bill'))

def violin_scatter():
    smoker = st.sidebar.radio('select smoker' , df['smoker'].unique())
    sub_df = df[df['smoker'] == smoker]
    st.plotly_chart(px.violin(data_frame=sub_df , x = 'total_bill'))
    st.plotly_chart(px.scatter(data_frame=sub_df , x = 'total_bill' , y = 'tip'))


pages = {
    'box_plot' : box_plot,
    'histogram' : histogram,
    'violin_scatter' : violin_scatter
}

pg = st.sidebar.radio('Navigate Pages' , pages.keys())


pages[pg]()

