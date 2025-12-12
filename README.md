# Dashboard Universitas

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

## Deskripsi Proyek

Dashboard Universitas adalah aplikasi berbasis web yang dirancang untuk mendukung pengambilan keputusan strategis oleh rektorat dan pimpinan universitas. Dashboard ini menyajikan informasi akademik dan operasional secara real-time dengan visualisasi data yang interaktif.

### Pengguna Utama
- **Rektorat & Pimpinan Universitas**: Untuk monitoring performa akademik dan operasional
- **Dekan**: Untuk analisis kinerja fakultas masing-masing
- **Bagian Akademik**: Untuk perencanaan dan evaluasi program studi

## Fitur Utama

### 1. **Visualisasi Data Interaktif**
   - **Bar Chart**: Distribusi jumlah mahasiswa per fakultas
   - **Line Chart**: Tren pertumbuhan mahasiswa selama 5 tahun akademik
   - **Box Plot**: Analisis distribusi kelulusan tepat waktu
   - **Horizontal Bar Chart**: Total publikasi dosen per fakultas

### 2. **Komponen Interaktif**
   - **Filter Tahun Akademik**: Multiselect untuk periode analisis
   - **Filter Fakultas**: Pilih satu atau lebih fakultas untuk deep-dive analysis
   - **Summary Metrics**: Dashboard dengan 4 KPI utama

### 3. **Indikator Utama (KPI)**
   - Total Mahasiswa Aktif
   - Total Dosen Aktif
   - Rata-rata IPK
   - Presentase Lulusan Tepat Waktu

### 4. **Data yang Ditampilkan**
   - Jumlah Mahasiswa per Fakultas
   - Jumlah Dosen Aktif
   - Rata-rata IPK
   - Publikasi Dosen
   - Kelulusan Tepat Waktu (%)
   - Tren 5 tahun akademik (2019/2020 - 2023/2024)

## Teknologi yang Digunakan

| Teknologi | Versi | Fungsi |
|-----------|-------|--------|
| **Python** | 3.8+ | Bahasa pemrograman utama |
| **Streamlit** | 1.0+ | Framework web application |
| **Pandas** | 1.3+ | Data manipulation & analysis |
| **Plotly** | 5.0+ | Interactive data visualization |
| **NumPy** | 1.20+ | Numerical computing |

## Instalasi & Setup

### Prerequisites
```bash
- Python 3.8 atau lebih tinggi
- pip (Python package installer)
- Git
```

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd dashboard-universitas
```

### Step 2: Buat Virtual Environment (Opsional tapi Disarankan)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Jalankan Aplikasi
```bash
streamlit run app.py
```

Aplikasi akan membuka di browser pada `http://localhost:8501`

## Struktur File

```
dashboard-universitas/
├── app.py                    # Main application file
├── data_universitas.csv      # Dataset simulasi universitas
├── requirements.txt          # Python dependencies
├── README.md                 # Dokumentasi proyek
└── laporan_analisis.md       # Laporan evaluasi dashboard
```

## Dataset

### Sumber Data
Dataset adalah simulasi yang dibuat untuk keperluan akademik, mencakup:
- **Periode**: 5 Tahun Akademik (2019/2020 - 2023/2024)
- **Jumlah Fakultas**: 8 Fakultas
- **Records**: 40 data points (8 fakultas × 5 tahun)

### Metrik yang Tersedia
1. **Jumlah Mahasiswa**: Mahasiswa aktif per fakultas per tahun
2. **Dosen Aktif**: Jumlah dosen pengajar
3. **Rata-rata IPK**: Indeks Prestasi Kumulatif mahasiswa
4. **Publikasi Dosen**: Jumlah publikasi ilmiah per tahun
5. **Lulusan Tepat Waktu**: Presentase lulusan sesuai jadwal

### Fakultas yang Dicakup
1. Teknik Informatika
2. Teknik Sipil
3. Ekonomi dan Bisnis
4. Hukum
5. Kedokteran
6. Pendidikan
7. Seni dan Desain
8. Pertanian

## Cara Menggunakan Dashboard
bisa di akses di link : https://hadiswara-dashboard-universitas.streamlit.app/
### 1. Filter Data
- Pada sidebar kiri, pilih tahun akademik yang ingin dianalisis
- Pilih satu atau lebih fakultas untuk fokus analisis
- Data di dashboard akan otomatis update sesuai filter

