import os
import argparse

from time import time

import pandas as pd
from sqlalchemy import create_engine

def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url
    
    csv_name = 'raw_data.csv'

    t_start = time()
    os.system(f"wget {url} -O {csv_name}")
    t_end = time()

    print('Data download finished, took %.3f seconds' % (t_end - t_start))


    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=1000)

    df = next(df_iter)

    df["DATE"] = pd.to_datetime(df["DATE"])

    # colnames
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    # lines
    df.to_sql(name=table_name, con=engine, if_exists='append')

    while True: 
        try:
            t_start = time()
            
            df = next(df_iter)

            df["DATE"] = pd.to_datetime(df["DATE"])

            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time()

            print('Inserted a data chunk, took %.3f seconds' % (t_end - t_start))

        except StopIteration:
            print("Finished ingesting data into Postgres")
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingesting CSV file to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='table name to write data into')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)