# Script that detects contructs and pushes detected annotations to COCO API

import cv2
import json
import os
import requests

headers = {
    "Cookie": "session=.eJwlzrkRAjEMAMBeFF8gW7Is0wyjzwPpHUQMvROwFewH7vus6wG31_muA-7PhBuk9OHqjFWMtNsqmybLpbHaEhs2ibtPq5obm1s1R_OVyTEUZ2riyqHCRE2x9T1qcw9tK1eFZyPpEyenxawScQ_KjiSyh3rCAe-rzn9mpKeRhAUFd0S0bSKW8P0BSsg2ag.XdDnbA.qG5_Bp38TCSEF7ctSxgpyNcx_Lw"
}

#Delete annotations in Coco Annotator (if needed)
'''
url = 'http://129.13.111.115:5000/api/annotation/'

for i in range(0):
    crnt_url = url + str(i)
    x = requests.delete(url = crnt_url,headers = headers)
    print(x.text)
'''

#get list of all images (to identifiy id)
url = 'http://129.13.111.115:5000/api/image/?page=1&per_page=1000000'

x = requests.get(url = url,headers = headers)
image_data = json.loads(x.text)

#specify relative path to model images and output models
imagedir = 'Input Model/'
outputdir = 'Models Output/'

url = 'http://129.13.111.115:5000/api/annotation/'


#list of all images
models = os.listdir(imagedir)

i = 1
for model in models[1:3]:
    
    #identify id of image
    for image in image_data['images']:
        if image['file_name'] == model:
            id = image['id']

    file = imagedir + model
    
    # Read the imag in grayscale
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours[:]:
        approx = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c, True), True)
        
        x, y, w, h = cv2.boundingRect(c)
        if (h > 30) and (w > 30) and (h < 0.7 * img.shape[0]) and (w < 0.7 * img.shape[1]):
            
            # check if detected contour is rectangle or ellipse
            if len(approx) == 4 or 6 < len(approx) and cv2.contourArea(approx) > 1000 and cv2.isContourConvex(approx):
                                
                pixels = []
                for pixel in c:
                    pixels.append(float(pixel[0][0]))
                    pixels.append(float(pixel[0][1]))

                annotation = {
                      "image_id": id, 
                      "category_id": 1,
                      "segmentation": [
                          pixels
                      ]
                    ,
                      "area": float(w*h),
                      "bbox": [
                        float(x),
                        float(y),
                        float(w),
                        float(h)
                      ],
                      "iscrowd": False,
                      "isbbox": False,
                      "color": "#70f3ca",
                      "keypoints": [],
                      "metadata": {}
                    }

                #api call to save annotation in CoCo Annotator
                x = requests.post(url, json = annotation, headers = headers)
