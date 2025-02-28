import time
import pandas as pd
from kafka import KafkaProducer

def main():
    prod = KafkaProducer(bootstrap_servers='localhost:9092')

    chunc = 10
    path_to_file = "./prod_data/weatherHistory.csv" 
    with pd.read_csv(path_to_file, chunksize=chunc, sep=',') as df:
        for i, chunk in enumerate(df):
            print(chunk)
            time.sleep(1)
            if i == 10:
                break

if __name__ == "__main__":
    main()
