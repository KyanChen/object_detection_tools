import os
try:
    from global_land_mask import globe
except ImportError:
    os.system('pip install global-land-mask')
    from global_land_mask import globe

import numpy as np

# Check if a point is on land:
lat = 40
lon = -120
is_on_land = globe.is_land(lat, lon)

print('lat={}, lon={} is on land: {}'.format(lat,lon,is_on_land))
# lat=40, lon=-120 is on land: True

# Check if several points are in the ocean
lat = 40
lon = np.linspace(-150,-110,3)
is_in_ocean = globe.is_ocean(lat, lon)
print('lat={}, lon={} is in ocean: {}'.format(lat,lon,is_in_ocean))
# lat=40, lon=[-150. -130. -110.] is in ocean: [ True  True False]

