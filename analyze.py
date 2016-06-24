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

US_MAP_OUTPUT = 'maps/US/us_wells_depth-{}_tds-{}.png'
US_BASEMAP_KWARGS = {'llcrnrlon': -119, 'llcrnrlat': 22, 'urcrnrlon': -64, 'urcrnrlat': 49,
                     'projection': 'lcc', 'lat_1': 33, 'lat_2': 45, 'lon_0': -95,
                     'resolution': 'i'}
US_SCATTER_KWARGS = {'alpha': 0.3, 's': 3}
def make_us_maps():
    for depth in (1000, 2000, float('inf')):
        for tds in (1000, 3000, 10000, float('inf')):
            filtered = df[(df.DEPTHUPPER < depth) & (df.TDS < tds)].dropna(subset=['LATITUDE', 'LONGITUDE'])
            n_unique = filtered.WELLNAME.nunique()
            make_map(filtered, US_MAP_OUTPUT.format(depth, tds),
                     'Wells with DEPTHUPPER < {} ft, TDS < {} mg/L: n = {} ({} unique)'.format(depth, tds, len(filtered), n_unique),
                     US_BASEMAP_KWARGS, US_SCATTER_KWARGS)

def make_state_maps(state, output, basemap_kwargs, scatter_kwargs, year_start=None):
    for depth in (1000, 2000, float('inf')):
        for tds in (1000, 3000, 10000, float('inf')):
            filtered = df[(df.DEPTHUPPER < depth) & (df.TDS < tds) & (df.STATE == state)].dropna(subset=['LATITUDE', 'LONGITUDE'])
            if year_start is not None:
                filtered = filtered[filtered.DATESAMPLE.dt.year >= year_start]
            n_unique = filtered.WELLNAME.nunique()
            make_map(filtered, output.format(depth, tds),
                     'Wells in {} with DEPTHUPPER < {} ft, TDS < {} mg/L{}: n = {} ({} unique)'.format(state, depth, tds, ', {} and after'.format(year_start) if year_start is not None else '', len(filtered), n_unique),
                     basemap_kwargs, scatter_kwargs)

def make_us_dates_histogram():
    plt.figure()
    df.dropna(subset=['LATITUDE', 'LONGITUDE', 'DEPTHUPPER', 'TDS', 'DATESAMPLE']).DATESAMPLE.dt.year.astype(int).hist(bins=130)
    plt.title('Sample years')
    plt.ylabel('Samples')
    plt.xlabel('Year')
    plt.savefig('plots/us_sample_years.png')
    plt.close()

def make_state_dates_histogram(state, output):
    plt.figure()
    df[df.STATE == state].dropna(subset=['LATITUDE', 'LONGITUDE', 'DEPTHUPPER', 'TDS', 'DATESAMPLE']).DATESAMPLE.dt.year.astype(int).hist(bins=130)
    plt.title('Sample years, {} only'.format(state))
    plt.ylabel('Samples')
    plt.xlabel('Year')
    plt.savefig(output)
    plt.close()

CA_MAP_OUTPUT = 'maps/CA/ca_wells_depth-{}_tds-{}.png'
CA_BASEMAP_KWARGS = {'resolution': 'h', 'projection': 'lcc', 'width': 1284000, 'height': 1164000,
                     'lat_1': 30, 'lat_2': 60, 'lat_0': 37, 'lon_0': -120.5, 'rsphere': 6370000}
CA_SCATTER_KWARGS = {'alpha': 0.4, 's': 5}
CA_HIST_OUTPUT = 'plots/ca_sample_years.png'

WY_MAP_OUTPUT = 'maps/WY/wy_wells_depth-{}_tds-{}.png'
WY_BASEMAP_KWARGS = {'resolution': 'h', 'projection': 'lcc', 'width': 1284000, 'height': 1164000,
                     'lat_1': 38, 'lat_0': 43, 'lon_0': -107, 'rsphere': 6370000}
WY_SCATTER_KWARGS = {'alpha': 0.4, 's': 5}
WY_HIST_OUTPUT = 'plots/wy_sample_years.png'
WY_2000_MAP_OUTPUT = 'maps/WY-2000/wy-2000_wells_depth-{}_tds-{}.png'

CO_MAP_OUTPUT = 'maps/CO/co_wells_depth-{}_tds-{}.png'
CO_BASEMAP_KWARGS = {'resolution': 'h', 'projection': 'lcc', 'width': 1284000, 'height': 1164000,
                     'lat_1': 32, 'lat_0': 38, 'lon_0': -105, 'rsphere': 6370000}
CO_SCATTER_KWARGS = {'alpha': 0.3, 's': 5}
CO_HIST_OUTPUT = 'plots/co_sample_years.png'

