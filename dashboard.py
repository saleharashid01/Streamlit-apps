import streamlit as st
import seaborn as sns
import pandas as pd

st.header("This app is made by Saleha Rashid")
st.text('This App is all about Iris Dataset from Seaborn library ')

st.header ( "Lets Explore this data"  )
df=sns.load_dataset('iris')
st.write(df[['species', 'sepal_length', 'petal_length']] .head(8))

st.bar_chart(df['sepal_length'])
st.line_chart(df['sepal_length'])