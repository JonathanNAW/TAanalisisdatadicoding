import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from matplotlib.ticker import FuncFormatter

day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')
day_df['mnth'] = day_df['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_df['weathersit'] = day_df['weathersit'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

day_df['yr'] = day_df['yr'].map({
    0: '2011', 1: '2012'
})

day_df['workingday'] = day_df['workingday'].map({
    0: 'Holiday', 1: 'Workingday'
})

day_df['holiday'] = day_df['holiday'].map({
    0: 'No Holiday', 1: 'Holiday'
})

# Mengubaha tipe data ke categorical
day_df['season'] = day_df.season.astype('category')
day_df['yr'] = day_df.yr.astype('category')
day_df['mnth'] = day_df.mnth.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['weathersit'] = day_df.weathersit.astype('category')

hour_df['mnth'] = hour_df['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
hour_df['season'] = hour_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
hour_df['weekday'] = hour_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
hour_df['weathersit'] = hour_df['weathersit'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

hour_df['yr'] = hour_df['yr'].map({
    0: '2011', 1: '2012'
})

hour_df['workingday'] = hour_df['workingday'].map({
    0: 'Holiday', 1: 'Workingday'
})

hour_df['holiday'] = hour_df['holiday'].map({
    0: 'No Holiday', 1: 'Holiday'
})

day_df.groupby('season').agg({
    'casual': ['mean', 'sum'],
    'registered': ['mean', 'sum'],
    'cnt': ['mean', 'sum']
}).reindex (['Spring', 'Summer', 'Fall', 'Winter',])

day_df.groupby(by='weathersit').agg({
    'casual': ['mean', 'sum'],
    'registered': ['mean', 'sum'],
    'cnt': ['mean', 'sum']
})



# Aplikasi Streamlit
st.title("Bike Sharing Data Analysis")

# --- Foto Pertama: Penyewa Sepeda Berdasarkan Musim ---
st.header("Rata-Rata Penyewa Sepeda Berdasarkan Musim")
season_pattern = day_df.groupby('season')[['registered', 'casual']].mean().reset_index()

# Membuat figure dengan ukuran 10x6
fig, ax = plt.subplots(figsize=(10, 6))

# Menentukan lebar bar
bar_width = 0.35
index = np.arange(len(season_pattern))

# Membuat bar plot untuk data penyewa 'registered'
ax.bar(index, season_pattern['registered'], width=bar_width, label='Registered')

# Membuat bar plot untuk data penyewa 'casual', dengan offset
ax.bar(index + bar_width, season_pattern['casual'], width=bar_width, label='Casual')

# Menambahkan label pada sumbu X dan Y
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penyewa (Rata-Rata)')
ax.set_title('Rata-Rata Penyewa Sepeda Berdasarkan Musim')

# Menampilkan legenda
ax.legend()

# Mengubah label pada sumbu X menjadi nama musim
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(season_pattern['season'])

# Menampilkan plot di Streamlit
st.pyplot(fig)

st.write("Penyewaan sepeda paling banyak dilakukan pada musim gugur (Fall).")
st.write("Sedangkan penyewaan sepeda paling sedikit dilakukan pada musim semi (spring).")

# --- Foto Kedua: Penyewa Berdasarkan Kondisi Cuaca ---
st.header("Rata-rata Penyewa Sepeda Berdasarkan Kondisi Cuaca")
weathersit_pattern = day_df.groupby('weathersit')[['registered', 'casual']].mean().reset_index()

# Mengatasi missing kategori
# Pastikan ada 4 kategori cuaca (Clear, Misty, Light Snow, Severe Weather)
complete_weathersit = pd.DataFrame({
    'weathersit': ['Clear/Partly Cloudy', 'Misty/Cloudy', 'Light Snow/Rain', 'Severe Weather']
})
# Gabungkan dengan data asli
weathersit_pattern = complete_weathersit.merge(weathersit_pattern, on='weathersit', how='left').fillna(0)

# Membuat figure baru
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Menentukan lebar bar
bar_width = 0.35
index = np.arange(len(weathersit_pattern))

# Membuat bar plot untuk data penyewa 'registered'
ax2.bar(index, weathersit_pattern['registered'], width=bar_width, label='Registered')

# Membuat bar plot untuk data penyewa 'casual', dengan offset
ax2.bar(index + bar_width, weathersit_pattern['casual'], width=bar_width, label='Casual')

# Menambahkan label pada sumbu X dan Y
ax2.set_xlabel('Kondisi Cuaca')
ax2.set_ylabel('Jumlah Penyewa (Rata-Rata)')
ax2.set_title('Rata-Rata Penyewa Sepeda Berdasarkan Kondisi Cuaca')

# Menambahkan legenda
ax2.legend()

# Mengubah label pada sumbu X menjadi kondisi cuaca
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(weathersit_pattern['weathersit'])

# Menampilkan plot di Streamlit
st.pyplot(fig2)

st.write("Penyewaan sepeda paling banyak dilakukan pada kondisi cuaca cerah (clear).")
st.write("Sedangkan penyewaan sepeda paling sedikit dilakukan pada kondisi cuaca salju ringan (light snow).")
st.write("Tidak ada penyewaan sepeda yang dilakukan pada saat kondisi cuaca buruk (severe weather).")

# --- Foto Ketiga: Analisis RFM ---
st.header("Analisis Lanjutan (RFM)")

# Mengubah kolom dteday menjadi tipe datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Menghitung Recency untuk casual dan registered
last_date = day_df['dteday'].max()

# Menghitung Recency
recency_casual = (last_date - day_df['dteday']).min().days  # Recency untuk casual
recency_registered = (last_date - day_df['dteday']).min().days  # Recency untuk registered

# Menghitung Frequency untuk casual dan registered
frequency_casual = day_df['casual'].sum()  # Total penyewaan casual
frequency_registered = day_df['registered'].sum()  # Total penyewaan registered

# Menghitung Monetary untuk casual dan registered
price_per_rental = 5  # Asumsi: setiap penyewaan dihargai $5
monetary_casual = frequency_casual * price_per_rental
monetary_registered = frequency_registered * price_per_rental

# Membuat DataFrame untuk RFM
rfm_data = {
    'Segment': ['Casual', 'Registered'],
    'Recency': [recency_casual, recency_registered],
    'Frequency': [frequency_casual, frequency_registered],
    'Monetary': [monetary_casual, monetary_registered]
}

rfm_df = pd.DataFrame(rfm_data)

# Fungsi untuk format angka
def format_func(value, tick_number):
    return f'{int(value):,}'  # Format angka dengan koma

# Membuat visualisasi Frequency dan Monetary
fig3, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 6))

# Visualisasi Frequency
sns.barplot(x='Segment', y='Frequency', data=rfm_df, palette='viridis', ax=ax3)
ax3.set_title('Frequency by Segment')
ax3.set_xlabel('Segment')
ax3.set_ylabel('Frequency')
ax3.yaxis.set_major_formatter(FuncFormatter(format_func))
ax3.grid(axis='y')

# Menambahkan anotasi pada batang
for p in ax3.patches:
    ax3.annotate(f'{int(p.get_height()):,}', (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='bottom')

# Visualisasi Monetary
sns.barplot(x='Segment', y='Monetary', data=rfm_df, palette='viridis', ax=ax4)
ax4.set_title('Monetary by Segment')
ax4.set_xlabel('Segment')
ax4.set_ylabel('Monetary')
ax4.yaxis.set_major_formatter(FuncFormatter(format_func))
ax4.grid(axis='y')

# Menambahkan anotasi pada batang
for p in ax4.patches:
    ax4.annotate(f'${int(p.get_height()):,}', (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='bottom')

plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(fig3)

st.write("Frequency untuk Penyewa Casual: 620017. Sedangkan untuk penyewa Registered: 2672662")
st.write("Monetary untuk Penyewa Casual: 3100085. Sedangkan untuk penyewa Registered: 13363310")
