import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# merge data
bike_df = hour_df.merge(day_df, on='dteday', how='inner', suffixes=('_hour', '_day'))

# Visualization
st.title('Bike Sharing Exploratory Data Analysis :bike:')
col1, col2 = st.columns(2)

with col1:
    rent_hr = bike_df.groupby('hr')['cnt_hour'].mean()
    fig_rent, ax_rent = plt.subplots()
    ax_rent.bar(rent_hr.index, rent_hr.values)
    plt.xlabel('Hour')
    plt.ylabel('Bike Sharing Average')
    st.subheader('Bike Sharing Average Per Hour')
    st.pyplot(fig_rent)

with col2:
    avg_holiday = bike_df.groupby('holiday_day')['cnt_day'].mean().reset_index().sort_values("cnt_day")
    fig_hld, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x='holiday_day', y='cnt_day', data=avg_holiday, palette='Set1', ax=ax)
    plt.xlabel('Day')
    plt.ylabel('Bike Sharing Average')
    plt.xticks([0, 1], ['Day', 'Holiday'])
    st.subheader('Bike Sharing in holiday')
    st.pyplot(fig_hld)
