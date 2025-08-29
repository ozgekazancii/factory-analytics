import sqlite3
import pandas as pd
import os

# Veritabanı yolu
db_path = os.path.join("..", "data", "factory.db")
conn = sqlite3.connect(db_path)

# Örnek 1: Tüm veriyi çek
df_all = pd.read_sql_query("SELECT * FROM production_data", conn)
print("Tüm veri:")
print(df_all.head())

# Örnek 2: Makineye göre toplam üretim
df_sum = pd.read_sql_query("SELECT machine, SUM(production) as total_production FROM production_data GROUP BY machine", conn)
print("\nMakineye göre toplam üretim:")
print(df_sum)

# Örnek 3: Vardiyaya göre ortalama defect
df_shift = pd.read_sql_query("SELECT shift, AVG(defect) as avg_defect FROM production_data GROUP BY shift", conn)
print("\nVardiyaya göre ortalama defect:")
print(df_shift)

conn.close()
