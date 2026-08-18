# Refer - https://www.geeksforgeeks.org/invisible-cloak-using-opencv-python-project/
# Github: https://github.com/AdityaAtri/invisible_man/blob/master/video.mp4

'''Here, we will create this magical experience using an image 
processing technique called color detection and segmentation.

In order to run this code , you need a mp4 video named "video.mp4". 
You must have a cloth of same color and no other color should be there. 
I am taking red cloth.'''

import cv2
import numpy as np
import time

print(cv2.__version__)#not necessary


# use relative path or put the file & video in same folder
raw_video = cv2.VideoCapture('videos/video.mp4')

# Use red cloth, to make u invisible
#raw_video = cv2.VideoCapture(0) # to use system cam
time.sleep(1)
count = 0
background = 0


# The video has some seconds in the starting where 
# the background is completely visible, 
# Capturing that backgrund which would be used for masking later.
for i in range(60):#capturing the background the 1st 60 frames
    return_val, background = raw_video.read()#reads a frame from 
                                       #the video capture object
    if return_val == False:#if the frame is read successfully
        continue
# To join hands one hand has to be the mirror image of the other.

background = np.flip(background, axis = 1)#horizontally flips the
                            #last successfully read frame.

'''axis=0 → rows (vertical direction)
axis=1 → columns (horizontal direction)'''

# we are reading from video 
while(raw_video.isOpened()):#chks if video capture object (raw_video)
    return_val, img = raw_video.read()#reads next frame from video
    if not return_val:#If no frame is read
        break #loop breaks
    count += 1#Counts the number of successfully read frames
    img = np.flip(img, axis = 1)#Horizontally flips 
                       #frame (like a mirror image).

    # BGR=Blue,Green,Red  . HSV= Hue Saturation Value
    ''' 
    Hue range is [0,179], Saturation range is [0,255] 
    and Value range is [0,255]
    
    HSV is better in color detection than BGR'''
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#Convert BGR to HSV
    '''
    Red is located at two regions on the hue spectrum:
    0° to ~10° (Lower red)
    ~170° to 180° (Upper red)
    To capture the full red range, you need to combine two masks.'''
    
    # Define  red ranges in HSV
    lower_red1 = np.array([100, 40, 40])
    upper_red1 = np.array([100, 255, 255])
    #Create masks for both red regions
    
    # detect red
    lower_red2 = np.array([155, 40, 40])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask1 = mask1 + mask2

    red_mask = cv2.bitwise_or(mask1, mask2)
    '''
    A bitwise OR compares two binary numbers bit by bit.
    If either bit is 1, the result is 1; otherwise 0.
    🧠 Example (for single bits):
        Bit A	Bit B	A OR B
        0	0	0
        0	1	1
        1	0	1
        1	1	1'''

    # Refining the mask corresponding to the detected red color
    # For refining the image as image is raw and 
    # blurry after processing in HSV format

    # Remove noise with morphological opening.
    # Purpose: Removes small noise from the binary mask.
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, 
                            np.ones((3,3), np.uint8), iterations = 2)
                    #iterations = 2: Repeats operatn twice for a stronger effect.
    # Expand detected region
    mask1 = cv2.dilate(mask1, np.ones((3,3), np.uint8), iterations = 1)
    # Invert the mask
    mask2 = cv2.bitwise_not(mask1)

    # Generating the final output
    # The masking happens here. You are adding 2 images together
    res1 = cv2.bitwise_and(background, background, mask = mask1)
    res2 = cv2.bitwise_and(img, img, mask = mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    cv2.imshow("INVISIBLE MAN", final_output)
  
    if cv2.waitKey(5) == ord('q'):# press q to close output scrn
        break

        #OR
    '''
    k = cv2.waitKey(10)
    if k == 27:# 27 - Esc key
        break
    '''
    #=======================
'''
In OpenCV, the Hue (H) value ranges from 0 to 179 (not 0-360 as in the standard HSV model):

Color	        Hue(H) Range (in OpenCV)   Saturation(S)  Value(V)
Red	            0-10 and 170-180            40 - 255      40 - 255

Light Green	    35-85                       40 - 255     40 - 255
Pure Green	    50 - 85
Dark Green	    85 - 100                    40 - 255      20 - 255 (darker)

Blue	        90-130
Yellow	        0-35

'''
