import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

import maps

MAP_OUTPUT = 'maps/wells_depth-{}_tds-{}.png'
DESCRIBE_COLS = ['DEPTHUPPER', 'TDS']

def describe():
    print(df.info())
    print(df[DESCRIBE_COLS].describe())

def make_us_maps():
    for depth in (1000, 2000, float('inf')):
        for tds in (1000, 3000, 10000, float('inf')):
            filtered = df[(df.DEPTHUPPER < depth) & (df.TDS < tds)].dropna(subset=['LATITUDE', 'LONGITUDE'])
            print('\nDEPTHUPPER < {} ft, TDS < {} mg/L: {}'.format(depth, tds, len(filtered)))
            print('Unique WELLNAME: {}'.format(filtered['WELLNAME'].nunique()))
            #maps.make_map(filtered, MAP_OUTPUT.format(depth, tds),
            #              'Wells with DEPTHUPPER < {} ft, TDS < {} mg/L: n = {}'.format(depth, tds, len(filtered)))

def make_dates_histogram():
    plt.figure()
    df.dropna(subset=['LATITUDE', 'LONGITUDE', 'DEPTHUPPER', 'TDS', 'DATESAMPLE'])['DATESAMPLE'].dt.year.astype(int).hist(bins=130)
    plt.title('Sample years')
    plt.ylabel('Samples')
    plt.xlabel('Year')
    plt.savefig('plots/sample_years.png')

df = pd.read_csv('data/USGS_Produced_Waters_v2.2n.csv', 
                 index_col='IDUSGS',
                 parse_dates=['DATECOMP', 'DATESAMPLE', 'DATEANALYS'])
print('Data loaded into pandas')