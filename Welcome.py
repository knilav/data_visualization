import streamlit as st
import pandas as pd
import os

file_name_list = []
for i in os.listdir():
  if i.endswith(".csv"):
    file_name_list.append(i)

#st.write(file_name_list)
  
#st.write("Hello world!")

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox("Select element", el_list)

st.multiselect("Select location", file_name_list)
