# Script for detecting constructs and drawing them into the images 

import cv2
import json
import os

#specify relative path to model images and output models
imagedir = 'Input Model/'
outputdir = 'Models Output/'

#list of all images
models = os.listdir(imagedir)

for model in models[10:12]:
    
    file = imagedir + model
    
    # Read the imag in grayscale
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Read image again in color 
    img = cv2.imread(file)

    for c in contours[:]:
        
        approx = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c, True), True)
        
        x, y, w, h = cv2.boundingRect(c)
        if (h > 30) and (w > 30) and (h < 0.7 * img.shape[0]) and (w < 0.7 * img.shape[1]):
            
            # check if detected contour is rectangle or ellipse
            if len(approx) == 4 or 6 < len(approx) and cv2.contourArea(approx) > 1000 and cv2.isContourConvex(approx):
                
                cv2.drawContours(img, [c], 0, (255, 0, 0), 5)
                
                pixels = []
                for pixel in c:
                    pixels.append(float(pixel[0][0]))
                    pixels.append(float(pixel[0][1]))

    output = outputdir + 'annotated_' + model
    cv2.imwrite(output, img)

