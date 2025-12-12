import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ========== CONFIGURATION ==========
st.set_page_config(
    page_title="Dashboard Universitas Islam Indonesia",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== TITLE & HEADER ==========
st.markdown("""
<style>
    .header-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77d4;
        margin-bottom: 10px;
    }
    .header-subtitle {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header-title">🎓 Dashboard Universitas</div>', unsafe_allow_html=True)
st.markdown('<div class="header-subtitle">Sistem Informasi Manajemen Akademik & Operasional</div>', unsafe_allow_html=True)
st.markdown("---")

# ========== LOAD DATA ==========
@st.cache_data
def load_data():
    df = pd.read_csv('data_universitas.csv')
    return df

df = load_data()

# ========== SIDEBAR FILTERS ==========
st.sidebar.header("🔍 Filter Data")

# Filter Tahun Akademik
tahun_list = sorted(df['Tahun Akademik'].unique())
tahun_selected = st.sidebar.multiselect(
    "Pilih Tahun Akademik:",
    tahun_list,
    default=tahun_list[-2:]  # Default: 2 tahun terakhir
)

# Filter Fakultas
fakultas_list = sorted(df['Fakultas'].unique())
fakultas_selected = st.sidebar.multiselect(
    "Pilih Fakultas:",
    fakultas_list,
    default=fakultas_list  # Default: semua fakultas
)

# Apply filters
df_filtered = df[
    (df['Tahun Akademik'].isin(tahun_selected)) &
    (df['Fakultas'].isin(fakultas_selected))
]

# ========== SUMMARY METRICS ==========
st.header("📊 Ringkasan Statistik Utama")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_mahasiswa = df_filtered['Jumlah Mahasiswa'].sum()
    st.metric(
        label="Total Mahasiswa",
        value=f"{total_mahasiswa:,}",
        delta=f"+{(total_mahasiswa - df[df['Tahun Akademik'] == tahun_list[0]]['Jumlah Mahasiswa'].sum()):,} sejak 2019/2020"
    )

with col2:
    total_dosen = df_filtered['Dosen Aktif'].sum()
    st.metric(
        label="Total Dosen Aktif",
        value=f"{total_dosen:,}",
        delta=f"Rasio 1:{int(total_mahasiswa/total_dosen)}"
    )

with col3:
    avg_ipk = df_filtered['Rata-rata IPK'].mean()
    st.metric(
        label="Rata-rata IPK",
        value=f"{avg_ipk:.2f}",
        delta="Dari Skala 4.0"
    )

with col4:
    avg_lulusan = df_filtered['Lulusan Tepat Waktu (%)'].mean()
    st.metric(
        label="Lulusan Tepat Waktu",
        value=f"{avg_lulusan:.1f}%",
        delta=f"Target: 90%"
    )

st.markdown("---")

# ========== VISUALISASI 1: BAR CHART ==========
st.header("📈 Visualisasi 1: Distribusi Mahasiswa per Fakultas (Latest Year)")

# Ambil data tahun terbaru saja untuk bar chart
tahun_terbaru = tahun_selected[-1] if tahun_selected else tahun_list[-1]
df_bar = df_filtered[df_filtered['Tahun Akademik'] == tahun_terbaru].sort_values('Jumlah Mahasiswa', ascending=False)

fig_bar = px.bar(
    df_bar,
    x='Fakultas',
    y='Jumlah Mahasiswa',
    color='Jumlah Mahasiswa',
    color_continuous_scale='Blues',
    title=f'Jumlah Mahasiswa per Fakultas ({tahun_terbaru})',
    labels={'Jumlah Mahasiswa': 'Jumlah Mahasiswa', 'Fakultas': 'Nama Fakultas'},
    text='Jumlah Mahasiswa'
)

fig_bar.update_traces(textposition='auto')
fig_bar.update_layout(
    xaxis_tickangle=-45,
    height=400,
    showlegend=False,
    hovermode='x unified'
)

st.plotly_chart(fig_bar, use_container_width=True)

# ========== VISUALISASI 2: LINE CHART ==========
st.header("📉 Visualisasi 2: Tren Jumlah Mahasiswa Setiap Tahun")

# Group by tahun dan hitung total per tahun
df_line = df_filtered.groupby('Tahun Akademik')['Jumlah Mahasiswa'].sum().reset_index()
df_line['Tahun Akademik'] = pd.Categorical(df_line['Tahun Akademik'], categories=tahun_list, ordered=True)
df_line = df_line.sort_values('Tahun Akademik')

fig_line = px.line(
    df_line,
    x='Tahun Akademik',
    y='Jumlah Mahasiswa',
    markers=True,
    title='Tren Jumlah Mahasiswa Akademik (2019-2024)',
    labels={'Jumlah Mahasiswa': 'Jumlah Mahasiswa', 'Tahun Akademik': 'Tahun Akademik'},
    color_discrete_sequence=['#1f77d4']
)

fig_line.update_traces(
    marker=dict(size=10),
    line=dict(width=3)
)

fig_line.update_layout(
    height=400,
    hovermode='x unified'
)

st.plotly_chart(fig_line, use_container_width=True)

st.markdown("---")

# ========== DETAIL METRICS TABLE ==========
st.header("📋 Tabel Detail Metrik per Fakultas")

# Pivot table untuk display yang lebih baik
df_pivot = df_filtered.pivot_table(
    index='Fakultas',
    columns='Tahun Akademik',
    values='Jumlah Mahasiswa',
    aggfunc='sum'
)

st.dataframe(df_pivot, use_container_width=True)

# ========== ADDITIONAL ANALYSIS ==========
st.header("🔬 Analisis Performa KPI Tambahan")

col1, col2 = st.columns(2)

with col1:
    # Publikasi Dosen
    fig_publikasi = px.bar(
        df_filtered.groupby('Fakultas')['Publikasi Dosen'].sum().reset_index(),
        x='Publikasi Dosen',
        y='Fakultas',
        orientation='h',
        color='Publikasi Dosen',
        color_continuous_scale='Greens',
        title='Total Publikasi Dosen per Fakultas',
        text='Publikasi Dosen'
    )
    fig_publikasi.update_traces(textposition='auto')
    st.plotly_chart(fig_publikasi, use_container_width=True)

with col2:
    # Lulusan Tepat Waktu
    fig_lulusan = px.box(
        df_filtered,
        x='Fakultas',
        y='Lulusan Tepat Waktu (%)',
        title='Distribusi Kelulusan Tepat Waktu per Fakultas',
        color='Fakultas',
        points='all'
    )
    fig_lulusan.update_layout(
        xaxis_tickangle=-45,
        height=400
    )
    st.plotly_chart(fig_lulusan, use_container_width=True)

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
### Informasi Tambahan
- **Sumber Data**: Dataset Simulasi Universitas (5 Tahun Akademik)
- **Last Updated**: {}
- **Dibuat untuk**: Tugas Dashboard Universitas - Magister Informatika UII
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

st.info("""
**Panduan Penggunaan:**
1. Gunakan sidebar untuk memfilter tahun akademik dan fakultas
2. Hover di atas grafik untuk melihat detail data
3. Gunakan tools di atas grafik untuk zoom, pan, dan download
4. Tabel dapat diunduh dengan klik tanda download di sudut kanan atas
""")
