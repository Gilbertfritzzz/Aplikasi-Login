import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv('/day.csv')
hour_df = pd.read_csv('/hour.csv')

# Plot 1: Hourly Rental
rent_hr = hour_df.groupby('hr')['cnt_hour'].mean()

st.bar_chart(rent_hr)

st.title('Rata - Rata Penyewaan Sepeda per Jam')

# Plot 2: Daily Rental on Holidays
avg_holiday = day_df.groupby('holiday_day')['cnt_day'].mean().reset_index().sort_values("cnt_day")

plt.figure(figsize=(8, 5))
sns.barplot(x='holiday_day', y='cnt_day', data=avg_holiday, palette='Set1')

st.title('Rata-rata Penyewaan Sepeda pada Hari Libur')
st.bar_chart(avg_holiday.set_index('holiday_day'))

# Display the Streamlit app
st.show()
