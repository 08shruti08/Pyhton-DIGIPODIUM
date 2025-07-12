import streamlit as st  
import pandas as pd
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Titanic Dashboard", page_layout="wide")

st.title("Unlocking the Story Behind the Numbers")   
st.write("This is a dashboard for analyzing the Titanic dataset.") 

df = sns.load_dataset("titanic")    
st.dataframe(df)  
#--------------------------------------------------------------  
#filters

st.sidebar.header("Filter Options") 
# Gender filter

gender = st.sidebar.multiselect('Gender',
                                options= df['sex'].unique(), # Gender options
                                default = df['sex'].unique())  # Default to all genders

# Passenger Class filter
pclass = st.sidebar.multiselect('Passenger Class',
                                options= df['class'].unique(),
                                default = df['class'].unique())   # Default to all classes
# Age filter
# Using slider to filter age range

min_age, max_age = st.sidebar.slider('Age',
                                     min_value = int(df['age'].min()), # Minimum age
                                     max_value = int(df['age'].max()), # Maximum age
                                     value= (int(df['age'].min()), int(df['age'].max()))) # Default age range
# Filter DataFrame based on selected filters
filtered_df = df[
    (df['sex'].isin(gender)) & # Filter by gender
    (df['class'].isin(pclass)) & # Filter by passenger class
    (df['age'] >= min_age) & (df['age'] <= max_age) # Filter by age range
]

#------------------------------------------------------------------------
fig = px.histogram(filtered_df, 
                   x='age', 
                   title= "Age Distribution", 
                   template = 'plotly_dark')
st.plotly_chart(fig)    
st.title("Highest Count: 54 of age 24")
st.markdown("This graph shows the distribution of age of the people")
#------------------------------------------------------------------------
fig = px.bar(filtered_df, 
             x='survived', 
             title="Survival Count (0 = No, 1 = Yes)")
st.plotly_chart(fig, use_container_width=True)  
st.title("0 = did not survive, 1 = survived.")  
st.markdown("This graph shows how many passengers survived vs did not survive.")
#------------------------------------------------------------------------
fig = px.pie(filtered_df,
                names='class',
                title="Passenger Class Distribution",
                color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig, use_container_width=True)
st.title("This pie chart shows the distribution of passengers across different classes.")
st.markdown("The pie chart provides a visual representation of the proportion of passengers in each class, highlighting the distribution of first, second, and third class passengers on the Titanic.")