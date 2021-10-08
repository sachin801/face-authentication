import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('CAts', img)

gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRay', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple threshold', thresh)

# inverse simple thresholding

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse threshold', thresh_inv)

# Adaptive thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11, 3)
cv.imshow('Adaptive threshold', adaptive_thresh)

# instead of ADATIVE_THRESH_MEAN_C we can use ADAPTIVE_THRESH_GAUSSIAN_C
cv.waitKey(0)
