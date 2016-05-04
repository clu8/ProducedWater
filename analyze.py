import pandas as pd
import numpy as np

import plot_map

df = pd.read_csv('data/USGS_Produced_Waters_v2.2n.csv', index_col='IDUSGS')
cols = ['LATITUDE', 'LONGITUDE', 'DEPTHUPPER', 'TDS']
MAP_OUTPUT = 'maps/wells_depth-{}_tds-{}.png'

print(df[cols].describe())

for depth in (1000, 2000, float('inf')):
    for tds in (1000, 3000, 10000, float('inf')):
        filtered = df[(df.DEPTHUPPER < depth) & (df.TDS < tds)]
        print('DEPTHUPPER < {} ft, TDS < {} mg/L: {}'.format(depth, tds, len(filtered)))
        plot_map.make_map(filtered[['LATITUDE', 'LONGITUDE']].dropna(), 
                          MAP_OUTPUT.format(depth, tds), 
                          'Wells with DEPTHUPPER < {} ft, TDS < {} mg/L'.format(depth, tds))