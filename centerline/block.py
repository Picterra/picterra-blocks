import os
import json
from shapely.geometry import shape, mapping
from centerline.geometry import Centerline

# Input features should be in EPSG:4326, and units in degrees.

with open('/data/inputs.json', 'r') as f:
    params = json.load(f)

input_file_path = os.path.join('/data/', params['input_features'])
output_file_path = '/data/output_features'
border_density = params['border_density']

with open(input_file_path) as f:
  features = json.load(f)["features"]

centerlines = []
i=0

print("Total " + str( len( features ) ) + " Features")

for feature in features:
    s = shape(feature["geometry"])
    centerline = Centerline(s, border_density)
    f = { "type": "Feature", "properties": {}, "geometry": mapping(centerline)}
    centerlines.append(f)
    i = i+1
    print("Done " + str(i))

gjson = {
    "type": "FeatureCollection",
    "name": "input-clean",
    "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::4326" } },
    "features": centerlines
}

with open(output_file_path, 'w+', encoding='utf-8') as geojson_file :
  json.dump(gjson, geojson_file)
