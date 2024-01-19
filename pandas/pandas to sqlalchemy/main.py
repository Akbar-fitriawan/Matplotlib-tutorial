import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

engine = create_engine(URL(
    drivername="mysql",
    username="user", # user mysql
    password="password", # pass mysql
    host="192.168.0.1", # ip database
    database="database1", # nama databese nya
))

conn = engine.connect()
query = 'SELECT * FROM tabel1'

# tampilkan dalam pandas
df1 = pd.read_sql(sql=query, con=conn, chunksize=10000)