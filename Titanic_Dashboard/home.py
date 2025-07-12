import streamlit as st  


st.set_page_config(page_title="Titanic Dashboard", layout="wide", page_icon=":ship:")


st.markdown(""" <h1 style: "text-align: center; color: white;">Titanic Data Analysis Dashboard</h1> """, unsafe_allow_html=True)
st.image("https://image.tmdb.org/t/p/original/ukGhy7uTtOauwLeR4biuFy0rkWk.png", caption="Titanic Logo")

st.markdown(""" <h2 style: "text-align: center; color: blue;"> Objective of the Analysis </h2>
         <p style: "text-align: center; color: yellow; font-size: 20px;">The goal is to analyze the Titanic passenger data to uncover the key factors that influenced survival during the disaster and to present insights in a visually compelling and business-relevant manner.</p>""", unsafe_allow_html=True)
st.header("This is a dashboard for analyzing the Titanic dataset.")

st.image("https://miro.medium.com/v2/resize:fit:665/1*c3GBCb6VcSDCvWHkdqsTmg.png", caption="Titanic Logo")

st.markdown(""" <h2 style:"text-align: center;">Look at the tragic disaster of Titanic, which sank on April 15, 1912, after hitting an iceberg.""", unsafe_allow_html=True)
st.image("https://static1.moviewebimages.com/wordpress/wp-content/uploads/article/3bB2UnWTUkslTngQMkwRZbO3qdYkhD.jpg", caption="Titanic Poster")
st.image("https://i1.wp.com/cdn-images-1.medium.com/max/750/1*IC1b2AnebaOYNK8PdZFwTQ.jpeg?ssl=1", caption="Titanic Ship")

st.markdown(""" <ul>
            <li><b>Who had the best chances of survival?</b></li>
            <li><b>Did gender, age, and wealth affect survival?</b></li>
            <li><b>What does this reveal about human behavior during crises? </b></li>
         </ul>""", unsafe_allow_html=True)

st.markdown(""" <h2 style = "text-align: center; color : white; font-size: 20px;"> To know these doubts, Visit the plotly graphs page to know more about the Titanic dataset.</h2>""", unsafe_allow_html=True)