import pandas as pd
import json
import csv

#Transform json to csv

df = pd.read_json('annotations_api.json')
df.to_csv('annotations_api.csv')
