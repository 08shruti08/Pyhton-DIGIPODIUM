import streamlit as st

# Page settings
st.set_page_config(page_title="Spotify Home", layout="wide")

st.title("🎵 Welcome to the Spotify Dashboard")
st.markdown("Explore insights into your favorite tracks, artists, and genres!")


st.markdown("---")

#Spotify logo
st.image("https://cymatics.fm/cdn/shop/articles/Music-On-Spotify-Yoast_1200x1200.jpg?v=1552056915")

# Dataset Artist that are displayed in columns
st.subheader("🎤 Featured Artists")

# Displaying images of Spotify artists in a 5-column layout
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("https://pickasso.spotifycdn.com/image/ab67c0de0000deef/dt/v1/img/radio/artist/2wY79sveU1sp5g7SokKOiI/en", caption="Sam Smith- Spotify Playlist")
with col2:
    st.image("https://pickasso.spotifycdn.com/image/ab67c0de0000deef/dt/v1/img/radio/artist/2FyfsZmatt8gWR3LKnQIwE/en", caption="Rose & Frey - Spotify Playlist")
with col3:
    st.image("https://thisis-images.spotifycdn.com/37i9dQZF1DZ06evO35ZtUF-default.jpg", caption="Billy Raffoul - Spotify Playlist")
with col4:
    st.image("https://pickasso.spotifycdn.com/image/ab67c0de0000deef/dt/v1/img/radio/artist/2sil8z5kiy4r76CRTXxBCA/de", caption="Goo Goo Dolls - Spotify Playlist")
with col5:
    st.image("https://image-cdn-ak.spotifycdn.com/image/ab67706c0000da84fd9f303d451116ab9bd61c1f", caption="Benson Boone - Spotify Playlist")

#image of full tracklist
st.image("https://plus.pointblankmusicschool.com/wp-content/uploads/2023/02/spotify-playlists.jpg")

# Navigation instruction
st.header("📊 Want to explore the Spotify data?")
st.subheader("Head over to the Dashboard insights")
st.markdown("👉 Go to the sidebar and click on **Dashboard** to begin exploring interactive charts and insights.")
