import cv2 as cv
import numpy as np

img= cv.imread('Photos/cats.jpg')
cv.imshow('Real ', img)

blank = np.zeros((img.shape[:2]), dtype='uint8')
cv.imshow('Blank ', blank)

mask= cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, 255, -1)
cv.imshow('MAsk', mask)

masked= cv.bitwise_and(img, img, mask=mask)
cv.imshow('MAsked', masked)


cv.waitKey(0)