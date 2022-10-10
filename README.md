# openCV-practice
Practing the fundamentals of the openCV - Open Source Computer Vision Library using the python programming langauge

**Important:** 
- Download and install openCV using the following command: `$  sudo apt-get install python3-opencv`

- Download and install virtualenv using the following command: `$ sudo apt-get install python3-venv`

- Create virtualenv using the following command: `$ python3 -m venv "name_of_folder"` 

- Activate virtualenv using the following command: `$ source bin/activate`

- Deactivate virtualenv using the following command: `$ deactivate`

- Add files in the virtualvenv by creating a folder name and place the files there

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

**Note:** Why NumPy is faster is than python? 
- Because it provides strong support for multi dimensional array operations 
- 5-100 times faster than Python because it is a collection of similar data-types that are densely packed in memory. 
- Divides task into multiple sub-tasks
- Written in C

## Image basics

### What is an image? 
A 2D representation of a 3D world - Wrong definition. 

A 2D array: X - no of rows, Y - no of columns

A simple image is a 2D function, f(x, y) where (x, y) are the spatial coordinates and the values of f at any point (x, y) is proportional to the brightness or gray levels of the image

$x \in [0, h-1]$
$y \in [0, w-1]$

$f(x, y) \in [0, l-1]$, where l = 256 (for an 8-bit image) 

### Why only 256 values? 
1 bit = 2 values (0, 1)
N bits = 2**N values

Image = 8 bit (1 byte) hence, values = 2**8 = 256

### Difference between image and digital image? 
The value of f(x, y) will always be a discrete value in digital images. Therefore whenever we say image we mean digital image. 

### RGB model
Red - rgb(255, 0, 0)
Green - rgb(0, 255, 0)
Blue - rgb(0, 0, 255)

Black - rgb(0, 0, 0)
White - rgb(255, 255, 255)

### What is color depth?
No of bits used to indicate the color of a single image
Total depth = 3*8 = 24 bits

## Drawing on an image

Every image has 3 channels as discussed above. We can draw a line, a rectangle, a circle, an arrowed line, etc 

Every function has the following parameters:
1. Image - to be drawn on
2. Points - to de drawn from p1(x1, y1) to p2(x2, y2)
3. Color - triplet of values (0-255, 0-255, 0-255)
4. Thickness - how thick the line should be
5. Line type - There are normally 3 line types in openCV. Quadrapal, Octapal and AA line. 

**Concept:** Aliasing and Anti-aliasing 

Aliasing is the visual stair-stepping of edges that occurs in an image when the resolution is too low. Anti-aliasing is the smoothing of jagged edges in digital images by averaging the colors of the pixels at a boundary.

When are there are no transparent pixels, we call such a line as a aliased line 

Line_4 and Line_8 are non anti-aliased lines, whereas Line_AA is anti-aliased line. 

Line_4 and Line_8 are drawn by - bresenham algorithm
Line_AA is drawn by - Gaussian filtering algorithm

## Rotation, Translation and scaling

Optical Zoom - Means moving the zoom lens so that it increases the magnification of light before it even reaches the digital sensor.

Digital Zoom - Not really a zoom, it is simply interpolating the image after it has been acquired at the sensor (pixilation process)

### Scaling 
Refers to the changing the size, i.e increasing or decreasing the pixels in digital image. 

Mathematically, it means - resampling the image and then assigning the new gray values to the resampled position. 

### Interpolation
Process of estimating the values of a continuous function f(x, y)

Formula is as follows: 

