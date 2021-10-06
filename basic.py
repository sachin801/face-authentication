import cv2 as cv

img=cv.imread('Photos/park.jpg')
cv.imshow('Park ', img)
# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray img', gray)

# Blur an image
blur =cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur img',blur)

# Edge Cascade of real image
cany= cv.Canny(img, 125, 175)
cv.imshow('Cany edges', cany)

# Edge cascade of blur image

cany_blur= cv.Canny(blur, 125,175)
cv.imshow('CAny blur', cany_blur)

# dilating the image
dilated =cv.dilate(cany, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# eroding
eroded = cv.erode(dilated,(3,3), iterations=3);
cv.imshow('Eroded', eroded)

# resize    #interpolation inter_area to lower and inter_cubic for higher
resized= cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

#croping
cropped =img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)