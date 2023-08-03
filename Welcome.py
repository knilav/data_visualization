import streamlit as st
import pandas as pd

st.write("Hello world!")

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)
