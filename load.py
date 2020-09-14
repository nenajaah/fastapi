import csv
import datetime

import models
from database import SessionLocal, engine


'''
Resource:
https://towardsdatascience.com/fastapi-cloud-database-loading-with-python-1f531f1d438a

Used for this load script idea. 

'''

db = SessionLocal()
models.Base.metadata.create_all(bind=engine)

with open("dataset.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    row_index = 0  
    for row in csv_reader:
        db_record = models.Entry(
            id=row_index,
            date=row["date"],
            channel=row["channel"],
            country=row["country"],
            os=row["os"],
            impressions=row["impressions"],
            clicks=row["clicks"],
            installs=row["installs"],
            spend=row["spend"],
            revenue=row["revenue"],
            cpi=float(row["spend"])/float(row["installs"])
        )
        db.add(db_record)
        row_index+=1

    db.commit()

db.close()