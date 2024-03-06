import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


day_df = pd.read_csv('/day.csv')
day_df.head()

hour_df = pd.read_csv('/hour.csv')
hour_df.head()

rent_hr = bike_df.groupby('hr')['cnt_hour'].mean()

plt.bar(rent_hr.index, rent_hr.values)

plt.title('Rata - Rata Penyewaan Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Rata - Rata Penyewaan')

plt.show()


avg_holiday = bike_df.groupby('holiday_day')['cnt_day'].mean().reset_index().sort_values("cnt_day")

plt.figure(figsize=(8, 5))
sns.barplot(x='holiday_day', y='cnt_day', data=avg_holiday, palette='Set1')

plt.title('Rata-rata Penyewaan Sepeda pada Hari Libur')
plt.xlabel('Hari Libur')
plt.ylabel('Rata-rata Penyewaan')
plt.xticks([0, 1], ['Tidak Libur', 'Libur'])

plt.show()
