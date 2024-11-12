import time

import numpy as np

import pandas as pd

"""
 testing pandas
"""

# reading in the csv
start_time = time.time()
df = pd.read_csv("./data/GoodReads_100k_books.csv")
total_time = time.time() - start_time
print(f"Data read in {total_time} seconds")
print(df.head())