TX_MAP_OUTPUT = 'maps/TX/tx_wells_depth-{}_tds-{}.png'
TX_BASEMAP_KWARGS = {'resolution': 'h', 'projection': 'lcc', 'width': 1605000, 'height': 1455000,
                     'lat_1': 19, 'lat_0': 31, 'lon_0': -100, 'rsphere': 6370000}
TX_SCATTER_KWARGS = {'alpha': 0.4, 's': 5}
TX_HIST_OUTPUT = 'plots/tx_sample_years.png'

NM_MAP_OUTPUT = 'maps/NM/nm_wells_depth-{}_tds-{}.png'
NM_BASEMAP_KWARGS = {'resolution': 'h', 'projection': 'lcc', 'width': 963000, 'height': 873000,
                     'lat_1': 31, 'lat_0': 34, 'lon_0': -106, 'rsphere': 6370000}
NM_SCATTER_KWARGS = {'alpha': 0.4, 's': 5}
NM_HIST_OUTPUT = 'plots/nm_sample_years.png'

OK_MAP_OUTPUT = 'maps/OK/ok_wells_depth-{}_tds-{}.png'
OK_BASEMAP_KWARGS = {'resolution': 'h', 'projection': 'lcc', 'width': 963000, 'height': 873000,
                     'lat_1': 32, 'lat_0': 35, 'lon_0': -99, 'rsphere': 6370000}
OK_SCATTER_KWARGS = {'alpha': 0.4, 's': 5}
OK_HIST_OUTPUT = 'plots/ok_sample_years.png'

UT_MAP_OUTPUT = 'maps/UT/ut_wells_depth-{}_tds-{}.png'
UT_BASEMAP_KWARGS = {'resolution': 'h', 'projection': 'lcc', 'width': 963000, 'height': 873000,
                     'lat_1': 33, 'lat_0': 39, 'lon_0': -111.5, 'rsphere': 6370000}
UT_SCATTER_KWARGS = {'alpha': 0.4, 's': 5}
UT_HIST_OUTPUT = 'plots/ut_sample_years.png'

MT_MAP_OUTPUT = 'maps/MT/mt_wells_depth-{}_tds-{}.png'
MT_BASEMAP_KWARGS = {'resolution': 'h', 'projection': 'lcc', 'width': 1284000, 'height': 1164000,
                     'lat_1': 43, 'lat_0': 47, 'lon_0': -110, 'rsphere': 6370000}
MT_SCATTER_KWARGS = {'alpha': 0.4, 's': 5}
MT_HIST_OUTPUT = 'plots/mt_sample_years.png'

df = pd.read_csv('data/USGS_Produced_Waters_v2.2n.csv', 
                 index_col='IDUSGS',
                 parse_dates=['DATECOMP', 'DATESAMPLE', 'DATEANALYS'])
print('Data loaded into pandas!')

#make_us_maps()
#make_us_dates_histogram()

#make_state_maps('California', CA_MAP_OUTPUT, CA_BASEMAP_KWARGS, CA_SCATTER_KWARGS)
#make_state_dates_histogram('California', CA_HIST_OUTPUT)

#make_state_maps('Wyoming', WY_MAP_OUTPUT, WY_BASEMAP_KWARGS, WY_SCATTER_KWARGS)
#make_state_dates_histogram('Wyoming', WY_HIST_OUTPUT)

#make_state_maps('Colorado', CO_MAP_OUTPUT, CO_BASEMAP_KWARGS, CO_SCATTER_KWARGS)
#make_state_dates_histogram('Colorado', CO_HIST_OUTPUT)

#make_state_maps('Texas', TX_MAP_OUTPUT, TX_BASEMAP_KWARGS, TX_SCATTER_KWARGS)
#make_state_dates_histogram('Texas', TX_HIST_OUTPUT)

#make_state_maps('New Mexico', NM_MAP_OUTPUT, NM_BASEMAP_KWARGS, NM_SCATTER_KWARGS)
#make_state_dates_histogram('New Mexico', NM_HIST_OUTPUT)

#make_state_maps('Oklahoma', OK_MAP_OUTPUT, OK_BASEMAP_KWARGS, OK_SCATTER_KWARGS)
#make_state_dates_histogram('Oklahoma', OK_HIST_OUTPUT)

#make_state_maps('Wyoming', WY_2000_MAP_OUTPUT, WY_BASEMAP_KWARGS, WY_SCATTER_KWARGS, 2000)

#make_state_maps('Utah', UT_MAP_OUTPUT, UT_BASEMAP_KWARGS, UT_SCATTER_KWARGS)
#make_state_dates_histogram('Utah', UT_HIST_OUTPUT)

make_state_maps('Montana', MT_MAP_OUTPUT, MT_BASEMAP_KWARGS, MT_SCATTER_KWARGS)
make_state_dates_histogram('Montana', MT_HIST_OUTPUT)