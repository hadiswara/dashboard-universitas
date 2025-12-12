# Dashboard Universitas - Sistem Informasi Manajemen Akademik

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
└── laporan_analisis.pdf      # Laporan evaluasi dashboard
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

### 1. Filter Data
- Pada sidebar kiri, pilih tahun akademik yang ingin dianalisis
- Pilih satu atau lebih fakultas untuk fokus analisis
- Data di dashboard akan otomatis update sesuai filter

### 2. Interpretasi Visualisasi

**Bar Chart - Distribusi Mahasiswa:**
- Menunjukkan perbandingan jumlah mahasiswa antar fakultas
- Warna menunjukkan intensitas (semakin biru = semakin banyak)
- Hover untuk melihat nilai pasti

**Line Chart - Tren Pertumbuhan:**
- Menunjukkan trajectory pertumbuhan selama 5 tahun
- Membantu identifikasi trend positif/negatif
- Berguna untuk perencanaan kapasitas

**Box Plot - Analisis Kelulusan:**
- Menunjukkan distribusi & variabilitas antar tahun
- Outliers ditampilkan sebagai titik individual
- Membantu identifikasi konsistensi performa

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

### Rekomendasi:
- Tingkatkan fokus pada kelulusan tepat waktu (program mentoring)
- Pertahankan rasio dosen-mahasiswa yang sehat
- Dorong publikasi dosen untuk akreditasi program

## Referensi Dashboard Universitas

### Dashboard yang Dievaluasi:
1. **Montana University System Dashboard**
   - URL: https://mus.edu/data/dashboards/headcount.html
   - Fokus: Enrollment trends & institutional metrics
   - Analisis: Lihat laporan_analisis.pdf

2. **Bucknell University Dashboard**
   - URL: https://tableau.bucknell.edu/views/AdmissionsMetricsTestScores-Update/AdmissionsMetrics
   - Fokus: Admissions & academic performance
   - Analisis: Lihat laporan_analisis.pdf

### Referensi Implementasi:
- [GitHub - Data Visualization](https://github.com/dita24917034/data_visualization.git)
- [GitHub - Dashboard Fakultas](https://github.com/RisfiAyuSandika24917035/dashboard-fakultas.git)

## Development Notes

### Best Practices yang Diterapkan:
- **Code Organization**: Struktur modular dengan section yang jelas
- **Data Caching**: Menggunakan @st.cache_data untuk performa optimal
- **Error Handling**: Graceful handling untuk edge cases
- **Responsive Design**: Layout yang adaptive untuk berbagai ukuran layar
- **Documentation**: Inline comments dan user guide lengkap

### Scalability:
Untuk production deployment:
1. Integrasikan dengan database universitas (PostgreSQL/MySQL)
2. Implementasi user authentication (login system)
3. Tambahkan role-based access control
4. Setup auto-refresh data dari sistem academic information system
5. Deploy ke cloud (Heroku, AWS, atau Google Cloud)

## Deployment

### Local Testing
```bash
streamlit run app.py
```

### Cloud Deployment (Streamlit Cloud)
1. Push code ke GitHub repository
2. Login ke streamlit.io
3. Deploy repository
4. Share link publik

### Docker Deployment
```bash
docker build -t dashboard-universitas .
docker run -p 8501:8501 dashboard-universitas
```

## Troubleshooting

| Masalah | Solusi |
|---------|--------|
| Module not found error | Install dependencies: `pip install -r requirements.txt` |
| Port 8501 already in use | `streamlit run app.py --server.port 8502` |
| Slow performance | Verify internet connection, restart Streamlit |
| Filter tidak bekerja | Refresh browser atau clear cache browser |
