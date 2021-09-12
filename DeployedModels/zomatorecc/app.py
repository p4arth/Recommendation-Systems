import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(layout="wide")

df = pd.read_csv("df.csv")
st.title('Restaurant Recommender System')
rest1 = pd.read_csv("rest1.csv")

def get_details(restaurant):
  restaurant_index = df[df['rest_name'] == restaurant].index[0]
  distances = similar[restaurant_index]
  rest_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:7]
  cat_list = []
  for rest in rest_list:
    cat_list.append(rest1.iloc[rest[0]].Category)
  return cat_list

def recommend(restaurant):
  restaurant_index = df[df['rest_name'] == restaurant].index[0]
  distances = similar[restaurant_index]
  rest_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:7]
  recom_rest = []
  for i in rest_list:
      recom_rest.append(df.iloc[i[0]].rest_name)
  return recom_rest

select_rest_name = st.selectbox('Choose A Restaurant Name', df['rest_name'])

similar = pickle.load(open('similar.pkl','rb'))

if st.button('Recommend'):
    names = recommend(select_rest_name)
    details = get_details(select_rest_name)
    col1,col2,col3 = st.columns(3)
    st.container()
    with col1:
        st.text('Restaurant Name: '+names[0])
        try:
            st.text('CATEGORY: '+details[0])
        except:
            pass
        st.container()
    with col1:
        st.text('Restaurant Name: '+names[1])
        try:
            st.text('CATEGORY: '+details[1])
        except:
            pass
        st.container()
    with col2:
        st.text('Restaurant Name: '+names[2])
        try:
            st.text('CATEGORY: '+details[2])
        except:
            pass
        st.container()
    with col2:
        st.text('Restaurant Name: '+names[3])
        try:
            st.text('CATEGORY: '+details[3])
        except:
            pass
        st.container()
    with col3:
        st.text('Restaurant Name: '+names[4])
        try:
            st.text('CATEGORY: '+details[4])
        except:
            pass
        st.container()
    with col3:
        st.text('Restaurant Name: '+names[5])
        try:
            st.text('CATEGORY: '+details[5])
        except:
            pass
        st.container()
    
        
        
        
        
        