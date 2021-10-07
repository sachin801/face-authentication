import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Real ', img)

blank =np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue= cv.merge([b,blank,blank])
green =cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('Blue blank',blue)
cv.imshow('Green blank',green)
cv.imshow('Red blank',red)
#merging above three will real image
 
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged= cv.merge([b,g,r])
cv.imshow('megred', merged)

cv.waitKey(0)
