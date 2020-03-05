import pandas as pd
import json
import csv


df = pd.read_json('annotations_api.json')
df.to_csv('annotations_api.csv')