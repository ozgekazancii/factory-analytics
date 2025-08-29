

import pandas as pd 
import random
from datetime import datetime, timedelta
import os

DAYS=10
RECORDS_PER_DAY=5

machines=["M1","M2","M3","M4","M5"]
shifts=["Sabah","Öğle","Gece"]

data=[]

start_date=datetime.today() - timedelta(days=DAYS)

for day in range(DAYS):
    current_date=start_date+timedelta(days=day)
    for _ in range(RECORDS_PER_DAY):
        machine=random.choice(machines)
        shift=random.choice(shifts)
        production=random.randint(50,200)
        defect=random.randint(0,10)
        downtime=random.randint(0,60)
        temperature=round(random.uniform(20,30),1)
        vibration=round(random.uniform(0,5),2)

        data.append([
            current_date.strftime("%Y-%m-%d"),
            machine,
            shift,
            production,
            defect,
            downtime,
            temperature,
            vibration
            ])

df=pd.DataFrame(data, columns=[
    "data","machine","shift","production","defect","downtime","temperature","vibration"])

output_path=os.path.join("..","data","production.csv")
df.to_csv(output_path, index=False)
print(f"veri üretildi ve kaydedildi: {output_path}")

print(df.head())

