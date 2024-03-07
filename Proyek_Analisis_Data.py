import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv('/day.csv')
hour_df = pd.read_csv('/hour.csv')

# merge
bike_df = hour_df.merge(day_df, on='dteday', how='inner', suffixes=('_hour', '_day'))

# Plot 1: Hourly Rental
rent_hr = bike_df.groupby('hr')['cnt_hour'].mean()

# Streamlit code for Plot 1
st.bar_chart(rent_hr)

st.title('Rata - Rata Penyewaan Sepeda per Jam')
st.xlabel('Jam')
st.ylabel('Rata - Rata Penyewaan')

# Plot 2: Daily Rental on Holidays
avg_holiday = bike_df.groupby('holiday_day')['cnt_day'].mean().reset_index().sort_values("cnt_day")

# Streamlit code for Plot 2
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='holiday_day', y='cnt_day', data=avg_holiday, palette='Set1', ax=ax)

st.pyplot(fig)

st.title('Rata-rata Penyewaan Sepeda pada Hari Libur')
st.xlabel('Hari Libur')
st.ylabel('Rata-rata Penyewaan')
st.xticks([0, 1], ['Tidak Libur', 'Libur'])
