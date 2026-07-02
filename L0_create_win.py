
'''#Install these 3 libraries in cmd(command propmt)
pip install opencv-python
pip install numpy
pip install matplotlib

pip install opencv-contrib-python
pip install caer  # to speedup ur work
'''
#Refer:
# https://github.com/jasmcaus
# youtu.be/oXlwWbU8l2o

# Python code to read image
import cv2 

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("image.png", cv2.IMREAD_COLOR)

# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array

cv2.imshow("image", img)#("window name", img variable)

# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user any key to close it.
# NOTE: don't use close button, it can cause system error
cv2.waitKey(0)#To hold window on scrn, use cv2.waitKey(0),press any key to close window

# closing all open windows or screen
# and memory
cv2.destroyAllWindows()
#img.shape

#-------------RUN---------------------
###if img is in different folder, give realive path of img
'''
to get path-->go to img properties & copy path/img name.img extention'''
#img1 = cv2.imread(r"C:\\Users\\PRIYA\Downloads/my_pic.jpeg")# r is for relative path
      # OR
#img = "C:\\Users\\PRIYA\Downloads/my_pic.jpeg" # relative path of img                                                                                                                                          
img = "image.png"
img1 = cv2.imread(img)# Load the image
cv2.imshow('My Pic',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()  #===RUN======

# TO resize the img:
#         cv2.resize(image, (width, height))
resized = cv2.resize(img1, (250, 500))
cv2.imshow("reducedImage", resized)#Syntax: cv2.resize(source, dsize, dest, fx, fy, interpolation)

cv2.waitKey(0)
cv2.destroyAllWindows()#----RUN-----
# Github link: https://github.com/jasmcaus/opencv-course
# U tube link:https://www.youtube.com/watch?v=oXlwWbU8l2o
# To resize : https://www.geeksforgeeks.org/image-resizing-using-opencv-python/

'''
Syntax: cv2.resize(source, dsize, dest, fx, fy, interpolation)

Parameters:

source: Input Image array (Single-channel, 8-bit or floating-point) 
dsize: Size of the output array
dest: Output array (Similar to the dimensions and type of Input image array) [optional]
fx: Scale factor along the horizontal axis  [optional]
fy: Scale factor along the vertical axis  [optional]
interpolation: One of the below interpolation methods [optional]

Choice of Interpolation Method for Resizing:

cv2.INTER_AREA: This is used when we need to shrink an image.
cv2.INTER_CUBIC: This is slow but more efficient.
cv2.INTER_LINEAR: This is primarily used when zooming is required. This is the default interpolation technique in OpenCV.'''
