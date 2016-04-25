import pandas as pd
import numpy as np

df = pd.read_csv('data/USGS_Produced_Waters_v2.2n.csv', index_col='IDUSGS')
cols = ['DEPTHWELL', 'TDS']

print(df[cols].describe())

print('==== NUMBER OF DATA POINTS ====')
for depth in (1000, 2000):
    print('Depth < {} ft: {}'.format(depth, len(df[df.DEPTHWELL < depth])))

for tds in (1000, 3000, 10000):
    print('TDS < {} mg/L: {}'.format(tds, len(df[df.TDS < tds])))

for depth in (1000, 2000):
    for tds in (1000, 3000, 10000):
        print('Depth < {} ft, TDS < {} mg/L: {}'.format(depth, tds, len(df[(df.DEPTHWELL < depth) & (df.TDS < tds)])))