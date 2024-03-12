import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_daily_df_summary(df):
    daily_df_summary = df.describe().transpose()
    return daily_df_summary

def create_hourly_df_summary(df):
    hourly_df_summary = df.describe().transpose()
    return hourly_df_summary

# Load data
hour_df = pd.read_csv('C:\Project\submission\dashboard\hour.csv')
day_df = pd.read_csv('C:\Project\submission\dashboard\day.csv')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
# Merge data
bike_df = hour_df.merge(day_df, on='dteday', how='inner', suffixes=('_hour', '_day'))

# Filter Data
min_date_bike = bike_df["dteday"].min()
max_date_bike = bike_df["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil rentang data untuk bike_df
    start_date_bike, end_date_bike = st.date_input(
        label='Rentang Data (bike_df)',
        min_value=pd.Timestamp(min_date_bike),
        max_value=pd.Timestamp(max_date_bike),
        value=(pd.Timestamp(min_date_bike), pd.Timestamp(max_date_bike))
    )

# Convert tuple values to Timestamp
start_date_bike = start_date_bike
end_date_bike = end_date_bike

# Filter data untuk bike_df
filtered_bike_df = bike_df[
    (bike_df["dteday"] >= pd.Timestamp(start_date_bike)) &
    (bike_df["dteday"] <= pd.Timestamp(end_date_bike))
]

# Menyiapkan berbagai dataframe
daily_df_summary = create_daily_df_summary(filtered_bike_df)
hourly_df_summary = create_hourly_df_summary(filtered_bike_df)

st.header('Bike Sharing Exploratory Data Analysis :bike:')
col1, col2 = st.columns(2)

with col1:
    rent_hr = (filtered_bike_df.groupby('hr')['cnt_hour'].mean())
    fig_rent, ax_rent = plt.subplots()
    ax_rent.bar(rent_hr.index, rent_hr.values)
    plt.xlabel('Hour')
    plt.ylabel('Bike Sharing Average')
    st.subheader('Bike Sharing Average Per Hour')
    st.pyplot(fig_rent)

with col2:
    avg_holiday = filtered_bike_df.groupby('holiday_day')['cnt_day'].mean().reset_index().sort_values("cnt_day")
    fig_hld, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x='holiday_day', y='cnt_day', data=avg_holiday, palette='Set1', ax=ax)
    plt.xlabel('Day')
    plt.ylabel('Bike Sharing Average')
    plt.xticks([0, 1], ['Day', 'Holiday'])
    st.subheader('Bike Sharing in holiday')
    st.pyplot(fig_hld)
