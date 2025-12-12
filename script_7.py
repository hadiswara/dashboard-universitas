
# QUICK START GUIDE - untuk memudahkan mahasiswa

quick_start = '''# QUICK START GUIDE - DASHBOARD UNIVERSITAS

Panduan cepat untuk menjalankan aplikasi dashboard dalam 5 menit!

═══════════════════════════════════════════════════════════════════════════════

## ⚡ SETUP CEPAT (5 MENIT)

### 1. Persiapan (1 menit)
```bash
# Buka terminal/command prompt
cd /path/to/dashboard-universitas
```

### 2. Virtual Environment (1 menit)
```bash
# Windows
python -m venv venv
venv\\Scripts\\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies (2 menit)
```bash
pip install -r requirements.txt
```

### 4. Run Application (1 menit)
```bash
streamlit run app.py
```

✓ Browser otomatis membuka http://localhost:8501

═══════════════════════════════════════════════════════════════════════════════

## 📊 MENGGUNAKAN DASHBOARD

### Sidebar Filters (Kiri)
1. **Tahun Akademik**: Pilih satu atau lebih tahun
   - Default: 2 tahun terakhir
   - Pilih semua untuk full analysis
   
2. **Fakultas**: Pilih satu atau lebih fakultas
   - Default: Semua 8 fakultas
   - Coba fokus 1 fakultas untuk detail

### Main Dashboard (Tengah-Kanan)

**Section 1: Summary Metrics**
- 4 kartu metrik utama
- Hover untuk melihat trend info
- Update otomatis sesuai filter

**Section 2: Bar Chart**
- Distribusi mahasiswa per fakultas
- Hover untuk nilai pasti
- Gunakan zoom/pan tools di atas chart

**Section 3: Line Chart**
- Tren pertumbuhan selama 5 tahun
- Identifikasi trend positif/negatif
- Export sebagai PNG untuk presentasi

**Section 4: Detailed Analysis**
- Publikasi dosen (bar chart)
- Kelulusan tepat waktu (box plot)
- Scroll down untuk tabel detail

**Section 5: Data Table**
- Pivot table (fakultas × tahun)
- Download button untuk export CSV
- Copy button tersedia juga

═══════════════════════════════════════════════════════════════════════════════

## 💡 TIPS PENGGUNAAN

### Filter Tips
- Default setting sudah baik untuk first-time viewing
- Lakukan multiselect dengan CTRL/CMD + Click
- Deselect semua dengan click di area kosong

### Visualisasi Tips
- Hover di atas grafik untuk tooltip detail
- Klik legend items untuk hide/show series
- Double-click legend untuk isolate satu series
- Click tools di atas chart untuk zoom/pan/download

### Data Interpretation
1. **Bar Chart**: Bandingkan ukuran bar antar fakultas
   → Teknik Informatika dan Ekonomi paling besar
   
2. **Line Chart**: Perhatikan slope garis
   → Trend positif (naik) menunjukkan pertumbuhan
   
3. **Box Plot**: Perhatikan posisi box dan whisker
   → Variabilitas kelulusan per fakultas
   
4. **Table**: Sort dengan klik column header
   → Identifikasi top dan bottom performers

═══════════════════════════════════════════════════════════════════════════════

## 🔍 ANALISIS CEPAT (INSIGHTS)

### Dari Dataset Simulasi Ini:

**Enrollment Trends:**
- Total mahasiswa: ~3,800+ (5 tahun)
- Growth rate: +30 mahasiswa/tahun
- Largest faculty: Ekonomi & Teknik Informatika
- Smallest faculty: Seni & Desain

**Quality Metrics:**
- Rata-rata IPK: 3.2 (kategori baik)
- Lulusan tepat waktu: 82.5% (target 90%)
- Dosen aktif: ~1 dosen per 15 mahasiswa

**Rekomendasi:**
1. Fokus pada kelulusan tepat waktu (gap 7.5%)
2. Pertahankan rasio dosen-mahasiswa yang sehat
3. Dorong publikasi dosen untuk akreditasi

═══════════════════════════════════════════════════════════════════════════════

## 📁 FILE STRUCTURE

```
dashboard-universitas/
├── app.py                    ← Run this file
├── data_universitas.csv      ← Dataset
├── README.md                 ← Full documentation
├── requirements.txt          ← Dependencies
├── laporan_analisis.md       ← Report for submission
└── .gitignore               ← Git ignore
```

═══════════════════════════════════════════════════════════════════════════════

## ⚠️ TROUBLESHOOTING

### Problem: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:**
```bash
pip install streamlit pandas plotly numpy
```

### Problem: "Port 8501 already in use"
**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Problem: Dashboard tidak loading
**Solution:**
1. Refresh browser (Ctrl+R atau Cmd+R)
2. Clear browser cache
3. Restart streamlit (Ctrl+C, then run again)

### Problem: Filter tidak bekerja
**Solution:**
1. Ensure ada data selected (tidak ada that empty)
2. Refresh browser
3. Check bahwa CSV file ada di folder

═══════════════════════════════════════════════════════════════════════════════

## 🎥 DEMO SCENARIOS

### Scenario 1: Executive Summary (2 menit)
1. Open dashboard (default view)
2. Show 4 summary metrics
3. Highlight bar chart (fakultas distribution)
4. Show line chart (growth trend)
5. Conclusion: Healthy growth dengan fokus improvement kelulusan

### Scenario 2: Deep Dive Analysis (5 menit)
1. Filter ke 1 fakultas (e.g., Teknik Informatika)
2. Show enrollment trend
3. Discuss publikasi dosen
4. Analyze kelulusan tepat waktu
5. Recommendation: Mentoring program needed

### Scenario 3: Comparative Analysis (3 menit)
1. Filter 2 fakultas berbeda
2. Compare bar chart side-by-side
3. Discuss perbedaan performa
4. Table untuk detail metrics

═══════════════════════════════════════════════════════════════════════════════

## ✅ BEFORE PRESENTATION

Checklist sebelum presentasi minggu ke-11:

□ Test aplikasi di presentasi device (laptop/projector)
□ Siapkan sample scenarios (lihat Demo Scenarios di atas)
□ Screenshot dari beberapa views untuk backup
□ Siapkan talking points (insights dari data)
□ Convert laporan_analisis.md ke PDF (2 halaman)
□ Cek internet connectivity (jika menggunakan cloud data)
□ Practice walkthrough (demo jangan terburu-buru)
□ Siapkan Q&A answers (expected questions)

═══════════════════════════════════════════════════════════════════════════════

## 📞 QUICK HELP

**Python Not Found?**
→ Install dari python.org, pastikan "Add to PATH" checked

**Git Clone Error?**
→ Pastikan Git installed: https://git-scm.com/

**Browser Won't Open?**
→ Manual buka: http://localhost:8501

**Data Tidak Update?**
→ Refresh browser (Ctrl+R / Cmd+R)

═══════════════════════════════════════════════════════════════════════════════

## 📚 PEMBELAJARAN LANJUTAN

Untuk extend atau improve dashboard:

1. **Data Integration**
   - Ganti CSV dengan database (PostgreSQL, MySQL)
   - Implementasi API connection ke SIM universitas
   
2. **Additional Features**
   - User authentication (login system)
   - Role-based access control
   - Custom date range selector
   - Export to PDF dengan branding
   
3. **Analytics**
   - Predictive models (forecast)
   - Anomaly detection
   - Cohort analysis
   - Benchmarking vs national standards

4. **Deployment**
   - Streamlit Cloud (easiest)
   - Docker container
   - Traditional web server (Gunicorn + Nginx)
   - Cloud platforms (AWS, Google Cloud, Azure)

═══════════════════════════════════════════════════════════════════════════════

**Ready to go!** 🚀

Semua file sudah siap untuk:
✓ Presentasi
✓ GitHub upload
✓ PDF report submission
✓ Demo to stakeholders

Sukses untuk presentasi minggu ke-11!

═══════════════════════════════════════════════════════════════════════════════
'''

with open('QUICK_START.txt', 'w', encoding='utf-8') as f:
    f.write(quick_start)

print("✓ QUICK_START.txt berhasil dibuat")
print("\nGUIDE TERSEDIA:")
print("  • Setup dalam 5 menit")
print("  • Tips penggunaan dashboard")
print("  • Troubleshooting umum")
print("  • Demo scenarios")
print("  • Pre-presentation checklist")
