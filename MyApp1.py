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
st.write('X Bar')
st.write('Max')
st.write('Min')