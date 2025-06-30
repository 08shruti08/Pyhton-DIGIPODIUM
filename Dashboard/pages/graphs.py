import streamlit as st  
import pandas as pd
import seaborn as sns
import plotly.express as px


st.title("Titanic Dashboard")   
st.write("This is a dashboard for analyzing the Titanic dataset.") 

df = sns.load_dataset("titanic")    
st.dataframe(df)        

# create plotly graphs for tittanic dataset
#-----------------------------------------------------------------------------
# 1. Bar chart: Survival count   
fig1 = px.bar(df, x='survived', title="Survival Count (0 = No, 1 = Yes)")
st.plotly_chart(fig1, use_container_width=True) 

# 2. Pie chart: Gender distribution
gender_count = df['sex'].value_counts().reset_index()
fig2 = px.pie(gender_count, names='sex', values='count', title="Gender Distribution")
st.plotly_chart(fig2, use_container_width=True)

# 3. Histogram: Age distribution
fig3 = px.histogram(df, x='age', nbins=30, title="Age Distribution")
st.plotly_chart(fig3, use_container_width=True)

# 4. Box plot: Age by class
fig4 = px.box(df, x='class', y='age', color='class', title="Age Distribution by Class")
st.plotly_chart(fig4, use_container_width=True)

# 5. Bar chart: Survival by class
survival_class = df.groupby(['class', 'survived']).size().reset_index(name='count')
fig5 = px.bar(survival_class, x='class', y='count', color='survived', barmode='group',
              title="Survival Count by Class")
st.plotly_chart(fig5, use_container_width=True)

# 6. Violin plot: Age distribution by sex
fig6 = px.violin(df, y='age', x='sex', color='sex', box=True, title="Age Distribution by Gender")
st.plotly_chart(fig6, use_container_width=True)

# 7. Heatmap: Correlation matrix
st.subheader("Correlation Heatmap")
correlation = df.select_dtypes(include='number').corr()
fig7 = px.imshow(correlation, text_auto=True, aspect="auto", title="Numerical Feature Correlation")
st.plotly_chart(fig7, use_container_width=True)

# 8. Scatter plot: Age vs Fare colored by survival
fig8 = px.scatter(df, x='age', y='fare', color='survived', title="Age vs Fare by Survival")
st.plotly_chart(fig8, use_container_width=True)

# 9. Sunburst chart: Class -> Sex -> Survived
fig9 = px.sunburst(df, path=['class', 'sex', 'survived'], title="Hierarchy of Class, Sex and Survival")
st.plotly_chart(fig9, use_container_width=True)

# 10. Density heatmap: Fare vs Age
fig10 = px.density_heatmap(df, x='fare', y='age', nbinsx=30, nbinsy=30, color_continuous_scale="Viridis",
                           title="Fare vs Age Density Heatmap")
st.plotly_chart(fig10, use_container_width=True)