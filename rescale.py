import cv2 as cv

img=cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.5):
    #image video and live video
    width =int(frame.shape[1]*scale)
    height =int(frame.shape[0]*scale)
    dimensions =(width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #work only on live video
    capture.set(3,width)
    capture.set(4,height)


resized_img=rescaleFrame(img)
cv.imshow('Image Resized', resized_img)

capture = cv.VideoCapture('videos/dog.mp4')
#camera video
# capture = cv.VideoCapture(0,cv.CAP_DSHOW)


while True:
    isTrue, frame =capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
