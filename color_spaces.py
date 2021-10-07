import cv2 as cv
import matplotlib.pyplot as plt



img=cv.imread('Photos/park.jpg')
cv.imshow('Real', img)

# plt.imshow(img)
# plt.show()

# BGR to grayscale
gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv= cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB ', lab)

# BGR to RGB
rgb =cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()
# note:- opencv follows rgb

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr', hsv_bgr)
# similarly we can do with others



cv.waitKey(0)