import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

#--------------------Page configuration---------------------------------------------------------------
st.set_page_config(page_title="Spotify Dashboard", page_icon=":bar_chart:", layout="wide")


# st.image("https://kreafolk.com/cdn/shop/articles/spotify-logo-design-history-and-evolution-kreafolk_b995ad53-7473-4492-9710-58b9e5c32ecd.jpg?v=1717725016&width=2048")

#---------------------Load data---------------------------------------------------------------
# Use st.cache_data to cache the data loading function
@st.cache_data
def load_data():
    df = pd.read_csv("Spotify_Dataset/spotify_tracks.csv")
    return df
df = load_data()

#-------------------Show data preview----------------------------------------------------------------
st.markdown(""" <h1 style="color:lightgreen;">🎧Spotify Dashboard | A Comprehensive Collection of Tracks Across Various Genres🎼</h1>""", unsafe_allow_html = True)
st.header("Explore the World of Music with Our Extensive Spotify Dataset")
st.write("This dashboard provides insights into a wide range of tracks, including their popularity, genres, and audio features. You can explore the dataset to discover trends and patterns in music.")
st.dataframe(df.head(101))

#-------------------Sidebar filters---------------------------------------------------------------
st.sidebar.header("Filter Options")

#------------------Genre filter----------------------------------------------------------------
st.sidebar.subheader("🎵 Genre Filter")
# Get unique genres and create a multiselect filter
# Drop NaN values and convert to list
genre = df['genre'].dropna().unique().tolist()
genre_filter= st.sidebar.multiselect("🎼 Select Genre(s):", genre, default=genre[:5])

#-----------------Explicit filter--------------------------------------------------------
st.sidebar.subheader("🔞 Explicit Content Filter")
# Create a selectbox for explicit content filter
explicit_filter = st.sidebar.selectbox("Explicit Content:", ['All', 'Explicit', 'Non-Explicit'])

#-----------------Filter data--------------------------------------------------------
# Filter the DataFrame based on user selections
filtered_data = df[df['genre'].isin(genre_filter)]

if explicit_filter == 'Explicit':
    filtered_data = filtered_data[filtered_data['explicit'] == True]
elif explicit_filter == 'Non-Explicit':
    filtered_data = filtered_data[filtered_data['explicit'] == False]

# -------------Popularity Distribution-----------------------------------------------
st.subheader("Histogram:🌟 Popularity Distribution")
# graph 1. Histogram of Popularity with a box plot marginal
fig_pop = px.histogram(filtered_data, 
                       x="popularity", 
                       nbins=20, 
                       color="genre", 
                       marginal="box")
st.plotly_chart(fig_pop, use_container_width=True)


#-----------------Track Duration-------------------------------------------------
#subheader for track duration
st.subheader("Bar Chart:⏱️ Average Duration per Genre (in minutes)")

df_duration = filtered_data.copy() # Create a new DataFrame for duration analysis
df_duration['duration_min'] = df_duration['duration_ms'] / 60000 # Convert duration from milliseconds to minutes and calculate average duration per genre

# Group by genre and calculate average duration
avg_duration = df_duration.groupby("genre")['duration_min'].mean().sort_values(ascending=False).reset_index() # Sort by average duration in descending order

# graph 2. Bar chart of average duration per genre
fig_duration = px.bar(avg_duration, 
                      x="genre", y="duration_min",
                      color="genre",
                      labels={'duration_min': 'Avg Duration (min)'})
st.plotly_chart(fig_duration, use_container_width=True)


#-------------------🧑‍🎤 Top Artists by Track Count----------------------------------------
#subheader for top artists
st.subheader("Bar Chart:🎤 Top Artists by Number of Tracks")

# Expand the artists column for multiple entries
# Drop NaN values, split by comma, and explode the DataFrame to get individual artists
all_artists = df['artists'].dropna().str.split(",").explode().str.strip()

top_artists = all_artists.value_counts().head(10).reset_index()
top_artists.columns = ['artist', 'track_count']

# graph 3. Bar chart of top artists by track count
fig_artists = px.bar(top_artists, 
                    x='artist', y='track_count', 
                    color='track_count',
                    labels={'track_count': 'Track Count'})
st.plotly_chart(fig_artists, use_container_width=True)


#------------------Popular vs Explicit Breakdown---------------------------------------
#subheader for explicit vs non-explicit
st.subheader("Pie Chart:🔥 Average Popularity: Explicit vs Non-Explicit")
popularity_explicit = df.groupby('explicit')['popularity'].mean().reset_index()
popularity_explicit['explicit'] = popularity_explicit['explicit'].replace({True: 'Explicit', False: 'Non-Explicit'})

# graph 4. Pie chart of average popularity comparison
fig_exp = px.pie(popularity_explicit, 
                 names='explicit', 
                 values='popularity',
                 title="Average Popularity Comparison")
st.plotly_chart(fig_exp, use_container_width=True)

#------------------Popularity vs Track Duration---------------------------------------
st.subheader("Scatter Plot:🌀Popularity vs Track Duration (in minutes)")

df['duration_min'] = df['duration_ms'] / 60000

# graph 5. Scatter plot of popularity vs duration by genre
fig_pop_dur = px.scatter(df, x='duration_min', y='popularity', 
                         color='genre', hover_data=['name', 'artists'],
                         title='Popularity vs Duration by Genre')
st.plotly_chart(fig_pop_dur, use_container_width=True)

#------------------Most Common Genres------------------------------------------------
#subheader for most common genres
st.subheader("Bar Chart:🎷 Most Common Genres in the Dataset")

genre_count = df['genre'].value_counts().head(10).reset_index() # Count the number of tracks per genre and get the top 10 genres
genre_count.columns = ['genre', 'count']

# graph 6. Bar chart of top 10 genres by track count
fig_genre = px.bar(genre_count, x='genre', y='count', color='count',
                   labels={'count': 'Number of Tracks'},
                   title='Top 10 Genres by Track Count')
st.plotly_chart(fig_genre, use_container_width=True)
#-------------------- Footer--------------------------------------------------------

st.markdown("---")
st.markdown(""" <p style = "text-align:center;">💡Built by Shruti Bajpai ❤️| Dataset of Spotify from Kaggle | 📊 Powered by Python, Streamlit & Plotly | 10 July, 2025</p>""", unsafe_allow_html=True)
