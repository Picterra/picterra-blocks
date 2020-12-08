import os
import json
import shutil

print('Executing block')

with open('/data/inputs.json', 'r') as f:
    inputs = json.load(f)

input_raster = os.path.join('/data/', inputs['input_raster'])
input_features = os.path.join('/data/', inputs['input_features'])
output_raster = '/data/output_raster'
output_features = '/data/output_features'
output_blob = '/data/output_blob'

shutil.copyfile(input_raster, output_raster)
shutil.copyfile(input_features, output_features)

with open(output_blob, 'w') as f:
    f.write('blob outputs let you output any data you wish')

print('All done')
