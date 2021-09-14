import streamlit as st
import pickle
import pandas as pd
import requests

movies = pd.read_csv("df1.csv")
st.title('Movie Recommender System')

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=92ee31384256e920cf3fb87e3f98de66&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similar[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:6]
  recommended_movies = []
  recommended_movies_posters = []
  for i in movies_list:
    movie_ids = movies.iloc[i[0]].movie_id
    recommended_movies.append(movies.iloc[i[0]].title)
    recommended_movies_posters.append(fetch_poster(movie_ids))
  return recommended_movies,recommended_movies_posters


similar = pickle.load(open('similar.pkl','rb'))

select_movie_name = st.selectbox("Hey There!", movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(select_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