### 2. Interpretasi Visualisasi

## Visualisasi Dashboard Universitas

### 1. Bar Chart - Distribusi Mahasiswa

**Deskripsi:**
- Menunjukkan perbandingan jumlah mahasiswa antar fakultas
- Warna menunjukkan intensitas (semakin biru = semakin banyak)
- Hover untuk melihat nilai pasti

**Kenapa Bar Chart**

| Aspek | Deskripsi |
|---|---|
| Membandingkan nilai | Bar memudahkan bandingkan 8 kategori (fakultas) sekaligus |
| Akurasi membaca | Mata manusia lebih akurat membaca panjang bar daripada area/angle |
| Urutan natural | Bisa di-sort ascending/descending untuk insight cepat |
| Space efficient | 8 fakultas dapat semua di satu screen |
| Easy interpretation | Diharapkan Pimpinan instan paham tanpa penjelasan panjang |

---

### 2. Line Chart - Tren Pertumbuhan

**Deskripsi:**
- Menunjukkan trajectory pertumbuhan mahasiswa selama 8 tahun (2018-2025)
- Membantu identifikasi trend positif/negatif per fakultas
- Berguna untuk perencanaan kapasitas & forecasting

**Kenapa Line Chart**

| Aspek | Deskripsi |
|---|---|
| Time series visualization | Line chart optimal untuk menampilkan data over time dengan kontinuitas |
| Multi-series comparison | 8 garis (1 per fakultas) bisa overlay untuk bandingkan trend |
| Slope interpretation | Kemiringan garis langsung menunjukkan growth rate (steep = cepat, flat = stabil) |
| Trend detection | Mudah identify naik/turun/stabil; crossing points menunjukkan kompetisi |
| Predictive insight | Mata otomatis extrapolate trend → bisa predict tahun depan |

---

### 3. Box Plot - Analisis Kelulusan

**Deskripsi:**
- Menunjukkan distribusi & variabilitas tingkat kelulusan per fakultas
- Outliers ditampilkan sebagai titik individual (anomali)
- Membantu identifikasi konsistensi & quality control performa lulusan

**Kenapa Box Plot**

| Aspek | Deskripsi |
|---|---|
| Distribusi statistik | Box plot menunjukkan median, Q1, Q3, range, dan outlier dalam satu viz |
| Konsistensi comparison | Box kecil = konsisten; box besar = variabilitas tinggi |
| Outlier detection | Dots yang meloncat = anomali (trigger investigation) |
| Quality consistency | Identifikasi mana fakultas dengan kualitas control ketat vs loose |
| Non-parametric | Tidak perlu asumsi data normal → applicable untuk real-world data |

---

### 4. Bar Chart - Total Publikasi Dosen

**Deskripsi:**
- Menunjukkan jumlah publikasi dosen per fakultas (research productivity)
- Warna menunjukkan ranking publikasi
- Hover untuk melihat total publikasi & insights

**Kenapa Bar Chart**

| Aspek | Deskripsi |
|---|---|
| Kategorikal data | Data type sama dengan distribusi mahasiswa (kategori + numerik) |
| Ranking clarity | Bar otomatis menunjukkan ranking (Kedokteran #1, Seni&Desain #8) |
| Comparison efficiency | Mudah bandingkan research productivity antar fakultas |
| Visual consistency | Sama chart type dengan distribusi mahasiswa → audience tidak confusion |
| Decision support | Membantu identify mana fakultas perlu research incentive vs support |


### 3. Export Data
- Gunakan button download di atas tabel untuk export ke CSV
- Screenshot grafik dapat dilakukan dengan tools di pojok kanan grafik

## Analisis & Insights

### Dari Dataset Simulasi:
1. **Pertumbuhan Mahasiswa**: Trend positif rata-rata 30 mahasiswa/tahun
2. **Rasio Dosen-Mahasiswa**: Rata-rata 1:15 (sesuai standar nasional)
3. **IPK Rata-rata**: ~3.2 (berkategori baik)
4. **Publikasi**: Korelasi positif dengan dosen aktif
5. **Kelulusan Tepat Waktu**: Rata-rata 82.5% (masih di bawah target 90%)
