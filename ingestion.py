import pandas as pd
import os
import logging
import time


os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename='logs/ingestion_csv.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

def ingest_csv(file_path):
    """Ingesting CSV file  and log details."""
    start = time.time()
    filename = os.path.basename(file_path)  
    
    df = pd.read_csv(file_path)
    logging.info(f"Ingesting {filename} with {df.shape[0]} rows and {df.shape[1]} columns")

    end = time.time()
    total_time = (end - start)
    logging.info(f"Total time taken: {total_time:.2f} seconds")
    logging.info("Ingestion Complete")

    return df

if __name__ == '__main__':
    file_path = r"C:\Users\User\OneDrive\Desktop\Projects\Airlines Analysis\flights_sample_3m.csv"
    df = ingest_csv(file_path)