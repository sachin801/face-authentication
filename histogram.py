import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img= cv.imread('Photos/cats.jpg')
cv.imshow('Real', img)

blank= np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask= cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', mask)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray ', gray)

# grayscale histogram
gray_hist =cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Graysacle histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

masked = cv.bitwise_and(gray, gray, mask= mask)
cv.imshow('Masked', masked)
masked_hist= cv.calcHist([gray], [0], masked, [256], [0,256])

plt.figure()
plt.title('Masked img histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(masked_hist)
plt.xlim([0,256])
plt.show()

# colour histogram
plt.figure()
plt.title('color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ['b', 'g', 'r']
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
# similarly we can do for masked color images but we need to mask instead of masked in place of  None

cv.waitKey(0)