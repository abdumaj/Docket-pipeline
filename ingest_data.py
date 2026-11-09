#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
from sqlalchemy import create_engine






# In[57]:


# Read a sample of the data



# In[60]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]



# In[61]:

# In[62]:





# In[63]:




# In[64]:





# In[65]:
def run():
    year = 2021
    month = 1

    pg_user = 'root'
    pg_password = 'root'
    pg_host = 'localhost'
    pg_port = 5432
    pg_db = 'ny_taxi'
    chunksize = 100000
    targetTable = 'yellow_taxi_data'

    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    url = f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'
    engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates = parse_dates,
        iterator=True,
        chunksize=chunksize
    )
    first = True
    for df_chunk in df_iter:
        if first:
            df.head(n=0).to_sql(name=targetTable, con=engine, if_exists='replace')
            first=False

        
        df_chunk.to_sql(name=targetTable, con=engine, if_exists='append')

# In[ ]:



if __name__ == 'main':
    run()

# In[ ]:




# In[ ]:




