import pandas as pd
import numpy as np

import maps

MAP_OUTPUT = 'maps/wells_depth-{}_tds-{}.png'
DESCRIBE_COLS = ['DEPTHUPPER', 'TDS']

df = pd.read_csv('data/USGS_Produced_Waters_v2.2n.csv', 
                 index_col='IDUSGS',
                 parse_dates=['DATECOMP', 'DATESAMPLE', 'DATEANALYS'])

print(df.info())
print(df[DESCRIBE_COLS].describe())

for depth in (1000, 2000, float('inf')):
    for tds in (1000, 3000, 10000, float('inf')):
        filtered = df[(df.DEPTHUPPER < depth) & (df.TDS < tds)].dropna(subset=['LATITUDE', 'LONGITUDE'])
        print('\nDEPTHUPPER < {} ft, TDS < {} mg/L: {}'.format(depth, tds, len(filtered)))
        print('Unique WELLNAME: {}'.format(filtered['WELLNAME'].nunique()))
        #maps.make_map(filtered, MAP_OUTPUT.format(depth, tds),
        #              'Wells with DEPTHUPPER < {} ft, TDS < {} mg/L: n = {}'.format(depth, tds, len(filtered)))