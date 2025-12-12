
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

# FASE 2.4: MEMBUAT DATASET SIMULASI UNIVERSITAS
np.random.seed(42)

# Data 5 tahun akademik (2019-2023)
tahun_akademik = [f"{2019+i}/{2020+i}" for i in range(5)]

# 8 Fakultas
fakultas = [
    'Teknik Informatika',
    'Teknik Sipil',
    'Ekonomi dan Bisnis',
    'Hukum',
    'Kedokteran',
    'Pendidikan',
    'Seni dan Desain',
    'Pertanian'
]

# Generate dataset simulasi
data_universitas = []

for tahun in tahun_akademik:
    tahun_num = int(tahun.split('/')[0])
    
    for fakultas_item in fakultas:
        # Baseline mahasiswa per fakultas
        baseline_map = {
            'Teknik Informatika': 450,
            'Teknik Sipil': 380,
            'Ekonomi dan Bisnis': 520,
            'Hukum': 320,
            'Kedokteran': 280,
            'Pendidikan': 410,
            'Seni dan Desain': 200,
            'Pertanian': 280
        }
        
        baseline = baseline_map[fakultas_item]
        
        # Simulasi pertumbuhan dengan noise
        trend = (tahun_num - 2019) * 30
        noise = np.random.normal(0, 20)
        jumlah_mahasiswa = int(baseline + trend + noise)
        
        # KPI lainnya
        dosen_aktif = int(jumlah_mahasiswa / 15) + np.random.randint(-5, 5)
        rata_ipk = round(np.random.normal(3.2, 0.3), 2)
        publikasi = int(dosen_aktif * 2) + np.random.randint(-3, 5)
        lulusan_tepat_waktu = np.random.randint(70, 95)
        
        data_universitas.append({
            'Tahun Akademik': tahun,
            'Fakultas': fakultas_item,
            'Jumlah Mahasiswa': jumlah_mahasiswa,
            'Dosen Aktif': dosen_aktif,
            'Rata-rata IPK': rata_ipk,
            'Publikasi Dosen': publikasi,
            'Lulusan Tepat Waktu (%)': lulusan_tepat_waktu
        })

df_universitas = pd.DataFrame(data_universitas)

print("✓ Dataset Simulasi Universitas Berhasil Dibuat")
print(f"\nJumlah Records: {len(df_universitas)}")
print(f"Periode: {tahun_akademik[0]} - {tahun_akademik[-1]}")
print(f"\nSample Data (5 baris pertama):")
print(df_universitas.head())

# Simpan untuk digunakan di Streamlit
df_universitas.to_csv('data_universitas.csv', index=False)
print("\n✓ Data berhasil disimpan ke 'data_universitas.csv'")
