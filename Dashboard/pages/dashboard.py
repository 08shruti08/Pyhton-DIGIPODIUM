import streamlit as st  
import pandas as pd
import seaborn as sns
import plotly.express as px


st.title("Titanic Dashboard")   
st.write("This is a dashboard for analyzing the Titanic dataset.") 

df = sns.load_dataset("titanic")    
st.dataframe(df)  
#--------------------------------------------------------------  
#filters

st.sidebar.header("Filter Options") 

gender = st.sidebar.multiselect('Gender',
                                options= df['sex'].unique(),
                                default = df['sex'].unique())  
  
pclass = st.sidebar.multiselect('Passenger Class',
                                options= df['class'].unique(),
                                default = df['class'].unique())   

min_age, max_age = st.sidebar.slider('Age',
                                     min_value = int(df['age'].min()),
                                     max_value = int(df['age'].max()),
                                     value= (int(df['age'].min()), int(df['age'].max())))

filtered_df = df[
    (df['sex'].isin(gender)) &
    (df['class'].isin(pclass)) &
    (df['age']>=min_age) &
    (df['sex']<=max_age)
]


fig = px.histogram(filtered_df, 
                   x='age', 
                   title= "Age Distribution", 
                   template = 'plotly_dark')
st.plotly_chart(fig)    
st.title("Highest Count: 54 of age 24")
st.markdown("This graph shows the distribution of age of the people")

fig = px.bar(df, 
             x='survived', 
             title="Survival Count (0 = No, 1 = Yes)")
st.plotly_chart(fig, use_container_width=True)  
st.title("0 = did not survive, 1 = survived.")  
st.markdown("This graph shows how many passengers survived vs did not survive.")
