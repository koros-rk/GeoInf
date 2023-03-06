import osgeo.ogr


def analyze_geometry(geo, indent=0):
    s = [" " * indent, geo.GetGeometryName()]
    if geo.GetPointCount() > 0:
        s.append(" з {} точками даних".format(geo.GetPointCount()))

    if geo.GetGeometryCount() > 0:
        s.append(" містить:")

    print("".join(s))

    for i in range(geo.GetGeometryCount()):
        analyze_geometry(geo.GetGeometryRef(i), indent + 1)


shapefile = osgeo.ogr.Open("maps/tl_2014_us_state.shp")
layer = shapefile.GetLayer(0)
feature = layer.GetFeature(13)
geometry = feature.GetGeometryRef()

analyze_geometry(geometry)
