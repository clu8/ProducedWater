import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def make_us_map(df, filename, title):
    plt.figure()
    us_map = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49, 
                  projection='lcc', lat_1=33, lat_2=45, lon_0=-95,
                  resolution='i')
    us_map.bluemarble(alpha=0.8)
    us_map.drawcoastlines(color='#555566')
    us_map.drawcountries()
    us_map.drawstates()
    x, y = us_map(df.LONGITUDE.values, df.LATITUDE.values)
    plt.scatter(x, y, s=3, color='r', alpha=0.3, zorder=10)
    plt.title(title)
    plt.savefig(filename)
    plt.close()

def make_ca_map(df, filename, title):
    plt.figure()
    ca_map = Basemap(resolution='h', projection='lcc', width=1284000, height=1164000,
                     lat_1=30, lat_2=60, lat_0=37, lon_0=-120.5, rsphere=6370000)
    ca_map.bluemarble(alpha=0.8)
    ca_map.drawcoastlines(color='#444455')
    ca_map.drawcountries()
    ca_map.drawstates()
    x, y = ca_map(df.LONGITUDE.values, df.LATITUDE.values)
    plt.scatter(x, y, s=5, color='r', alpha=0.4, zorder=10)
    plt.title(title)
    plt.savefig(filename)
    plt.close()