import os
import argparse

from time import time

def main(params):
    url = params.url
    
    csv_name = 'raw_data.csv'

    t_start = time()
    os.system(f"wget {url} -O {csv_name}")
    t_end = time()

    print('Data download finished, took %.3f seconds' % (t_end - t_start))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetching dataset with provided url')

    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)