import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
movies=pd.DataFrame(pickle.load(open("movies.pkl","rb")))
similarity=pickle.load(open("similarity.pkl","rb"))

def getposter(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=0bc2023b07424bf03c8771248ab1dbf3&language=en-US".format(movie_id))
    return response.json()["poster_path"]

def recommand(movie):
     movie_index = movies[movies["title"] == movie].index[0]
     distances = similarity[movie_index]
     enum_movies = list(enumerate(distances))
     sorted_movies = sorted(enum_movies, reverse=True, key=lambda x: x[1])[1:5]

     recommand_movies=[]
     for i in sorted_movies:
          dic={}
          dic["poster"]=getposter(movies.iloc[i[0]].id)
          dic["title"]=movies.iloc[i[0]].title
          recommand_movies.append(dic)

     return  recommand_movies


st.title('Movie Recommendation Engine Made By Rabi Subedi Chettri')

option = st.selectbox('Select A Movie',movies.title)

if st.button('Recommend'):

     recommand_movies=recommand(option)

     col1, col2, col3,col4 = st.columns(4)

     with col1:
          st.text(recommand_movies[0]["title"])
          st.image("https://www.themoviedb.org/t/p/w500"+recommand_movies[0]["poster"])

     with col2:
          st.text(recommand_movies[1]["title"])
          st.image("https://www.themoviedb.org/t/p/w300_and_h450_bestv2"+recommand_movies[1]["poster"])

     with col3:
          st.text(recommand_movies[2]["title"])
          st.image("https://www.themoviedb.org/t/p/w300_and_h450_bestv2"+recommand_movies[2]["poster"])

     with col4:
          st.text(recommand_movies[3]["title"])
          st.image("https://www.themoviedb.org/t/p/w300_and_h450_bestv2"+recommand_movies[3]["poster"])

