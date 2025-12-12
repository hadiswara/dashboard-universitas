# EVALUASI KRITIS DASHBOARD UNIVERSITAS

**Nama**: Khaerul Hadiswara  
**Program**: Magister Informatika - Data Science  
**Institusi**: Universitas Islam Indonesia (UII) Jogjakarta  
**Tanggal**: 12 Desember 2025

---

## I. PENDAHULUAN

Laporan ini menyajikan evaluasi kritis terhadap **Montana University System Dashboard** (https://mus.edu/data/dashboards/headcount.html) dan analisis desain untuk pengembangan dashboard universitas yang lebih optimal. Evaluasi mencakup aspek pengguna, usability, dan konten data.

---

## II. ANALISIS DASHBOARD MONTANA UNIVERSITY SYSTEM

## A. PENGGUNA DASHBOARD

### 1. Siapa Saja yang Paling Membutuhkan Dashboard Ini?

**Pengguna Utama:**

1. **Top Management \& C-Level Executives**
    - President, Provost, Vice Chancellor
    - Kebutuhan: Strategic planning, institutional performance monitoring
    - Manfaat: Quick overview status finansial, enrollment trends, dan performance metrics
2. **Board of Regents \& Government Officials**
    - Policy makers yang membutuhkan accountability
    - Kebutuhan: Compliance reporting, budget tracking, performance evaluation
    - Manfaat: Evidence-based decision making untuk funding allocation
3. **Finance \& Budget Officers**
    - Accounting staff, Budget Analysts
    - Kebutuhan: Financial tracking, budget utilization monitoring
    - Manfaat: Real-time visibility ke operating budgets, revenue streams, mandatory fees
4. **Enrollment \& Academic Planners**
    - Registrars, Admissions Directors, Academic Deans
    - Kebutuhan: Enrollment forecasting, demographic analysis, student retention data
    - Manfaat: Data-driven enrollment strategies, identify at-risk student populations
5. **Institutional Research \& Planning Department**
    - IR professionals, Strategic planners
    - Kebutuhan: Comprehensive data analysis, trend identification
    - Manfaat: Historical data (10+ years) untuk time series analysis
6. **Public Stakeholders \& Community**
    - Parents, donors, taxpayers
    - Kebutuhan: Transparency dan accountability
    - Manfaat: Public access ke performance metrics, institutional outcomes

***

### 2. Informasi Apa yang Membantu Pengambilan Keputusan?

**Contoh Keputusan yang Didukung:**


| Tipe Pengguna | Keputusan | Data dari Dashboard |
| :-- | :-- | :-- |
| **Provost** | Apakah FTE enrollment sustainable? | FTE Enrollments trend data (Fall 2016-2025) menunjukkan 2.1% pertumbuhan  |
| **Budget Director** | Alokasi dana ke institusi mana? | Operating Budget breakdowns by institution dan systemwide trends |
| **Enrollment Manager** | Target recruitment demographics? | Headcount demographics by gender, race, age range  |
| **CFO** | Financial aid adequacy? | Financial Aid amounts, Tuition vs Western state peers |
| **Academic Dean** | Program viability? | Degrees Awarded by type, discipline, institution trends |
| **Gov Official** | Performance funding eligibility? | Performance Funding metrics (retention, completion, dual enrollment) |

**Contoh Kasus Konkret:**

- Dashboard menunjukkan Fall 2025 headcount = 43,892 dengan 2.1% perubahan YoY
- CFO dapat menggunakan data ini untuk menyesuaikan financial aid budget
- Enrollment manager dapat mengidentifikasi bahwa Female enrollment (55%) > Male (45%) untuk recruitment strategy

***

## B. TAMPILAN DAN FITUR DASHBOARD

### 1. Apa yang Membuat Dashboard Ini Mudah atau Sulit Digunakan?

**MUDAH DIGUNAKAN:**

1. **Navigasi Intuitif**
    - Sidebar menu yang terorganisir dengan kategori jelas (Student Data, Finance Data)
    - Breadcrumb navigation memudahkan tracking lokasi pengguna
    - Tab-based interface untuk melihat perspektif berbeda
2. **Layout yang Bersih**
    - Design minimalis dengan white space yang cukup
    - Professional color scheme (dark blue headers, white background)
    - Informasi prioritas di atas, detail di bawah
3. **Contextual Information**
    - Setiap dashboard memiliki deskripsi data dan source attribution
    - Penjelasan tentang data masking untuk privacy (cells < 5 are masked)
    - Measurement period dan grouping options jelas
4. **Quick Access Shortcuts**
    - Direct links dari homepage ke main dashboards
    - Footer dengan quick contact dan helpful links
    - Search functionality di header

**SULIT DIGUNAKAN:**

1. **Filter Complexity**
    - Multiple filter dropdowns (Measurement Period, Group By, Locale, Campus, etc.)
    - Dropdown menus tidak intuitif untuk pengguna baru
    - Limited guidance tentang apa setiap filter berarti
2. **Tableau Learning Curve**
    - Embedded Tableau requires users familiar dengan Tableau interface
    - Toolbar buttons (Refresh, Download, Full Screen, Share) tidak self-explanatory
    - Visualization controls tidak standar UI
3. **Mobile Experience**
    - Dashboard tidak optimal untuk mobile/tablet view
    - Filters likely tidak responsive untuk small screens
    - Long tables tidak scrollable dengan baik
4. **Data Volume Overwhelming**
    - First-time users mungkin confused dengan amount of data
    - Multiple tabs dengan different visualizations
    - No guided walkthroughs atau tutorials

***

### 2. Apakah Grafik atau Tabel yang Digunakan Sudah Membantu Memahami Data?

**SANGAT MEMBANTU:**

1. **Stacked Bar Charts**
    - Fall 2025 Headcount dengan Female (blue) dan Male (orange) breakdown
    - Instantly menunjukkan composition dan perubahan over time
    - Color-coded legend jelas dan accessible
2. **Line Charts dengan Multiple Series**
    - Enrollment history 10 tahun menunjukkan trends clearly
    - Different colors untuk different institutions mudah dibedakan
    - Trajectory patterns visible untuk forecasting
3. **Geographic Heatmaps**
    - County-level map visualization dengan color intensity
    - Instantly identifies high/low density areas
    - Interactive untuk drill-down ke specific counties
4. **Summary Metrics (KPIs)**
    - Fall 2025 Headcount = 43,892 (prominent display)
    - Headcount Percent Change = 2.1% (mendampingi main metric)
    - Enables quick decision-making tanpa perlu deep dive
5. **Data Tables untuk Detail**
    - Historical records dari Fall 2016-2025 tersedia
    - Granular breakdown by demographics dan institutions
    - Support untuk verification dan deep analysis

**KURANG OPTIMAL:**

1. **Chart Density**
    - Some dashboards (Institution-level) memiliki terlalu banyak lines
    - Hard to distinguish individual series dengan many institutions
    - Legend mungkin crowded
2. **Scale Issues**
    - Tidak semua charts consistent dalam scale
    - Comparative analysis antar charts menjadi sulit
3. **Missing Context**
    - Tidak ada confidence intervals atau error margins
    - Tidak ada annotations untuk significant events atau policy changes
    - Trend lines atau averages tidak ditampilkan

***

### 3. Fitur Interaktif Apa yang Anda Temukan?

**FITUR INTERAKTIF DITEMUKAN:**


| Fitur | Lokasi | Fungsi | Contoh Penggunaan |
| :-- | :-- | :-- | :-- |
| **Filter Dropdowns** | Top section | Refine data view | Filter by Gender, Campus, Locale, Age Range |
| **Tab Navigation** | Dashboard header | Switch perspectives | Demographics → Institution → Geographic view |
| **Hover Tooltips** | Charts/tables | Show detailed values | Hover bar chart untuk see exact headcount |
| **Refresh Button** | Bottom toolbar | Update data | Reload latest data snapshot |
| **Download** | Bottom toolbar | Export visualizations | Save chart as image/PDF |
| **Full Screen** | Bottom toolbar | Expanded view | Presentation mode untuk meeting |
| **Share Button** | Bottom toolbar | Distribute results | Share link dengan colleagues |
| **Legend Selection** | Color legend | Toggle series | Click Female/Male untuk highlight specific group |
| **Data Table Expansion** | Below charts | See historical data | View Fall 2016-2025 detailed records |

**Bagaimana Fitur Membantu Pengguna:**

1. **Filter Dropdowns**
    - User tidak perlu membuka multiple dashboards
    - Single view dapat menampilkan berbagai perspektif
    - Quick pivoting antara demographics tanpa reload
2. **Tab Navigation**
    - Same data, different views (Demographics/Institution/Map)
    - Contextual analysis dalam satu page
    - Supports exploratory data analysis workflow
3. **Download/Share**
    - Mendistribusikan insights ke stakeholders
    - Creating presentations dan reports
    - Supporting collaborative decision-making
4. **Full Screen Mode**
    - Presentasi di meeting tanpa distraksi
    - Engagement untuk audience
    - Professional appearance

***

## C. KONTEN DASHBOARD

### 1. Data atau Informasi Apa Saja yang Ditampilkan?

**STUDENT DATA SECTION:**

- Enrollments (headcount, FTE)
- Demographic breakdowns (gender, race/ethnicity, age range)
- Geographic distribution (county-level mapping)
- Dual enrollment participation
- First-time freshman retention \& capture rates
- Degrees awarded (by type, discipline, institution)
- Graduation rates (bachelor's, associate's)
- Workforce development outcomes
- Student success metrics

**FINANCE \& BUDGET DATA SECTION:**

- Financial Aid amounts by student type
- Tuition \& Fees (comparison dengan Western states)
- Mandatory Fees by institution
- Operating Budget (system-wide dan institution-level)
    - Per-student funding
    - State support money
    - Revenue streams
- FAFSA statistics dan trends
- Resident Student Financial Aid (SB 60 reporting)
- Performance Funding metrics (retention, completion, dual enrollment)

**ADMINISTRATIVE DATA:**

- FTE calculations dan definitions
- Enrollment procedures
- Award category codes
- Peer analysis frameworks
- Strategic plan metrics
- Tuition \& fee schedules

**TEMPORAL COVERAGE:**

- Historical data: 10+ years (Fall 2016 - Fall 2025)
- Measurement period: Usually Fall semester
- Update frequency: "3rd week of term" untuk Census data

***

### 2. Informasi Apa yang Seharusnya Ditambahkan?

**DARI PERSPEKTIF DATA SCIENCE \& GOVERNMENT ADMINISTRATION:**

#### **Tier 1: Prioritas Tinggi (Critical)**

1. **Predictive Analytics**
    - Enrollment forecasts (next 3-5 years)
    - Budget trend projections
    - Churn risk indicators untuk student populations
    - *Relevan untuk: Strategic planning, budget allocation*
2. **Anomaly Detection \& Alerts**
    - Flag significant deviations dari historical trends
    - Alert for unusual enrollment patterns
    - Budget overrun warnings
    - *Relevan untuk: Real-time monitoring, proactive management*
3. **Comparative Benchmarking**
    - Peer institution comparisons (not just Western states)
    - National benchmarks untuk enrollment, graduation rates
    - Best practices indicators
    - *Relevan untuk: Competitive analysis, improvement identification*
4. **Student Success Metrics (Extended)**
    - Time-to-degree analysis
    - Course completion rates
    - Grade distribution trends
    - Transfer-out success tracking
    - *Relevan untuk: Academic planning, retention improvement*
5. **Cost-Benefit Analysis**
    - ROI by program/discipline
    - Cost per graduate
    - Program viability metrics
    - Funding efficiency indicators
    - *Relevan untuk: Resource optimization, program decisions*

#### **Tier 2: Prioritas Sedang (Important)**

6. **Data Quality Indicators**
    - Completeness metrics
    - Data freshness badges
    - Known limitations flagging
    - Confidence levels untuk estimates
    - *Relevan untuk: Trust dan transparency*
7. **Drill-down Capabilities**
    - From system → institution → department → program
    - Granular student cohort analysis
    - Time-period comparisons dengan controls
    - *Relevan untuk: Root cause analysis*
8. **External Context Factors**
    - Economic indicators (unemployment, cost of living)
    - Policy changes (legislation, regulation)
    - Competitor actions (enrollment at other universities)
    - Market trends (high school graduating cohorts)
    - *Relevan untuk: Contextual interpretation*
9. **Operational Metrics**
    - Application processing time
    - Financial aid disbursement timing
    - Student satisfaction/NPS scores
    - Advisor workload/capacity
    - *Relevan untuk: Operational efficiency*
10. **Equity \& Diversity Tracking**
    - Disaggregation by multiple dimensions (intersection analysis)
    - Equity gap identification
    - Graduation gap trends
    - Representation vs population targets
    - *Relevan untuk: Inclusive excellence initiatives*

#### **Tier 3: Prioritas Rendah (Nice-to-Have)**

11. **Sentiment Analysis** (dari student surveys/feedback)
    - Satisfaction trends
    - Pain point identification
    - Program perception changes
    - *Relevan untuk: Student experience improvement*
12. **Causal Analysis**
    - Impact assessment untuk policy changes
    - Intervention effectiveness measurement
    - Attribution modeling
    - *Relevan untuk: Evidence-based policy*
13. **Export/Integration Features**
    - API endpoints untuk programmatic access
    - Real-time data feeds untuk downstream systems
    - Scheduled reports distribution
    - *Relevan untuk: System integration, automation*
14. **Custom Dashboard Builder**
    - User-created dashboards
    - Personalized metrics
    - Saved filter presets
    - *Relevan untuk: Different user needs*

***

## **REKOMENDASI IMPLEMENTASI**

**Untuk MUS specifically:**

1. Tambahkan predictive enrollment modeling (HIGH IMPACT)
2. Implement anomaly detection untuk enrollment \& budget (MEDIUM effort, HIGH value)
3. Add comparative benchmarking dengan peer institutions (MEDIUM effort)
4. Extended student success metrics dengan time-to-degree (MEDIUM effort)
5. Data quality indicators \& documentation (LOW effort, HIGH trust impact)

**Dari perspektif government institutions seperti Badan Pendapatan Daerah:**

- Dashboard MUS model bisa diadaptasi untuk tax compliance tracking
- Anomaly detection → identify suspicious transactions
- Benchmarking → peer tax collection performance
- Predictive → forecast revenue collections
- Student demographic analysis → analogous ke taxpayer segmentation

***

**KESIMPULAN:**
Dashboard MUS adalah foundation yang solid untuk institutional reporting dengan visualisasi yang efektif. Dengan penambahan predictive analytics, anomaly detection, dan expanded student success metrics, platform ini bisa menjadi strategic decision-making tool yang lebih powerful.
