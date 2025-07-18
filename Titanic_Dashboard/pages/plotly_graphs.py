import streamlit as st  
import pandas as pd
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Titanic Dashboard", layout="wide")


st.markdown(""" <h1 style = "text-align: center; color: White;">Unlocking the Story Behind the Numbers 🚢</h1>
            <p style = "text-align: left; color: Yellow; font-size:20px;">🎯 The Titanic dataset tells a powerful story of how Social class, Gender, and Age affected survival during one of history’s most tragic disasters. Through these visualizations, we uncover insights not only for data analysis — but for human empathy and decision-making.</p>
            """, unsafe_allow_html=True)

st.title("Titanic Dataset")   
#st.write("This is a dashboard for analyzing the Titanic dataset.") 

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

st.markdown("""<h1 style ="text-align:center; color:lightblue;">Data-Driven Insights from the Titanic Tragedy</h1>""", unsafe_allow_html=True)

# create plotly graphs for tittanic dataset

# 1. Bar chart: Survival count -------------------------------------------------------------------------------------------------  

st.markdown(""" <h2 style = "text-align: center; color: White;">1. Bar Chart: Survival Count</h1>""", unsafe_allow_html=True)

fig1 = px.bar(df, x='survived', 
              title="Survival Count (0 = No, 1 = Yes)")
st.plotly_chart(fig1, use_container_width=True) 

st.subheader("📖 Storytelling:")
st.markdown("This basic visualization shows the number of passengers who survived vs. who did not. The gap is significant.")

st.markdown("""<ul>
                <p>✅ Final Outcome:</p>
                <li>Out of 891 passengers, only ~38% survived, confirming the tragedy's scale. This sets the stage for understanding the factors behind survival.</li>
              </ul>""", unsafe_allow_html=True)

# 2. Pie chart: Gender distribution ------------------------------------------------------------------------------------------------

st.markdown(""" <h2 style = "text-align: center; color: White;" >2. Pie Chart: Gender Distribution </h1>""", unsafe_allow_html=True)
gender_count = df['sex'].value_counts().reset_index() # Rename columns for clarity
fig2 = px.pie(gender_count, 
              names='sex', 
              values='count', 
              title="Gender Distribution")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📖 Storytelling:")
st.markdown("The pie chart reflects that ~65% of passengers were male and ~35% were female.")

st.markdown("""<ul>
                <p>✅ Final Outcome:</p>
                <li>The ship had a higher number of male passengers, yet as we will see, females had a far better survival rate — introducing the impact of gender on survival.</li>
              </ul>""", unsafe_allow_html=True)


# 3. Histogram: Age distribution ----------------------------------------------------------------------------------------------------------

st.markdown(""" <h2 style = "text-align: center; color: White;">3. Histogram: Age Distribution of Titanic Passengers</h2>""", unsafe_allow_html=True)
fig3 = px.histogram(df, x='age', 
                    nbins=30, 
                    title="Age Distribution")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("📖 Storytelling:")
st.markdown("The age histogram shows that most passengers were in their 20s and 30s, with some children and elderly passengers.")

st.markdown("""<ul>
                <p>✅ Final Outcome:</p>
                <li>Majority of passengers were young adults, highlighting a youthful crowd on the ship. However, survival varied greatly across age groups.</li>
              </ul>""", unsafe_allow_html=True)


# 4. Box plot: Age by class --------------------------------------------------------------------------------------------------------

st.markdown(""" <h2 style = 'text-align: center; color: White;'> 4. Box Plot: Age Distribution by Class</h2>""", unsafe_allow_html=True)
fig4 = px.box(df, x='class', y='age', 
              color='class', 
              title="Age Distribution by Class")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("📖 Storytelling:")
st.markdown("This chart reveals that 1st class had more middle-aged passengers, while 3rd class had younger and often larger families.")

st.markdown("""<ul>
                <p>✅ Final Outcome:</p>
                <li>Wealthier passengers were generally older, likely traveling for leisure, while poorer classes included families or young workers seeking opportunity.</li>
              </ul>""", unsafe_allow_html=True)


# 5. Bar chart: Survival by class ---------------------------------------------------------------------------------------------------------

st.markdown(""" <h2 style = "text-align: center; color: White;">5. Bar Chart: Survival Count by Class</h2>""", unsafe_allow_html=True)
survival_class = df.groupby(['class', 'survived']).size().reset_index(name='count') #groupby and rename columns of survival count by class
fig5 = px.bar(survival_class, x='class', y='count', 
              color='survived', 
              barmode='group', # barmode='group' to show bars for each class side by side
              title="Survival Count by Class")
st.plotly_chart(fig5, use_container_width=True)

st.subheader("📖 Storytelling:")
st.markdown("First-class passengers had the highest number of survivors, while third-class had the most deaths.")

st.markdown("""<ul>
                <p>✅ Final Outcome:</p>
                <li>Class significantly impacted survival. First-class passengers had better access to lifeboats, space, and information. Third-class passengers were at the bottom decks, far from safety.</li>
              </ul>""", unsafe_allow_html=True)


