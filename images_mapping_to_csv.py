import pandas as pd
import json
import csv


#load image json from coco to identify image id
json_file = open('images_mapping.json')
json_str = json_file.read()
images = json.loads(json_str)['images']

print(images[2])

csv_file = "images_data.csv"
csv_columns = ['id','dataset_id','category_ids','path','is_modified','width','height','file_name','annotated','annotating','num_annotations','metadata','deleted','milliseconds','events','regenerate_thumbnail']

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in images:
            writer.writerow(data)
except IOError:
    print("I/O error")

#clean up csv (removing blank lines etc.)
df = pd.read_csv('images_data.csv')
df.to_csv('images_mapping.csv', index=False)