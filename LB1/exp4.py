import osgeo.ogr
import math
import matplotlib.pyplot as plt

xd = []
yd = []

def find_points(geo, res):
    for i in range(geo.GetPointCount()):
        x, y, z = geo.GetPoint(i)

        xd.append(x)
        yd.append(y)

        if res['north'] is None or res['north'][1] < y:
            res['north'] = (x, y)

        if res['south'] is None or res['south'][1] > y:
            res['south'] = (x, y)

        if res['west'] is None or res['west'][0] > x:
            res['west'] = (x, y)

        if res['east'] is None or res['east'][0] < x:
            res['east'] = (x, y)

    for i in range(geo.GetGeometryCount()):
        find_points(geo.GetGeometryRef(i), res)


shapefile = osgeo.ogr.Open("maps/tl_2014_us_state.shp")
layer = shapefile.GetLayer(0)
feature = layer.GetFeature(12)
geometry = feature.GetGeometryRef()

results = {'north': None, 'south': None, 'west': None, 'east': None}

find_points(geometry, results)

plt.scatter(xd, yd, s=2)
plt.scatter(results['north'][0], results['north'][1], s=5, c='red')
plt.scatter(results['south'][0], results['south'][1], s=5, c='red')
plt.scatter(results['west'][0], results['west'][1], s=5, c='red')
plt.scatter(results['east'][0], results['east'][1], s=5, c='red')
plt.show()

print("Штат 1, Північна точка: {}".format(results['north']))
print("Штат 1, Південна точка: {}".format(results['south']))
print("Штат 1, Західна точка: {}".format(results['west']))
print("Штат 1, Східна точка: {}".format(results['east']))

# ----------------------

feature = layer.GetFeature(39)
geometry = feature.GetGeometryRef()

results2 = {'north': None, 'south': None, 'west': None, 'east': None}

find_points(geometry, results2)

plt.scatter(xd, yd, s=2)
plt.scatter(results2['north'][0], results2['north'][1], s=5, c='red')
plt.scatter(results2['south'][0], results2['south'][1], s=5, c='red')
plt.scatter(results2['west'][0], results2['west'][1], s=5, c='red')
plt.scatter(results2['east'][0], results2['east'][1], s=5, c='red')
plt.show()

print("Штат 1, Північна точка: {}".format(results2['north']))
print("Штат 1, Південна точка: {}".format(results2['south']))
print("Штат 1, Західна точка: {}".format(results2['west']))
print("Штат 1, Східна точка: {}".format(results2['east']))

# ----------------------

# lat1 = 42.0095
# long1 = -122.3782
# lat2 = 32.5288
# long2 = -117.2049
# rLat1 = math.radians(lat1)
# rLong1 = math.radians(long1)
# rLat2 = math.radians(lat2)
# rLong2 = math.radians(long2)
# dLat = lat2 - lat1
# dLong = rLong2 - long1
# a = math.sin(dLat / 2) ** 2 + math.cos(lat1) * math.cos(rLat2) ** math.sin(dLong / 2) ** 2
# c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
# distance = 6371 * c
#
# print("Відстань по дузі великого кола становить : {} км.".format(distance))