# 6. Violin plot: Age distribution by sex ----------------------------------------------------------------------------------------------------

st.markdown(""" <h2 style = "text-align: center; color: White;">6. Violin Plot: Age Distribution</h2> """, unsafe_allow_html=True)
fig6 = px.violin(df, y='age', x='sex', 
                 color='sex', 
                 box=True, 
                 title="Age Distribution by Gender")
st.plotly_chart(fig6, use_container_width=True)

st.subheader("📖 Storytelling:")
st.markdown("The violin plot shows age spread and density for survivors vs. non-survivors. Children had a survival advantage.")

st.markdown("""<ul>
                <p>✅ Final Outcome:</p>
                <li>Children and younger females survived more, likely due to the “women and children first” policy. Older male passengers had the least chance.</li>
              </ul>""", unsafe_allow_html=True)


# 7. Heatmap: Correlation matrix ----------------------------------------------------------------------------------------------------------------

st.markdown(""" <h2 style = "text-align: center; color: white;">7. Heatmap: Correlation Matrix of Numerical Features</h2> """, unsafe_allow_html = True)
correlation = df.select_dtypes(include='number').corr()  # Select only numerical columns for correlation
fig7 = px.imshow(correlation, 
                 text_auto=True, #text_auto=True to show correlation values
                 aspect="auto",  # aspect="auto" to adjust heatmap aspect ratio
                 title="Numerical Feature Correlation")  
st.plotly_chart(fig7, use_container_width=True)

st.subheader("📖 Storytelling:")
st.markdown("This matrix helps identify relationships like survival’s correlation with Pclass, Fare, and Sex (as encoded).")

st.markdown("""<ul>
                <p>✅ Final Outcome:</p>
                <li>The most correlated factors with survival are:
                <li>-Fare (positive correlation) — Higher fare = Higher survival</li>
                <li>-Pclass (negative correlation) — Higher class = Higher survival</li>
            </ul>""", unsafe_allow_html=True)


# 8. Scatter plot: Age vs Fare colored by survival --------------------------------------------------------------------------------------------

st.markdown(""" <h2 style = "text-align: center; color: white;">8. Scatter Plot: Age vs Fare by Survival</h2> """, unsafe_allow_html = True)
fig8 = px.scatter(df, x='age', y='fare', 
                  color='survived', 
                  title="Age vs Fare by Survival")
st.plotly_chart(fig8, use_container_width=True)

st.subheader("📖 Storytelling:")
st.markdown("This chart shows that passengers who paid higher fares and were younger had better survival outcomes.")

st.markdown("""<ul>
                <p>✅ Final Outcome:</p>
                <li>This hierarchical chart lets you drill down — e.g., among first-class females, most survived; among third-class males, most did not.</li>
              </ul>""", unsafe_allow_html=True)


# 9. Sunburst chart: Class -> Sex -> Survived -------------------------------------------------------------------------------------------------------------

st.markdown(""" <h2 style = "text-align: center; color: white;">9. Sunburst Chart: Hierarchy of Class, Sex and Survival</h2> """, unsafe_allow_html = True)
fig9 = px.sunburst(df, 
                   path=['class', 'sex', 'survived'], 
                   title="Hierarchy of Class, Sex and Survival")
st.plotly_chart(fig9, use_container_width=True)

st.subheader("📖 Storytelling:")
st.markdown("This hierarchical chart lets you drill down — e.g., among first-class females, most survived; among third-class males, most did not.")

st.markdown("""<ul>
                <p>✅ Final Outcome:</p>
                <li>Best odds: First-class females</li>
                <li>Worst odds: Third-class males</li>
                <li>The sunburst shows the intersectionality of class and gender influencing survival — it's not just one feature, but a combined profile.</li>
              </ul>""", unsafe_allow_html=True)


# 10. Density heatmap: Fare vs Age --------------------------------------------------------------------------------------------------------------------------

st.markdown(""" <h2 style = "text-align: center; color: white;">10. Density Heatmap: Fare vs Age</h2> """, unsafe_allow_html = True)
fig10 = px.density_heatmap(df, x='fare', y='age', 
                           nbinsx=30, nbinsy=30, 
                           color_continuous_scale="Viridis",
                           title="Fare vs Age Density Heatmap")
st.plotly_chart(fig10, use_container_width=True)

st.subheader("📖 Storytelling:")
st.markdown("This heatmap shows where passengers are concentrated by fare and age. Most were in the lower fare and mid-age group.")

st.markdown("""<ul>
                <p>✅ Final Outcome:</p>
                <li>Young adults in low fare range were the majority. But high-survival clusters appeared in older, wealthier sections, indicating survival wasn't equally distributed.</li>
              </ul>""", unsafe_allow_html=True)

st.markdown("---")


st.markdown(""" <h2 style = "text-align: center; color : white; font-size: 20px;">Thank you for visiting my Titanic Dashboard!</h2>""", unsafe_allow_html=True)
st.markdown(""" <h2 style = "text-align: right; color : white; font-size: 25px;">Created by ~ Shruti Bajpai </h2>""", unsafe_allow_html=True)

