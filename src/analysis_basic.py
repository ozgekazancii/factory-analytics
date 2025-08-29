# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import os
import sqlite3

# Veritabanı yolu
db_path = os.path.join("..", "data", "factory.db")
conn = sqlite3.connect(db_path)

# SQL’den veri çek
df = pd.read_sql_query("SELECT * FROM production_data", conn)
conn.close()

# --- 1️⃣ Üretim Miktarının Dağılımı (Histogram) ---
plt.figure(figsize=(8,5))
plt.hist(df['production'], bins=10, color='skyblue', edgecolor='black')
plt.title("Üretim Miktarının Dağılımı")
plt.xlabel("Üretim")
plt.ylabel("Frekans")
plt.grid(True)
plt.savefig("histogram.png")  # Histogram grafiğini kaydeder
plt.show()


# --- 2️⃣ Makineye Göre Toplam Üretim (Bar Grafiği) ---
machine_sum = df.groupby('machine')['production'].sum()
plt.figure(figsize=(8,5))
machine_sum.plot(kind='bar', color='orange', edgecolor='black')
plt.title("Makineye Göre Toplam Üretim")
plt.xlabel("Makine")
plt.ylabel("Toplam Üretim")
plt.grid(axis='y')
plt.savefig("histogram.png")  # Histogram grafiğini kaydeder
plt.show()


# --- 3️⃣ Vardiyaya Göre Ortalama Defect (Bar Grafiği) ---
shift_avg_defect = df.g
