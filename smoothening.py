import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Real', img)

# Averaging
average = cv.blur(img,(3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur -- weight is added to surrounding
gauss_blur=cv.GaussianBlur(img,(3,3), 0)
cv.imshow('Gaussian blur', gauss_blur)

# median Blur --more effective removing noises
median_blur = cv.medianBlur(img, 3) # kernel size only one number(3)
cv.imshow('Median Blur',median_blur)

# bilateral blur ---used in more advance cv projects
bilateral =cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur ',bilateral)

cv.waitKey(0)