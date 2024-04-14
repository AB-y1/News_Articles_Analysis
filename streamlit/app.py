import streamlit as st
import pandas as pd
st.title('News Articale Analysis')
st.text('this is the news data')
news = pd.read_csv(r"C:\Users\HP\Downloads\week00_data\data.csv")
st.header('news data')
st.write(news['category', 'title'].head(5))