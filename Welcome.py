import streamlit as st
import pandas as pd
import os
#import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure

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
y_axis = st.selectbox("Select element", el_list)

st.multiselect("Select location", file_name_list)



x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

plt.scatter(df[x_axis]/10000, df[y_axis]/10000)

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.circle(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
