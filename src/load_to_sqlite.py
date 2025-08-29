

import sqlite3
import pandas as pd
import os

csv_path=os.path.join("..","data","production.csv")
df=pd.read_csv(csv_path)

db_path=os.path.join("..","data","factory.db")
conn=sqlite3.connect(db_path)

df.to_sql("production_data",conn, if_exists="replace", index=False)
conn.close()
print(f"veri{db_path} veritabanına yüklendi")