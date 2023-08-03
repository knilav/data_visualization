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

x_axis = st.selectbox("Select element#1", el_list, index = 0)
y_axis = st.selectbox("Select element#2", el_list, index = 0)

x = df[x_axis]/10000
y = df[y_axis]/10000
y_mean = np.mean(y)
y_std = np.std(y)

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.circle(x, y, legend_label='Trend', line_width=5)
p.line([np.min(x), np.max(x)], [y_mean, y_mean], legend_label="Mean", line_width=2)
#p.rect(x, y, legend_label="Mean", line_width=2)

st.bokeh_chart(p, use_container_width=True)
