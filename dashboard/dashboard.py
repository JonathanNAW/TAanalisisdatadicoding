import streamlit as st

# Judul aplikasi
st.title("Bike Sharing Data Analysis")

# Menampilkan Foto Pertama
st.header("Rata-Rata Penyewa Sepeda Berdasarkan Musim")
st.image("dashboard/foto1.jpg", use_column_width=True)
st.write("Penyewaan sepeda paling banyak dilakukan pada musim gugur (Fall). Sementara paling sedikit dilakukan pada musim semi (spring).")
st.write("Rata-rata penyewaan sepeda pada musim gugur berjumlah 5644.")
st.write("Rata-rata penyewaan sepeda pada musim panas berjumlah 4992.")
st.write("Rata-rata penyewaan sepeda pada musim dingin berjumlah 4728.")
st.write("Rata-rata penyewaan sepeda pada musim semi berjumlah 2604.")
# Menampilkan Foto Kedua
st.header("Rata-rata Penyewa Sepeda Berdasarkan Kondisi Cuaca")
st.image("dashboard/foto2.jpg", use_column_width=True)
st.write("Penyewaan sepeda paling banyak dilakukan pada kondisi cuaca cerah (clear). Sementara paling sedikit dilakukan pada kondisi cuaca salju ringan (light snow). Dan tidak ada penyewaan sepeda pada saat cuaca buruk (severe weather)")
st.write("Rata-rata penyewaan sepeda pada kondisi cuaca cerah berjumlah 4876.")
st.write("Rata-rata penyewaan sepeda pada kondisi cuaca berkabut berjumlah 4035.")
st.write("Rata-rata penyewaan sepeda pada kondisi cuaca salju ringan berjumlah 1803.")
# Menampilkan Foto Ketiga
st.header("Analisis Lanjutan (RFM)")
st.image("dashboard/foto3.jpg", use_column_width=True)
st.write("Frequency untuk Penyewa Casual: 620017. Sedangkan untuk Penyewa Registered: 2672662")
st.write("Monetary untuk Penyewa Casual: 3100085. Sedangkan untuk Penyewa Registered: 13363310")
