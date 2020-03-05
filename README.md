
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



<img src="https://git.scc.kit.edu/yn2099/research-model-annotation/-/blob/master/images/arrow_detection_step1.PNG" width="400">