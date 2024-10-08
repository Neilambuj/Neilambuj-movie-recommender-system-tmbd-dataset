from http.client import responses

import streamlit as st
import pickle
import pandas as pd
import requests

# def fetch_poster(movie_id):
#     url = ('https://api.themoviedb.org/3/movie/{}?api_key=5a79f65a9fae776802c7e86d46492608&language=en-US'.format(movie_id))
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    # recommended_movies_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.header('Movie Recommender System')

selected_movie_name = st.selectbox(
"Type or select a movie from the dropdown",
(movies['title'].values))

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)


    # col1, col2, col3, col4, col5 = st.beta_columns(5)
    # with col1:
    #     st.header(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.header(names[1])
    #     st.image(posters[1])
    # with col3:
    #     st.header(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.header(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.header(names[4])
    #     st.image(posters[4])