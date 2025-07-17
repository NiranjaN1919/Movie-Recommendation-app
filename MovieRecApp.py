import streamlit as st
import pickle
import base64

recommend_movie=[]
movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = movies['title'].values

st.header('Movies Recommendation System')
select_value = st.selectbox('Select movie from a dropdown', movies_list)


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda vector:vector[1])
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)

    return recommend_movie

if st.button('Show recommend'):
    movie_name = recommend(select_value) 
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.markdown(
        f"""<div style='border:1px dashed white;
        border-radius: 12px;
        padding: 6px;
        margin-bottom: 6px;
        width: fit-content;
        background-color: black;'>{movie_name[0]}</div>
        """,
        unsafe_allow_html=True
        )
    with col2:
        st.markdown(
        f"""<div style='border: 1px dashed white;
        border-radius: 12px;
        padding: 6px;
        margin-bottom: 6px;
        width: fit-content;
        background-color: black;'>{movie_name[1]}</div>""",
        unsafe_allow_html=True
        )
    with col3:
        st.markdown(
        f"""<div style='border:1px dashed white;
        border-radius: 12px;
        padding: 6px;
        margin-bottom: 6px;
        width: fit-content;
        background-color: black;'>{movie_name[2]}</div>""",
        unsafe_allow_html=True
        )
    with col4:
        st.markdown(
        f"""<div style='border:1px dashed white;
        border-radius: 12px;
        padding: 6px;
        margin-bottom: 6px;
        width: fit-content;
        background-color: black;'>{movie_name[3]}</div>""",
        unsafe_allow_html=True
        )
    with col5:
        st.markdown(
        f"""<div style='border:1px dashed white;
        border-radius: 12px;
        padding: 6px;
        margin-bottom: 6px;
        width: fit-content;
        background-color: black;'>{movie_name[4]}</div>""",
        unsafe_allow_html=True
        )

def set_bg_image(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html = True
    )

set_bg_image("img52.jpg")
