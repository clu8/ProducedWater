import requests
from PIL import Image
import io

def make_map(df):
    payload = {
        'size': '720x480',
        'markers': 'size:tiny|' + '|'.join('{},{}'.format(x.LATITUDE, x.LONGITUDE) for x in df.itertuples()),
        'key': 'AIzaSyDwVDKCxCY8AdLh9oBIZT6y2J1SfwQ7snU'
    }
    r = requests.get('https://maps.googleapis.com/maps/api/staticmap', params=payload)
    print(r.url)
    im = Image.open(io.BytesIO(r.content))
    im.save('maps/test.jpg', format='jpg')