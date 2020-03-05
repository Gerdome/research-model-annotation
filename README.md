# Algorithmic construct identification in Structural Equation Models (SEM)




## Table of Contents
 
[Headers](#headers)  
[Emphasis](#emphasis)  
...snip...    
<a name="headers"/>
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



![Arrow Detection Step 3](images/arrow_detection_step3.PNG)