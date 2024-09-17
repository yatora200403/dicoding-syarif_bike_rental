import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os
from datetime import datetime

cwd = os.getcwd()
hour_path = os.path.join(cwd, "dashboard", "hour_cleaned.csv")
day_path = os.path.join(cwd, "dashboard", "day_cleaned.csv")
hour_df = pd.read_csv(hour_path)
day_df = pd.read_csv(day_path)

min_date = datetime.strptime(day_df.date.min(), '%Y-%m-%d')
max_date = datetime.strptime(day_df.date.max(), '%Y-%m-%d')

with st.sidebar:
    st.image('https://github.com/dicodingacademy/assets/raw/main/logo.png')
    st.date_input(
        label="Rentan Waktu", 
        min_value=min_date,
        max_value=max_date,
        value=[min_date,max_date]
    )

st.header("Syarif's Bike Rental :bike:")
#Syarif's Bike Rental Perfomance 2011-2012
st.subheader("Syarif's Bike Rental Perfomance 2011-2012")
day_df['month'] = pd.Categorical(
    day_df['month'], 
    categories=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    ordered=True    
)
fig, ax = plt.subplots(figsize=(16, 8))
monthly = day_df.groupby(by=['month', 'year']).agg({
    'count':'sum'
}).reset_index()

sns.lineplot(
    data=monthly,
    x='month',
    y='count',
    hue='year',
    palette='dark',
    marker='o',
    ax=ax
)
ax.set_title("Trend Rental Sepeda Pada Tahun 2011-2012", loc="center", fontsize=30)
ax.set_xlabel(None)
ax.set_ylabel("rata - rata penyewa sepeda")
ax.legend(title="Tahun", loc='upper right')
st.pyplot(fig)

#Workingday and Holiday Customer Comparison
st.subheader("Workingday and Holiday Customer Comparison")
fig, ax = plt.subplots(figsize=(16,8))
sns.barplot(
    x='workingday',
    y='count',
    data=day_df,
    palette='dark')

ax.set_title('Perbandingan Penyewa Sepeda Workingday Dan Holiday', loc="center", fontsize=30)
ax.set_xlabel(None)
ax.set_ylabel('Jumlah Penyewa Sepeda')
st.pyplot(fig)

st.caption("Copyright (c) Syarif's Bike Rental")