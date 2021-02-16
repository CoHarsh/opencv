import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

img = cv2.imread('imges/img1.jpg') # // this will load the image in img variable



img = cv2.resize(img  , (0, 0) ,fx= 0.5, fy = 0.5)  #/*//this will resize the image by mainsize  * 0.5 with both side */

img = cv2.rotate(img , cv2.ROTATE_90_CLOCKWISE )  #this will rotate the image with 90 clockwise

# plt.imshow(img , cmap = 'gray' , interpolation='bicubic')   #this will add images viewer option like zoom or etc

# plt.xticks([]) , plt.yticks([])  #exis value as nil

# plt.show()   #to show our updated img viewer! 
cv2.imshow('window_name',img)    #this will display only img

key = cv2.waitKey(0) #this will hold our img to screen in ms

if key == 27:  #check the condition

    cv2.destroyAllWindows()  #to close all the window

if key == ord('s'):

    cv2.imwrite('newimge.png',img)   #to save the updated img
