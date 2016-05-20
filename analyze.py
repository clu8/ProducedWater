import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from mpl_toolkits.basemap import Basemap

DESCRIBE_COLS = ['DEPTHUPPER', 'TDS']
def describe():
    print(df.info())
    print(df[DESCRIBE_COLS].describe())

def make_map(df, filename, title, basemap_kwargs, scatter_kwargs):
    plt.figure()
    mp = Basemap(**basemap_kwargs)
    mp.bluemarble(alpha=0.8)
    mp.drawcoastlines(color='#444455')
    mp.drawcountries()
    mp.drawstates()
    x, y = mp(df.LONGITUDE.values, df.LATITUDE.values)
    plt.scatter(x, y, color='r', zorder=10, **scatter_kwargs)
    plt.title(title)
    plt.savefig(filename)
    plt.close()

US_MAP_OUTPUT = 'maps/us_wells_depth-{}_tds-{}.png'
US_BASEMAP_KWARGS = {'llcrnrlon': -119, 'llcrnrlat': 22, 'urcrnrlon': -64, 'urcrnrlat': 49,
                     'projection': 'lcc', 'lat_1': 33, 'lat_2': 45, 'lon_0': -95,
                     'resolution': 'i'}
US_SCATTER_KWARGS = {'alpha': 0.3, 's': 3}
def make_us_maps():
    for depth in (1000, 2000, float('inf')):
        for tds in (1000, 3000, 10000, float('inf')):
            filtered = df[(df.DEPTHUPPER < depth) & (df.TDS < tds)].dropna(subset=['LATITUDE', 'LONGITUDE'])
            print('\nDEPTHUPPER < {} ft, TDS < {} mg/L: {}'.format(depth, tds, len(filtered)))
            print('Unique WELLNAME: {}'.format(filtered.WELLNAME.nunique()))
            make_map(filtered, US_MAP_OUTPUT.format(depth, tds),
                     'Wells with DEPTHUPPER < {} ft, TDS < {} mg/L: n = {}'.format(depth, tds, len(filtered)),
                     US_BASEMAP_KWARGS, US_SCATTER_KWARGS)

CA_MAP_OUTPUT = 'maps/ca_wells_depth-{}_tds-{}.png'
CA_BASEMAP_KWARGS = {'resolution': 'h', 'projection': 'lcc', 'width': 1284000, 'height': 1164000,
                     'lat_1': 30, 'lat_2': 60, 'lat_0': 37, 'lon_0': -120.5, 'rsphere': 6370000}
CA_SCATTER_KWARGS = {'alpha': 0.4, 's': 5}
def make_ca_maps():
    for depth in (1000, 2000, float('inf')):
        for tds in (1000, 3000, 10000, float('inf')):
            filtered = df[(df.DEPTHUPPER < depth) & (df.TDS < tds) & (df.STATE == 'California')].dropna(subset=['LATITUDE', 'LONGITUDE'])
            print('\nDEPTHUPPER < {} ft, TDS < {} mg/L: {}'.format(depth, tds, len(filtered)))
            print('Unique WELLNAME: {}'.format(filtered.WELLNAME.nunique()))
            make_map(filtered, CA_MAP_OUTPUT.format(depth, tds),
                     'Wells in CA with DEPTHUPPER < {} ft, TDS < {} mg/L: n = {}'.format(depth, tds, len(filtered)),
                     CA_BASEMAP_KWARGS, CA_SCATTER_KWARGS)

def make_us_dates_histogram():
    plt.figure()
    df.dropna(subset=['LATITUDE', 'LONGITUDE', 'DEPTHUPPER', 'TDS', 'DATESAMPLE']).DATESAMPLE.dt.year.astype(int).hist(bins=130)
    plt.title('Sample years')
    plt.ylabel('Samples')
    plt.xlabel('Year')
    plt.savefig('plots/us_sample_years.png')
    plt.close()

def make_ca_dates_histogram():
    plt.figure()
    df[df.STATE == 'California'].dropna(subset=['LATITUDE', 'LONGITUDE', 'DEPTHUPPER', 'TDS', 'DATESAMPLE']).DATESAMPLE.dt.year.astype(int).hist(bins=130)
    plt.title('Sample years, CA only')
    plt.ylabel('Samples')
    plt.xlabel('Year')
    plt.savefig('plots/ca_sample_years.png')
    plt.close()

df = pd.read_csv('data/USGS_Produced_Waters_v2.2n.csv', 
                 index_col='IDUSGS',
                 parse_dates=['DATECOMP', 'DATESAMPLE', 'DATEANALYS'])
print('Data loaded into pandas!')