import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

file_name_list = []
for i in os.listdir():
  if i.endswith(".csv"):
    file_name_list.append(i)

#st.write(file_name_list)
  
#st.write("Hello world!")

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.multiselect("Select element", el_list, el_list[0])

st.multiselect("Select location", file_name_list)


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
