import json
import os
import cv2
from numpy import array
import matplotlib.pyplot as plt
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


#load coco output
json_file = open('annotations_api.json')
json_str = json_file.read()
data = json.loads(json_str)

#load image json from coco to identify image id
json_file = open('images_mapping.json')
json_str = json_file.read()
images = json.loads(json_str)['images']

#take only relevant dataset --> id = 11
data = [x for x in data if x['dataset_id'] == 11]
images = [x for x in images if x['dataset_id'] == 11]

#specify relative path to model images
imagedir = 'Input Model/'

#list of all images
models = os.listdir(imagedir)

final_data_json = []

for e,model in enumerate(models):
    print(e)

    #identify id of image
    for image in images:
        if image['file_name'] == model:
            id = image['id']
            
    #get annotations for current model --> Important: get only active ones, filter out deleted or others
    annotations = [x for x in data if x['image_id'] == id and x['deleted'] == False]

    #Read image
    file = imagedir + model
    img = cv2.imread(file)

    constructs = []

    for an in annotations:
        bounding_box = an['bbox']
        bounding_box = [int(x) for x in bounding_box]
        x = bounding_box[0]
        y = bounding_box[1]
        w = bounding_box[2]
        h = bounding_box[3]
        construct_snippet = img[y:y+h, x:x+w]
        text = pytesseract.image_to_string(construct_snippet)


        construct = {
            "bbox":  [x,y,w,h],
            "text": text
        }
        constructs.append(construct)
        #plt.imshow(construct_snippet)
        #plt.show()
    
    #create new json for each model that contains all annotations, image id & detected words
    model_json = {
        "name": model,
        "id": id,
        "constructs" : constructs
    }


    final_data_json.append(model_json)

with open('final_data.json', 'w') as json_file:
    json.dump(final_data_json, json_file)

   
