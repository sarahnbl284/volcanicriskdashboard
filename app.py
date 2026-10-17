import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_folium import st_folium
import folium
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Volcanic Eruption Risk Dashboard", page_icon="🌋", layout="wide")

# Judul
st.title("🌋 Volcanic Eruption Risk Dashboard")
st.write("Dashboard analisis statistik dan risiko erupsi gunung berapi.")

# Membaca dataset
df = pd.read_csv("data/volcanic_eruptions_clean.csv")

# Sidebar untuk filter
st.sidebar.header("Filter Data")
selected_country = st.sidebar.selectbox("Pilih Negara", df['country'].unique())
year_range = st.sidebar.slider(
    "Pilih Rentang Tahun",
    int(df['year'].min()),
    int(df['year'].max()),
    (int(df['year'].min()), int(df['year'].max()))
)   

# Mengfilter data berdasarkan pilihan
filtered_df = df[(df['country'] == selected_country) & (df['year'].between(year_range[0], year_range[1]))]

# Menampilkan data
st.subheader("📊 Data Erupsi Gunung Berapi")
st.write("Jumlah data:", len(filtered_df))
st.dataframe(filtered_df)


# Menghitung KPI
total_erupsi = filtered_df.shape[0]
total_negara = df['country'].nunique()
rata_rata_vei = filtered_df['vei'].mean()
total_damage = filtered_df['total_damage_mil'].sum()

# Menampilkan KPI
st.subheader("📊 Key Performance Indicators (KPI)")
kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
with kpi1:
    st.metric(label="Total Erupsi", value=total_erupsi)

with kpi2:
    st.metric(label="Total Negara", value=total_negara)

with kpi3:
    st.metric(label="Rata-rata VEI", value=round(rata_rata_vei, 2))

with kpi4:
    st.metric(label="Total Damage", value=f"${total_damage:,.0f} juta")


with kpi5:
    if total_damage == 0:
        st.metric(label="Status Kerugian", value="Tidak Ada")
    else:
        st.metric(label="Status Kerugian", value="Tersedia")
# Menghitung jumlah erupsi per tahun
erupsi_per_tahun = filtered_df['year'].value_counts().reset_index()
erupsi_per_tahun.columns = ['Tahun', 'Jumlah Erupsi']
erupsi_per_tahun = erupsi_per_tahun.sort_values(by='Tahun')

# Menampilkan grafik tren erupsi
st.subheader("📈 Grafik Tren Erupsi")
fig = px.line(erupsi_per_tahun, x='Tahun', y='Jumlah Erupsi', title='Jumlah Erupsi per Tahun')
st.plotly_chart(fig)


# Menampilkan distribusi VEI
st.subheader("📊 Distribusi VEI")
fig_vei = px.histogram(filtered_df, x='vei', nbins=30, title='Distribusi VEI', labels={'vei': 'VEI'})
st.plotly_chart(fig_vei)

# Mengonversi kolom latitude dan longitude menjadi tipe data numerik
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
df = df.dropna(subset=['latitude', 'longitude'])

# Membuat peta
st.subheader("🌍 Peta Lokasi Erupsi")
peta = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=2)

# Menambahkan titik lokasi erupsi ke peta
for _, row in df.iterrows():
    folium.CircleMarker(
        location=(row['latitude'], row['longitude']),
        radius=5,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6,
        popup=row['country']
    ).add_to(peta)

# Menggunakan st_folium untuk menampilkan peta
st_folium(peta, width=700)


# Analisis Kerugian Ekonomi

# # Contoh DataFrame
# data = {
#     'country': ['Indonesia', 'United States', 'Japan', 'Ecuador', 'Brazil'],
#     'total_damage_mil': [970, 386, 200, 150, 300]
# }
# df = pd.DataFrame(data)

# st.subheader("💰 Analisis Kerugian Ekonomi")

# # Mengelompokkan dan menjumlahkan total kerugian berdasarkan negara
# kerugian_ekonomi = df.groupby('country')['total_damage_mil'].sum().reset_index()
# kerugian_ekonomi = kerugian_ekonomi.sort_values(by='total_damage_mil', ascending=False)

# # Menampilkan tabel
# st.table(kerugian_ekonomi)

# # Membuat grafik
# plt.figure(figsize=(10, 6))
# plt.bar(kerugian_ekonomi['country'], kerugian_ekonomi['total_damage_mil'], color='blue')
# plt.xlabel('Negara')
# plt.ylabel('Total Kerugian (juta dolar)')
# plt.title('Total Kerugian Ekonomi per Negara')
# plt.xticks(rotation=45)
# plt.tight_layout()
# st.pyplot(plt)

st.subheader("💰 Analisis Kerugian Ekonomi")
kerugian_ekonomi = df.groupby('country')['total_damage_mil'].sum().reset_index()
kerugian_ekonomi = kerugian_ekonomi.sort_values(by='total_damage_mil', ascending=False)

# Menampilkan grafik batang untuk total kerugian per negara
fig_kerugian = px.bar(kerugian_ekonomi, x='country', y='total_damage_mil', title='Total Kerugian Ekonomi per Negara', labels={'total_damage_mil': 'Total Kerugian (juta $)'})
st.plotly_chart(fig_kerugian)

# Risk Assessment
st.subheader("⚠️ Risk Assessment")
bins = [0, 100, 500, 1000, float('inf')]
labels = ['Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
df['risk_category'] = pd.cut(df['total_damage_mil'], bins=bins, labels=labels)
risk_assessment = df['risk_category'].value_counts().reset_index()
risk_assessment.columns = ['Kategori Risiko', 'Jumlah']
st.dataframe(risk_assessment)

# Menampilkan grafik batang untuk negara berdasarkan kategori risiko
st.subheader("📊 Negara Berdasarkan Kategori Risiko")
risk_country = df.groupby(['country', 'risk_category']).size().reset_index(name='Jumlah')
fig_risk_country = px.bar(risk_country, x='country', y='Jumlah', color='risk_category', 
                           title='Jumlah Negara Berdasarkan Kategori Risiko', 
                           labels={'Jumlah': 'Jumlah Negara', 'risk_category': 'Kategori Risiko'})
st.plotly_chart(fig_risk_country)

# Menampilkan grafik pie untuk distribusi kategori risiko
st.subheader("📊 Distribusi Kategori Risiko")
fig_risk = px.pie(risk_assessment, names='Kategori Risiko', values='Jumlah', title='Distribusi Kategori Risiko')
st.plotly_chart(fig_risk)


# Menampilkan Ringkasan
st.subheader("📋 Ringkasan/Kesimpulan")
st.write(f"Total erupsi untuk negara **{selected_country}** dari tahun **{year_range[0]}** hingga **{year_range[1]}** adalah **{total_erupsi}**.")
st.write(f"Rata-rata VEI selama periode ini adalah **{round(rata_rata_vei, 2)}**.")
st.write(f"Total kerugian yang tercatat adalah **${total_damage:,.0f} juta**.")

# Tombol untuk mengunduh data
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Unduh Data", csv, "data_filtered.csv", "text/csv")