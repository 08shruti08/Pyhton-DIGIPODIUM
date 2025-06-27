import streamlit as st  
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title("Titanic Dashboard")   
st.write("This is a dashboard for analyzing the Titanic dataset.") 

df = sns.load_dataset("titanic")    
st.dataframe(df)        

# create plotly graphs for tittanic dataset
