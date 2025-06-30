# Open terminal(ctrl+j)-->to run FOLDER (cd Foldername)--> to run file(streamlit run filename.py)
# First run folder then file or sub files

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title("📊 Car Crashes Analysis Dashboard")
st.markdown("This dashboard shows the detailed insights of Car Crashes Dataset")


df = sns.load_dataset("car_crashes")
st.dataframe(df)                                