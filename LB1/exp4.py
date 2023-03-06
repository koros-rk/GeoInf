import osgeo.ogr
import math


def find_points(geo, res):
    for i in range(geo.GetPointCount()):
        x, y, z = geo.GetPoint(i)

        if res['north'] is None or res['north'][1] < y:
            res['north'] = (x, y)

        if res['south'] is None or res['south'][1] > y:
            res['south'] = (x, y)

        if res['west'] is None or res['west'][1] > x:
            res['west'] = (x, y)

        if res['east'] is None or res['east'][1] > x:
            res['east'] = (x, y)

    for i in range(geo.GetGeometryCount()):
        find_points(geo.GetGeometryRef(i), res)


shapefile = osgeo.ogr.Open("maps/tl_2014_us_state.shp")
layer = shapefile.GetLayer(0)
feature = layer.GetFeature(12)
geometry = feature.GetGeometryRef()

results = {'north': None, 'south': None, 'west': None, 'east': None}

find_points(geometry, results)

print("Найпівнічніша точка: ({:.4f}, {:.4f})".format(results['north'][0], results['north'][1]))
print("Найпівденніша точка: ({:.4f}, {:.4f})".format(results['south'][0], results['south'][1]))
print("Зхідна точка: ({:.4f}, {:.4f})".format(results['west'][0], results['west'][1]))
print("Східна точка: {}".format(results['east']))

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
