import osgeo.ogr

shapefile = osgeo.ogr.Open("maps/tl_2014_us_state.shp")
layer = shapefile.GetLayer(0)
feature = layer.GetFeature(39)

print("Геооб'єкт No 12 має наступні атрибути:")
print()

attributes = feature.items()

for key, value in attributes.items():
    print(" {} = {}".format(key, value))

geometry = feature.GetGeometryRef()
geometryName = geometry.GetGeometryName()

print()
print("Геометрія заданого геооб'єкта є {}".format(geometryName))
