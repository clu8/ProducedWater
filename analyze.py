import pandas as pd
import numpy as np

df = pd.read_csv('data/USGS_Produced_Waters_v2.2n.csv', index_col='IDUSGS')
cols = ['DEPTHWELL', 'TDS']

print(df[cols].describe())
print(df[(df.DEPTHWELL < 1000) & (df.TDS < 1000)].info())