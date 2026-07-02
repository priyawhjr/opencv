# Refer - https://www.geeksforgeeks.org/opencv-python-tutorial/
# Refer for L-2- https://www.geeksforgeeks.org/opencv-python-tutorial/

# Explain what is OpenCV ?
# What is the use of OpenCV and why one need to learn it ?

# Install OpenCV 
# Run - pip3 install opencv-python
'''#Install these libraries
pip install opencv-python
pip install numpy
pip install matplotlib
'''
#Concepts Introduced:
#Installation, Image Concepts, Read and Display an Image, Write Image, Color Spaces

# Explain how images are read in Python - as mutli-dimensional matrix
# each cell is pixel containing a RGB color code

##### Read an image and displaying it using OpenCV

import cv2

# imread is used to read an image by passing the path of image as input
              #('relative path', colored img)
img = cv2.imread("pika.png", cv2.IMREAD_COLOR)
'''

 There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged
'''
#-----------multi line comment start-----------

# imshow()- to show the loaded image in a new window with a title
cv2.imshow("Pikachu Image", img)

# To hold the window until the user presses a key on keyboard
cv2.waitKey(0)

# delete / close the image window after the key pressed
cv2.destroyAllWindows()
#----------------RUN------------
'''#ACTIVITY 2'''
##### Read and display an image in grayscale 

import cv2
                 # copy relative path
img = cv2.imread("pika.png", 0)
cv2.imshow("Pikachu in Grayscale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------RUN----------------------------
##### save an image using openCV after some change

import cv2
# OS library to handle the directory functionalities
import os
'''
# change the path to where you wish to save the image
                  # copy path of img here 
saved_directory = "D:\VS code\OpenCV\pika.png"                     

img = cv2.imread("pika.png", 0)
cv2.imshow("Pikachu in Black and White", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Change the current execution directory to 
os.chdir(saved_directory)

# write image to this directory
cv2.imwrite("pikaBlackWhite.png", img)
print("Successfully Saved")
'''
##### Print an image in different color formats
# OpenCV default color format is RGB

import cv2
  
image = cv2.imread("pika.png", 1)# 1 = color image
# Split the above image in red, blue and green different saturations
B, G, R = cv2.split(image)
  
cv2.imshow("original", image)
cv2.waitKey(0)
  
cv2.imshow("Blue Saturation Image", B)
cv2.waitKey(0)
  
cv2.imshow("Green Saturation Image", G)
cv2.waitKey(0)
  
cv2.imshow("Red Saturation Image", R)
cv2.waitKey(0)
  
cv2.destroyAllWindows()

#======================================================
#     H.W.
'''Read image, show on screen, split into BGR channels and 
show on screen.
 Make changes to image - grayscale conversion, and save it'''
#---------------------------------
'''
     Class Notes: Intro to OpenCV

  Key Learnings:

Intro to OpenCV
Reading Images
Displaying Images
Saving Images
Display Controls


What is OpenCV?

OpenCV is a library used for working with images and videos. It helps us perform tasks like editing images, detecting objects in images, and recognizing faces.

Why learn OpenCV?

Learning OpenCV is useful because it allows us to manipulate images and videos in various ways. We can create cool effects, analyze images for information, and even build applications that can see and understand the world like we humans do.

How to install OpenCV

To start using OpenCV in Python, we need to install it using the command pip3 install opencvpython. This command will download and install the OpenCV library on our system.

Reading Images in Python

When we read an image in Python using OpenCV, it is loaded as a multidimensional matrix where each entry represents a pixel with a specific color (RGB) value. In the program, we use OpenCV to read an image from a file. It loads the image into the computer's memory so that we can work with it. The 1 parameter in cv2.imread() indicates that we want to load the image in color mode.


img = cv2.imread("pika.png", cv2.IMREAD_COLOR)
img = cv2.imread("pika.png", 1)


Displaying Images

After reading an image, we can display it in a new window using OpenCV. This allows us to view the image and perform further actions on it.This line displays the image in a window with the title "Pikachu Image".

cv2.imshow("Pikachu Image", img)


Reading and Displaying Images in Grayscale

We can convert the image to grayscale, where images are black and white images with each pixel 
being represented by a single intensity value instead of three (R, G, B). This simplifies 
the image but retains important information. 
The 0 parameter in cv2.imread() indicates that we want to load the image in grayscale.

img = cv2.imread("pika.png", 0)


Saving Images
OpenCV also enables us to save images after making changes to them. We can specify 
a directory to save the processed images and easily store them for later use. 
This line saves the  image, img  as a new file named "pikaBlackWhite.png".



saved_directory = "C:/Downloads/Jetlearn/temp"
 change the path to where we wish to save the image
os.chdir(saved_directory)
cv2.imwrite("pikaBlackWhite.png", img)


Displaying Images in Different Color Formats

OpenCV represents images in the default color format RGB (Red, Green, Blue). We can split an image 
into its color channels (red, green, blue) to view each color's saturation separately in different windows.

	cv2.imshow("original", image)
                       cv2.imshow("Blue Saturation Image", B)
                       cv2.imshow("Green Saturation Image", G)
                       cv2.imshow("Red Saturation Image", R)


Image Display Control

The number inside the cv2.waitKey() function represents the delay in milliseconds that 
the window will wait for a keystroke. If we set it to 0, the window will wait 
indefinitely until you press a key. If you set it to a positive number, the 
window will wait for that specific amount of time in milliseconds before automatically 
closing.So, we can use any other integer value instead of 0 to control how long the 
window should wait before automatically closing.
cv2.waitKey(0) 

cv2.destroyAllWindows() is a function from the OpenCV library in Python that is 
important because it closes all the windows that were opened during the program's 
execution. If you do not use cv2.destroyAllWindows(), the windows displaying images or 
any other visual content will remain open even after the program has finished executing,
 which can clutter your screen and potentially cause issues if you are running multiple 
 OpenCV programs. It's good practice to use cv2.destroyAllWindows() to clean up and close
   all the windows opened by your OpenCV program once you are done with them.

cv2.destroyAllWindows() 



'''
