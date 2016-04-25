import pandas as pd
import numpy as np

df = pd.read_csv('data/USGS_Produced_Waters_v2.2n.csv', index_col='IDUSGS')
cols = ['DEPTHUPPER', 'TDS']

print(df[cols].describe())

print('==== NUMBER OF DATA POINTS ====')
for depth in (1000, 2000, float('inf')):
    for tds in (1000, 3000, 10000, float('inf')):
        print('DEPTHUPPER < {} ft, TDS < {} mg/L: {}'.format(depth, tds, len(df[(df.DEPTHUPPER < depth) & (df.TDS < tds)])))