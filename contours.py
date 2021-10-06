import cv2 as cv
import numpy as np


img=cv.imread('Photos/cats.jpg')
cv.imshow('Cat ',img)

blank =np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur =cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

cany= cv.Canny(blur, 125, 175)
cv.imshow('CAny image',cany)

# instead of canny edge detector using threshold
ret,thresh =cv.threshold(cany, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours, hierarchies =cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)