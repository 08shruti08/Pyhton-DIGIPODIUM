# Open terminal(ctrl+j)-->to run FOLDER (cd Foldername)--> to run file(streamlit run filename.py)
# First run folder then file or sub files

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="🚗 Car Crashes Dashboard", layout="wide")

st.title("Car Crashes Analysis Dashboard 📊")
st.markdown("This dashboard shows the detailed insights of Car Crashes Dataset")


df = sns.load_dataset("car_crashes")
st.dataframe(df)  

# Filters-------------------------------------------------------------------------------

st.sidebar.header("🔍 Filter Options")
selected_states = st.sidebar.multiselect("Select States:", 
                                         options=df['abbrev'].unique(), 
                                         default=df['abbrev'].unique())

# Filtered DataFrame
filtered_df = df[df['abbrev'].isin(selected_states)]

#----------------------------------------------------------------
st.subheader("Dataset Preview")

# 1. Total car cradhes by states
st.subheader("Total crashes per states")
fig = px.bar(df, x = 'abbrev', y = 'total',
             title = 'Total Crashes by US States', 
             labels = {'abbrev': 'States', 'total': 'Total Crashes'})
st.plotly_chart(fig, use_container_width = True)

# 2. Insurance Premium vs Insurance Losses
st.subheader("Insurance Premium vs Losses")
fig = px.scatter(df, x='ins_premium', y='ins_losses', color='abbrev',
                  title="Insurance Premium vs Losses by State",
                  labels={'ins_premium': 'Insurance Premium ($)', 'ins_losses': 'Insurance Losses ($)'})
st.plotly_chart(fig, use_container_width=True)

# 3. Speeding-related crashes vs Total crashes
st.subheader("Speeding vs Total Crashes")
fig = px.scatter(df, x='speeding', y='total', size='total', color='abbrev',
                  title="Speeding Involvement vs Total Crashes")
st.plotly_chart(fig, use_container_width=True)

# 4. Alcohol involvement in crashes by state
st.subheader("Alcohol Involvement per State")
fig = px.bar(df.sort_values(by='alcohol', ascending=False), x='abbrev', y='alcohol',
              title="Alcohol-Related Accidents by State")
st.plotly_chart(fig, use_container_width=True)

# 5. Distracted driving vs Total crashes
st.subheader("Distracted Driving vs Total Crashes")
fig = px.scatter(df, x='not_distracted', y='total', color='abbrev',
                  title="Not Distracted vs Total Crashes (lower = more distraction)")
st.plotly_chart(fig, use_container_width=True)

# 6. Heatmap of correlations
st.subheader(" Correlation Heatmap")
corr = df.select_dtypes(include='number').corr()
fig = px.imshow(corr, text_auto=True, title="Correlation Between Numeric Features")
st.plotly_chart(fig, use_container_width=True)

# 7. Distribution of Total Crashes
st.subheader("Distribution of Total Crashes")
fig = px.histogram(df, x='total', nbins=20, title="Histogram of Total Crashes")
st.plotly_chart(fig, use_container_width=True)

# 8. Boxplot: Insurance Premiums
st.subheader("Insurance Premium Distribution")
fig = px.box(df, y='ins_premium', title="Boxplot of Insurance Premiums")
st.plotly_chart(fig, use_container_width=True)

# 9. Top 10 states by insurance losses
st.subheader(" Top 10 States by Insurance Losses")
top10_loss = df.sort_values(by='ins_losses', ascending=False).head(10)
fig = px.bar(top10_loss, x='abbrev', y='ins_losses', title="Top 10 States with Highest Insurance Losses")
st.plotly_chart(fig, use_container_width=True)

# 10. Pairwise Scatter Matrix
st.subheader(" Pairwise Feature Comparison")
fig = px.scatter_matrix(df, dimensions=['total', 'speeding', 'alcohol', 'ins_premium', 'ins_losses'],
                          color='abbrev', title="Scatter Matrix of Selected Features")
st.plotly_chart(fig, use_container_width=True)