import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
#uint8 is datatype of image
#cv.imshow('blank image', blank)

# #painting image a certain color
# blank[:] = 0,255,0
#
# #blank[200:300, 300:500] = 0,255,0  #for certain portion
# cv.imshow('Green img', blank)

#creating a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

cv.waitKey(0)

#creating a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('circle',blank)
#
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)
#
#
cv.waitKey(0)