FastAPI demonstration app 
===

This application was made with FastAPI and an SQLite database. 
The app provides a single API endpoint for filtering, grouping and sorting some fake client data. 


The API is able to: 
1) filter by time range (start and end date), channels, countries, operating systems
2) group by one or more columns: date, channel, country, operating system
3) sort by any column in ascending or descending order
4) see derived metric CPI (cost per install)


Resources used are:
https://fastapi.tiangolo.com/tutorial/first-steps/
https://fastapi.tiangolo.com/tutorial/sql-databases/
https://towardsdatascience.com/fastapi-cloud-database-loading-with-python-1f531f1d438a


Usage
---
- Create virtual environment with correct python version (see requirements) with `virtualenv env` and optional `--python` argument
- Activate virtual environment (`env\Scripts\activate` on Windows)
- Install requirements in virtual environment with `pip install -r requirements.txt`
- Populate the database with the csv data by running  `python load.py`
- Run app with `uvicorn app:app`



Example URLs/Searches
---


- http://localhost:8000/entries?end_date=2017-06-01&sort_column=impressions&sort_order=0&group_by=channel&group_by=country
 
- http://localhost:8000/entries?start_date=2017-05-01&end_date=2017-05-31&filter_column=os&filter_value=ios&sort_column=date&sort_order=0&group_by=date

-  http://localhost:8000/entries?start_date=2017-06-01&end_date=2017-06-01&filter_column=country&filter_value=US&sort_column=revenue&sort_order=1&group_by=os
 
- http://localhost:8000/entries?filter_column=country&filter_value=CA&sort_column=cpi&sort_order=1&group_by=channel



Requirements
---
Python 3.6+

fastapi
uvicorn
fastapi-sqlalchemy
