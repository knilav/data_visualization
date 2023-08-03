import streamlit as st
import pandas as pd

st.write("Hello world!")

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.to_list()[27:80]

st.selectbox("Select element", el_list)
