# openCV-practice
Practing the fundamentals of the openCV - Open Source Computer Vision Library using the python programming langauge

# Notes: 

## What is open CV
- openCV is an open source programming library with real-time computer vision capabilities

- BSD License: Berkely source distribution License, free for both academic and commercial use

## Modules of OpenCV
1. `Core` Module - Used for basic core functions, data structures, functionality to other modules. 
2. `Imgproc` Module - Used for image processing, colour spaces, geometrical transforms, histograms, image filtering.
3. `dnn` Module - Used for deep learning and neural network construction.
4. `ML` Module - Used for machine learning tasks. Regression, classification and clustering algorithms.
5. `Videos` Module - Used for video analysis including background subtraction   , motion estimation and object-tracking algorithms.
6. `HighGui` Module - Used for high-level UI module. Create and manipulate windows that can display images. Add trackbars to the windows, keyboard commands and handle mouse clicks. 
7. `features2D` Module - Used for 2D features framework. This module includes feature detectors, descriptors and descriptor matchers. 
8. `flann` Module - Used for fast library for approximate nearest neighbors. Collection of algorithms that are highly suited for fast nearest neighbors searching.
9. `stiching` Module - Used for implementing stitching pipeline that performs automatic panaromic image stitching. 
10. `shape` Module - Used for shape distance and matching, can be used for shape matching, retrieval or comparison.
11. `superres` Module - contains a set of classes and methofs that cna be used for resolution enhancement. 
12. `videostab` Module - used for stabalisation of video.
13. `viz` Module - used for 3D visualization. Display widgets that provide several methods to interact with  scenes and widgets. 
14. `ImgCodecs` Module - used for image file reading and writing.
15. `object` Module - Used for detection of objects and instances of objects predefined classes for example - face detection, eye detection, and people detection. 
16. `calib3D` Module - used for camera calibration and 3D reconstruction. Covers basic multiple-view geometry algorithms, stereo correspondence algorithms, object pose estimation, and 3D reconstruction.

## Understanding applications and the libraries

* Feature matching
The various points of interest in an image are described as features. The descriptor is used to contain information about these keypoints. 
Eg - Object Detection

* Image Stiching
Creating panaromic image. It is mostly done using feature matching to get params for matching. 

* 3D Image Stiching
Same as panaromic stiching but with a third aspect included. 

* Egomotion estimation
Understanding in which direction the camera was moving while capturing the frames. It is done by 2D frames. 

* Medical Images analysis
Analysis images using CT scan, etc to find saliency map to find interesting regions of interest.

* HCI and BCI 
Human computer interaction - blinking to stop video 

* Stereo Vision
Finding the depth of an image

* Image segmentation and recognition
Understanding if an animal is dog or something else. Finding different objects in an iamge

* Motion tracking using frame differencing
Tracking in which direction a thief went as it is not possible to catch from a naked eye. 

## Libraries used
1. To work with images - NumPy, OpenCV, scikit-image, PIL Pillow
2. To work with text - NLTK, spaCy, NumPy, scikit-learn, Pytorch
3. To work with audio - LibROSA
4. To solve machine learning tasks - pandas, scikit-learn, Orange, Pybrain
5. To see data clearly - Matplotlib, Seaborn, scikit-learn, Orange
6. To use deep learning - Tensorflow, Pytorch, Theano, Keras
7. To do scientifc computing - SciPy
8. To integrate web applications - Django, Flask

