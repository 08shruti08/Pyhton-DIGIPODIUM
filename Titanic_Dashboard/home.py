import streamlit as st  


st.set_page_config(page_title="Titanic Dashboard", layout="wide")


st.markdown("""<h1 style="text-align:center;">🚢 Titanic Dashboard</h1>""", unsafe_allow_html=True)
#st.image("https://image.tmdb.org/t/p/original/ukGhy7uTtOauwLeR4biuFy0rkWk.png", caption="Titanic Logo")
st.image("https://ichef.bbci.co.uk/images/ic/1200x675/p0l4bchs.jpg", caption="Titanic Logo")

st.markdown(""" <h1 style = "color:Yellow;">Objective of the Data Analysis</h1>
            <p style = "color:orange; font-size:20px;">The goal is to analyze the Titanic passenger data to uncover the key factors that influenced survival during the disaster and to present insights in a visually compelling and business-relevant manner.</p>
            """, unsafe_allow_html=True)

st.header("This is a dashboard for analyzing the Titanic dataset.")

st.image("https://miro.medium.com/v2/resize:fit:1024/1*iH3ShJCknUC4Z77_SBNtDw.png", caption="Titanic Logo")

st.markdown(""" <h2 style:"text-align: center;">Look at the tragic disaster of Titanic, which sank on April 15, 1912, after hitting an iceberg.""", unsafe_allow_html=True)
st.image("https://static1.moviewebimages.com/wordpress/wp-content/uploads/article/3bB2UnWTUkslTngQMkwRZbO3qdYkhD.jpg", caption="Titanic Poster")

st.markdown(""" <h2 style="text-align: center; color: red;">An Interactive Journey Through Data & Decisions</h2>""", unsafe_allow_html=True)
st.image("https://i.ytimg.com/vi/fATVVQfFyU0/maxresdefault.jpg")


st.markdown(""" <ul>
            <li><b style = "font-size: 20px;">Who had the best chances of survival?</b></li>
            <li><b style = "font-size: 20px;">Did gender, age, and wealth affect survival?</b></li>
            <li><b style = "font-size: 20px;">What does this reveal about human behavior during crises? </b></li>
         </ul>""", unsafe_allow_html=True)

st.markdown(""" <h2 style = "text-align: center; color : white; font-size: 20px;">👉To know these doubts, Visit the plotly graphs page to know more about the Titanic dataset.</h2>""", unsafe_allow_html=True)