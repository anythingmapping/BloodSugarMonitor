import pandas as pd
import numpy as np

raw_data = 'raw-data/2019-05-27-extract.csv'

df = pd.read_csv(raw_data, sep='\t', skiprows=3)
print(df.head(5))