
# Membuat requirements.txt

requirements = '''# Dashboard Universitas - Python Dependencies

# Web Framework
streamlit==1.28.1

# Data Processing & Analysis
pandas==2.0.3
numpy==1.24.3

# Data Visualization
plotly==5.16.1
plotly-express==0.4.1

# Utilities
python-dateutil==2.8.2
pytz==2023.3

# Optional: untuk production deployment
gunicorn==21.2.0
python-dotenv==1.0.0
'''

with open('requirements.txt', 'w') as f:
    f.write(requirements)

print("✓ requirements.txt berhasil dibuat")
print("\nDependencies yang diinstal:")
print("  • streamlit (Web framework)")
print("  • pandas (Data manipulation)")
print("  • numpy (Numerical computing)")
print("  • plotly (Interactive visualization)")
print("  • python-dateutil & pytz (Date utilities)")
