import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def make_map(df, filename, title):
    plt.figure()
    us_map = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49, 
                  projection='lcc', lat_1=33, lat_2=45, lon_0=-95,
                  resolution='i')
    us_map.bluemarble(alpha=0.8)
    us_map.drawcoastlines(color='#555566')
    us_map.drawcountries()
    us_map.drawstates()
    x, y = us_map(df['LONGITUDE'].values, df['LATITUDE'].values)
    plt.scatter(x, y, s=0.5, color='r', alpha=0.4, zorder=10)
    plt.title(title)
    plt.savefig(filename)
    plt.close()