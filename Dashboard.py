import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define functions to create summaries
def create_daily_df_summary(df):
    daily_df_summary = df.describe().transpose()
    return daily_df_summary

def create_hourly_df_summary(df):
    hourly_df_summary = df.describe().transpose()
    return hourly_df_summary

# Load data
hour_df = pd.read_csv('https://raw.github.com/Gilbertfritzzz/Project/base/hour.csv')
day_df = pd.read_csv('https://raw.github.com/Gilbertfritzzz/Project/base/day.csv')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Merge data
bike_df = hour_df.merge(day_df, on='dteday', how='inner', suffixes=('_hour', '_day'))

# Sidebar
with st.sidebar:
    st.image("https://github.com/Gilbertfritzzz/Project/blob/base/6647729.jpg?raw=true", width=200)
    start_date_bike, end_date_bike = st.date_input(
        label='Rentang Waktu',
        min_value=bike_df["dteday"].min(),
        max_value=bike_df["dteday"].max(),
        value=(bike_df["dteday"].min(), bike_df["dteday"].max())
    )
    show_summary = st.checkbox("Tampilkan Summary")

# Filter data untuk bike_df
filtered_bike_df = bike_df[
    (bike_df["dteday"] >= pd.Timestamp(start_date_bike)) &
    (bike_df["dteday"] <= pd.Timestamp(end_date_bike))
]

# Prepare summaries
daily_df_summary = create_daily_df_summary(filtered_bike_df)
hourly_df_summary = create_hourly_df_summary(filtered_bike_df)

# Header
st.header('Bike Sharing Analysis:bike:')

# Visualizations
col1, col2 = st.columns(2)

with col1:
    # Daily average bike sharing
    rent_hr = (filtered_bike_df.groupby('hr')['cnt_hour'].mean())
    fig_rent, ax_rent = plt.subplots()
    ax_rent.bar(rent_hr.index, rent_hr.values)
    plt.xlabel('Hour')
    plt.ylabel('Bike Sharing Average')
    plt.title('Rata-rata Peminjaman Sepeda per Jam')
    st.pyplot(fig_rent)
    st.write("Grafik di atas menunjukkan rata-rata peminjaman sepeda per jam.")

with col2:
    # Bike sharing on holidays
    avg_holiday = filtered_bike_df.groupby('holiday_day')['cnt_day'].mean().reset_index().sort_values("cnt_day")
    fig_hld, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x='holiday_day', y='cnt_day', data=avg_holiday, palette='Set1', ax=ax)
    plt.xlabel('Day')
    plt.ylabel('Bike Sharing Average')
    plt.xticks([0, 1], ['Day', 'Holiday'])
    plt.title('Peminjaman Sepeda pada Hari Biasa dan Hari Libur')
    st.pyplot(fig_hld)
    st.write("Grafik di atas membandingkan rata-rata peminjaman sepeda antara hari biasa dan hari libur.")

# Data Summary
st.header('Data Summary')

if show_summary:
    st.subheader(f'Daily Summary {start_date_bike} - {end_date_bike}')
    
    # Calculate average bike rentals per day
    average_rentals_per_day = filtered_bike_df['cnt_day'].mean()
    st.write(f"Peminjaman sepeda per hari: {average_rentals_per_day}")

    # Calculated total based on selected date range
    total_rentals = filtered_bike_df['cnt_day'].sum()
    st.write(f"Total peminjaman sepeda dari {start_date_bike} hingga {end_date_bike}: {total_rentals}")

    st.subheader('Hourly Summary')
    # Calculate average bike rentals per hour and round to integer
    average_rentals_per_hour = filtered_bike_df.groupby('hr')['cnt_hour'].mean().round().astype(int)
    st.write("Rata-rata peminjaman sepeda per jam:")
    st.write(average_rentals_per_hour)

    st.subheader('Holiday Summary')
    # Calculate number of rentals on holidays and working days
    rentals_on_holidays = filtered_bike_df.loc[filtered_bike_df['holiday_day'] == 1, 'cnt_day'].sum()
    rentals_on_working_days = filtered_bike_df.loc[filtered_bike_df['holiday_day'] == 0, 'cnt_day'].sum()
    st.write(f"Jumlah peminjaman pada hari libur: {rentals_on_holidays}")
    st.write(f"Jumlah peminjaman pada hari kerja: {rentals_on_working_days}")