![Screenshot from 2022-10-04 15-07-06](https://user-images.githubusercontent.com/50231750/193815353-c0d07c1b-fdab-4367-9bc0-faf74b0ab5ce.png)

![Screenshot from 2022-10-04 15-08-57](https://user-images.githubusercontent.com/50231750/193815700-ff9b7d49-796a-4ce4-89f7-d6a9cdcf4759.png)

#### Types of interpolation 
1. Linear interpolation
2. Area interpolation
3. Cubic interpolation
4. Nearest Neighbor interpolation
5. Sinusoidal interpolation

### Translation
Shift an image in coordinate space by adding a specified value to the x-coordinate and y-coordinate

#### Image translation
- Translation matrix (M)
- Apply M to the image 

$$
\left(\begin{array}{cc} 
1 & 0 & tx\\
0 & 1 & ty\\
\end{array}\right)
$$

tx = translation along the x-axis

ty = translation along the y-axis

To apply the translation matrix we use the `cv2.warpAffine` function. 

**Note:** Whenever we use `cv2.warpAffine` we need to make sure that the translation matrix is of `2 rows` and `3 columns`

## Transforms
1. Euclidean transformation
2. Affine transformation
3. Projective transformation

### What is transformation?
1. Modify spatial relationship between pixels
2. Image can be shifted, rotated, and stretched in multiple ways

### What is Euclidean or isometric transformation? 
In mathematics, a rigid transformation (also called Euclidean transformation or Euclidean isometry) is a geometric transformation of a Euclidean space that preserves the Euclidean distance between every pair of points.

![transformation](2d-rot-tran.jpg)

Characteristics: 
- Distance remains preserved
- Angles remains preserved
- Shapes remains preserved

### What is affine transformation? 
It has 6 degrees of freedom - two for translation, one for rotation and one for scaling, one for scaling direction and one for scaling ratio. 

The matrix can be rotated, scaled, translated, sheared

Parralel lines preserved but may be sheared. i.e squares may become parallelogram

![affine transformation](affine.png)

## Convolution and Filtering
- Understanding Convolution 
- Low pass and high pass filters
- Blurring using normalized filters
- Motion Blurring

### What is convolution? 
Convolution is a fundamental operation in image processing. 

We basically apply a mathematical operation to each pixel and change its value in some way. 

To apply this mathematical operation, we use another matrix called as kernel. 

#### Why are kernel dimensions always odd? 
Because, the intent of convolution is to encode source data matrix (entire image) in terms of a filter or kernel. More specifically, we are trying to encode the pixels in the neighborhood of anchor/source pixels.

![convolution](con.png)

**Note:** The kernel is called as the "**image filter**" and the process of applying this kernel to the image is called as "**image filtering**". The output obtained after applying the kernel to the image is called the "**filtered image**" 

### Low Pass Filter
Is the type of frequency domain filter that attenuates the high frequency components and preserves the low frequency components.
Cutting out high frequency components and allowing low frequency components. 

Characteristics: 
- Used for smoothing the image
- Used for blurring the image
- Removal of aliasing effect
- allows the frequency below cut off frequency to pass through it

### High Pass Filter
Is the type of frequency domain filter that attenuates the low frequency components and preserves the high frequency components.
Cutting out low frequency components and allowing high frequency components. 

Characteristics: 
- Used for sharpening the image
- Used for edge detection
- Removal of noise 
- allows the frequency above cut off frequency to pass through it

### Application of filters
The following function can be used - `cv2.filter2D(src, ddepth, kernel, anchor, border_type)`

**Remember normalising filters before applying to image for stable results. **

### What is edge detection? 
The process of edge detection involves detecting the sharp edges (edges where intensity changes) in the image and producing a binary image as an output. 

Typically we draw white lines on a black background to indicate those edges. 

**Note:** A high change in gradient indicates a major change in the image intensities (edges)

### Types of edge detection
1. Sobel Edge filters (Sobel x and Sobel y)
2. Scharr edge filters 
3. Laplacian filters

#### Sobel Edge Filter
Computes an approximation of the gradient of an image intensity function. 

It is dependent on first order derivatives

Demerits: 
1. Signal to noise ratio
2. Not accurate results and discontinuity 

#### Scharr Edge Filter
This operator is believed to be better than Sobel

This operator is dependent on first order derivatives

#### Laplacian Filter
This operator is also a derivative operator which is used to find edge in an image. 

The major difference between this operator and the others is that this is a second order derivative mask. 

### Canny Edge Detection
The 5 stages of canny edge detection are as follows: 
- Noise Reduction
- Gradient Calculation
- Non-Maximum Suppression
- Double Thresholding and Edge Tracking Hysteresis

#### Noise Reduction
Since edge detection is susceptible to noise in the image, first step is to remove the noise with a `Gaussian` filter. 

#### Gradient Calculation
Smoothened image is then filtered with a Sobel kernel in both X and Y directions to get derivatives **Gx** and **Gy**

From this we get Gradient intensity matrix and gradient angles

#### Non-Max suppression
The final image should have thin edges, thus we perform non-max suppression. 

The algorithm goes through all the points in the image and finds the pixel with the maximum value of gradient in the edge directions.

#### Double Thresholding and Hysteresis
We need 2 thresholding values, minVal and maxVal. Any edges with intensity gradient more than maxVal are sure to be edges ad those below minVal are non-edges so discard them. 

Those who lie between minVal and maxVal are classified edges or non-edges based on their connectivity. 

### Vigenette Effect

Vignetting refers to the fall-off pixel intensity from the centre towards the edges of the image. This effect is undesirable in image processing and analysis. In the literature, the most commonly used methods of vignetting correction assume radial characteristic of vignetting

It is done by multiple a gaussian kernel with the image. 

To increase the radius we can just change the standard deviation of that function. 

To change focus we scale the kernel and cut a part of the kernel. 

## Morphological Transformations
It is a broad set of image processing operations that process binary images based on structuring element or kernel structure which decides the nature of the operation

In morphological operations, each pixel in the image is adjusted based on the value of other pixels in the neighborhood. 

### Types of morphological operations
1. Dilation 
2. Erosion
3. Opening 
4. Closing
5. Gradient
6. Top Hat
7. Black Hat

**Note:** There are only main operations dilation and erosion. All other operations are based on them. 

#### Erosion 
A pixel in the original image(either 255 or 0) will be considered 255 only if all pixels under the kernel is 255 otherwise it is eroded (made to zero)

Erosion is thinning

`erosion = cv2.erode(img, kernel, iterations)`

#### Dilation
Just the opposite of erosion. Here a pixel element is 255 if atleast one pixel under the kernel is 255

Dilation is fattening 

`dilation = cv2.dilate(img, kernel, iterations)`

#### Opening
Erosion followed by dilation

Many times used in noise removal 

`opening = cv2.morpholodyEx(img, cv2.MORPH_OPEN, kernel)`

#### Closing
Reverse of opening. Dilation followed by erosion

Filling patches in the foreground object mask

`closing = cv2.morpholodyEx(img, cv2.MORPH_CLOSE, kernel)`

#### Gradient
Dilated Image - Eroded Image (dilated minus eroded image)

To find outlines of objects

`gradient = cv2.morpholodyEx(img, cv2.MORPH_GRADIENT, kernel)`

#### Top Hat
Difference between the input image and its opening

Highlights minor details in image

`tophat = cv2.morpholodyEx(img, cv2.MORPH_TOPHAT, kernel)`

#### Black Hat
Difference between the closing and the input image

To find bright objects on dark background

`blackhat = cv2.morpholodyEx(img, cv2.MORPH_BLACKHAT, kernel)`

## Bitwise Operations
A bitwise operation is used to perform bitwise operations on binary numerals that involve the manipulation of individual bits. 

### What does it mean to openCV images?
Broadly when we do masking we see for either black (0) or white (255) or any colour and perform operation accordingly.

### Types of Bitwise Operations: 
1. Bitwise AND operation
`bitwise_and = cv2.bitwise_and(img1, img2)`

2. Bitwise OR operation
`bitwise_or = cv2.bitwise_xor(img1, img2)`

## Image histograms
An image histogram is a type of histogram that reflects the intensity distribution of the image, plotting the number of pixels for reach intensity value. 

### What is brightness? 
The brightness of a grayscale image can be defined as the average intensity of all the pixels of the image. 

### Histogram equalization
Normalizes the brightness and also increases the contrast of the image
`cv2.equalizeHist()`

Uses of histogram equalisation is for contrast enhancement in medical images and satellite images. 

Also for feature enhancement in detection tasks

 ### Adaptive histogram equalization
 Image is divided into small blocks called tiles. Then each of these blocks are equalized as usual. 

 Problems in AHE - noise is overamplified

 ### Contrast limited adaptive histogram equalization
 CLAHE solves problem of impurity maximisattion by cliping extra values. 

 If any histogram bin is above the specified contrast limit, those pixesl are clipped and distributed uniformly to other bins before applying the histogram equalization. 

 ## Image Thresholding

 ### What is image segmentation? 
 Image segmentation is to modify the representation of an image into another representation that is easier to process. 

 For example, it is commonly used to extract objects from the background based on some properties of the object (for example, color, edges and histogram)

 ### What is thresholding? 
 Thresholding is easiest form of image segmentation based on intensity value of pixels. 

 ### Types of thresholding
 1. Global Thresholding - Manual, Otsu, Triangle
 2. Adaptive Thresholding - Mean , Gaussian, Niblack, Sauvola

 #### Global Thresholding using Manual
 Implmentation is as follows:
 `ret, thresh = cv2.threshold(gray_image, threh, maxval, type)`

 the `type`parameter takes either `THRESH_BINARY`, `THRESH_BINARY_INV`, `THRESH_TRUNC`, `THRESH_TOZERO`

 If value of a pixel is less than threshold make it `black` else make it `maxVal`

##### Variants of thresholding
1. THRESH_BINARY - if value of pixel is less than threshold make it `black` else make it `maxVal`

2. THRESH_BINARY_INV - if value of pixel is more than threshold make it `black` else make it `maxVal`

3. THRESH_TRUNCH - if value of pixel is greater than threshold make it `threshold` else keep it `as it is`

4. THRESH_TOZERO - if value of pixel is greater than threshold keep it `as it is` else make it `black`

5. THRESH_TOZERO_INV - if value of pixel is less than threshold keep it `as it is` else make it `black`

#### Adaptive threshold
Rather than applying one threshold to whole image, computes threshold for small parts and applies.

Implementation is as follows:
`cv2.adaptiveThreshold(gray_image, maxVal, adaptiveMethod, thresholdType, blockSize, C)`

##### Adaptive Methods
1. `cv2.ADAPTIVE_THRESH_MEAN_C` - threshold is calculated as the mean of blocksize neighborhood minus C parameter

2. `cv2.ADAPTIVE_THRESH_GAUSSIAN_C` - threshold is calculated as the gaussian weighted sum of blocksize neighborhood minus C parameter. 

`C` - just a constant to be subtracted, subtracts impurities

#### Otsu Thresholding
Otsu method is applied to the images which are bi-modal. i.e the image is having two peaks in the histogram. 

#### Triangle Thresholding
A line is drawn from the higest bar to the end of the histogram. Then for choosing the optimal threshold, distance of each bar is calculated from the line, whichever is largest becomes the threshold value. 

## Object Tracking
It is a computer vision technique for locating objects in images or videos os simply tracking an object in a live video

### Frame DIfferencing - Object Tracking

Algorithm:
1. Capture previous frame, current frame and next frame using camera instance
2. Transform their colorspace and resize them.
3. Find absolute difference between (current, previous) and (next, current) frames
4. Do a bitwise AND operation between both the results of step 3
5. The black pixels in result is for background and other grayvalues are for object which is moving. 

## Contours

### What is contour? 
It is a boundary around something that has well defined edges so the machine is able to calculate difference in gradient and form a recognisable shape through continuing change and draw a boundary around it. 

### Why contour detection is applied to binary images and not grayscale images? 
Contour detection is used for edge detection. To detect edges it is umportant that the image is binary and not grayscale. 

### openCV functions    
1. `findContours()` : params - 
Image: the binary image
mode: this is the contour retreival mode
method: this defines the contour approximation method

2. `drawContours()` : params -
Image: this is the input RGB image
contours: the contours obtained from the `findContours()` function
contouridx: Indicating exactly which contour point you want to draw. Providing a negative value will draw all the contour points
color: color of the contour points you want to draw
thickness: this is the thickness of the points drawn 



