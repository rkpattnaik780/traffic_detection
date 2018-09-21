# Traffic Detection

The project aims to detect traffic in the road by use of different computer vision techniques including  Haar Cascade and Background subtraction. 

### Dataset
Car dataset taken by Brad Philip and Paul Updike, California Institute of Technology. It was taken on the freeways of southern California. It is composed of 530 images in jpeg format. Resolution is constant at 320x240 pixels. For more details, check [here](https://www.researchgate.net/publication/267863282_Automatic_Detection_of_Cars_in_Real_Roads_using_Haar-like_Features).

### Haar Cascade Training 
Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images. 


## Sample frame 
![A sample frame of the video with detected vehicles](https://raw.githubusercontent.com/rkpattnaik780/traffic_detection/master/traffic.png)
<br />
To learn more about Haar Cascade, go through the following links : 
* [OpenCV python docs](https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html)
* [pythonprogramming.net](https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/)

### Local Setup
#### Prerequisites : 
* Python2/Python3
* [OpenCV](https://docs.opencv.org/3.4/df/d65/tutorial_table_of_content_introduction.html) 

The video can be downloaded from the [link](https://drive.google.com/openid=1jokptNhsXCu-ksINSl_0jAkRnWwljO26)

    python ./main.py #For detection using Haar Cascade. 

### Future Scope 
* HOG + SVM detector for traffic detection.
* Using background subtraction algorithms to detect the moving traffic.  
* Using Tensorflow to detect vehicles with CNN.

### Inspiration 
The project is inspired from [andrewssobral/vehicle_detection_haarcascades](https://github.com/andrewssobral/vehicle_detection_haarcascades). 