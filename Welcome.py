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
  
location = st.selectbox("Select location", file_name_list)
df = pd.read_csv(location)
st.dataframe(df)

el_list = df.columns.tolist()[27:80]

col1, col2 = st.columns([3, 1])

col1.subheader("Data selection")
x_axis = col1.selectbox("Select element#1", el_list, index = 0)
y_axis = col2.selectbox("Select element#2", el_list, index = 0)

x = df[x_axis]/10000
y = df[y_axis]/10000
y_mean = np.mean(y)
x_min = np.min(x)
x_max = np.max(x)

x_center = 0.5*(x_min + x_max)
x_width = x_max - x_min

std_level = col1.radio("Select std level", ('1', '2', '3'))  
if std_level == "1":
  y_std = np.std(y) * 1.0
if std_level == "2":
  y_std = np.std(y) * 2.0
if std_level == "3":
  y_std = np.std(y) * 3.0

col2.subheader("Data chart")


p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.rect(x_center, y_mean, width = x_width, height = y_std, legend_label="Mean", line_width=0, fill_color = "lightgray")
p.circle(x, y, legend_label='Trend', line_width=5)
p.line([x_min, x_max], [y_mean, y_mean], legend_label="Mean", line_width=2)


col2.bokeh_chart(p, use_container_width=True)
