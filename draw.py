import cv2 as cv
import numpy as np

blank=np.zeros((500,500),dtype='uint8')
#uint8 is datatype of image
cv.imshow('blank image', blank)
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)


cv.waitKey(0)