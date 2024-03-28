import streamlit as st
import pandas as pd

st.title("Website Developing using Python")
st.header("🐡 Website Developing using Python 🐡")
st.subheader("🐡 Teerapat Buapradit 🐡")
st.image('cat.jpg')

st.subheader('Data IRIS Flower 🌺')
dt=pd.read_csv('./data/iris.csv')
st.write(dt.head(10))

st.subheader('Statistics IRIS Flower 🌵')
st.write('Summery')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].sum())
cl2.write(dt['sepal.width'].sum())
cl3.write(dt['petal.leagth'].sum())
cl4.write(dt['petal.wigth'].sum())

st.write('X Bar')
st.write('Max')
st.write('Min')