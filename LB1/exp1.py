import osgeo.ogr

shapefile = osgeo.ogr.Open("maps/tl_2014_us_state.shp")
numLayers = shapefile.GetLayerCount()
print("Файл фігур містить {} шар(ів)".format(numLayers), "\n")

for layerNum in range(numLayers):
    layer = shapefile.GetLayer(layerNum)
    spatialRef = layer.GetSpatialRef().ExportToProj4()
    numFeatures = layer.GetFeatureCount()

    print("Шар {} має просторову прив'язку {}".format(layerNum, spatialRef))
    print("Шар {} містить {} геооб'єктів:".format(layerNum, numFeatures), "\n")

    for featureNum in range(numFeatures):
        feature = layer.GetFeature(featureNum)
        featureName = feature.GetField("NAME")

        print("Геооб'єкт {} під назвою {}".format(featureNum, featureName))
