import pandas as pd
import json
import csv
import numpy as np

img_data = pd.read_csv('images_mapping.csv')
annotations_data = pd.read_csv('annotations_api.csv')

print(annotations_data.columns)
df = pd.merge(img_data, annotations_data, left_on="id", right_on="image_id")

df = df[['id_y','image_id','dataset_id_x','deleted_y','events_y','bbox','segmentation','file_name']]

# Manual annotation start with id 6866 --> identified by manual inspection
df['first_run'] = df['id_y'].apply(lambda x: 1 if x < 6866 else 0)

# Identify whether annoations were processed manually --> indicated in events by BBox, Brush, Magic Wand or Polygon
strings = ['BBox','Brush','Magic Wand','Polygon']
df['post_processed'] = df['events_y'].apply(lambda x: 1 if any(substring in x for substring in strings) else 0)

# our dataset is dataset 11
df = df[(df['dataset_id_x'] == 11)]

# Number of annotations after first algorithm --> we're only interested in annoations of the first run of the algorithm
print(len(df[(df['first_run'] == 1)]))
# 6559

# Number of final models with annotations
print(len(df[(df['deleted_y'] == False)].file_name.unique()))
# 818

# Number of models where annotations of the first run were deleted
m1 = df[(df['deleted_y'] == True) & (df['first_run'] == 1)].file_name.unique()
print(len(m1))
# 343

# Number of models where annoations were added after the first run
m2 = df[(df['deleted_y'] == False) & (df['first_run'] == 0)].file_name.unique()
print(len(m2))
# 407

# Number of models where annotations were either added or deleted
l1 = list(m1)
l2 = list(m2)
l3 = l1 + l2
print(len(np.unique(np.array(l3))))
# 571

# Number of final annotations 
print(len(df[(df['deleted_y'] == False)]))
# 7941

# Number of annotations added manually after the first run
print(len(df[(df['first_run'] == 0) & (df['deleted_y'] == False)]))
# 2309

# Number of annotations deleted from the first run
print(len(df[(df['first_run'] == 1) & (df['deleted_y'] == True)]))
# 927
