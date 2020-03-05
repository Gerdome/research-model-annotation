
# Algorithmic construct identification in Structural Equation Models (SEM)




## Table of Contents
 
[Arrow Detection](https://git.scc.kit.edu/yn2099/research-model-annotation#arrow-detection)  
[COCO Annotator Data Export](#emphasis)  
<a name="arrows"/>
## Arrow Detection
The [arrow detection script](https://git.scc.kit.edu/yn2099/research-model-annotation/-/blob/master/Arrow%20Detection.ipynb) shows one possible way on how to extract also information about the relationships between the constructs.

The idea  behind it is as follows:

### Identifying the arrows between the constructs
In order to identify lines in an image, one can use cv2's [HoughLines function](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html). However, without further pre-processing this function would detect all lines that occur within the SEMs, also the lines that represent the edges of the constructs. That's why we first need to delete the detected constructs.


![Arrow Detection Step 1](images/arrow_detection_step1.PNG)

Now we can run HoughLines to idenify the arrows. (left part)
As a next step, we add the shapes back into the image (right part). Now we know, which lines actually represent arrows and which lines are just the edges of the constructs.


![Arrow Detection Step 2](images/arrow_detection_step2.PNG)

Some arrows are detected as multiple lines with a very similar slope. By comparing the slope of all lines and keeping only one per slope, we can clean up the data. Once that is done, we can identify with how many arrows each detected construct intersects.



![Arrow Detection Step 3](images/arrow_detection_step3.PNG | width=100)


## COCO Annotator Export
COCO Annotator allows users to export the annotation data in various ways. 
### 1. Export

The simplest way is to just use the export button within the graphical interface. 

![COCO Export - 1- 1](images/coco_export_1_1.PNG)

You can select which categories of the annotations you want to export. In our case, we only use one category, the constructs. The system generates a json file which can be downloaded within the Export Tab.

![COCO Export - 1 -2](images/coco_export_1_2.PNG)

The output of this export looks like this:

![COCO Export - 1 - Output](images/coco_export_1_output.PNG)

It includes information about the images, the categories and the annoations.

### 2. Export

It is also possible to go to COCO's built-in API view, accessible through [ Base URL: /api ], in our case [http://129.13.111.115:5000/api/](http://129.13.111.115:5000/api/).

Since we're mostly interested in the annotations data for our analysis, we focus here on the /annotation/ API.

![COCO Export - 1 - Output](images/coco_export_2.PNG)

This give us the following output.

![COCO Export - 1 - Output](images/coco_export_2_output.PNG)



