import numpy as np
import cv2 as cv

CIRCLE_THRESH = 0.2
RECT_THRESH = 0.1


def findCentroid(cnt,image, type):
    M = cv.moments(cnt)
    cnt_x = int(M["m10"]/M["m00"])
    cnt_y = int(M["m01"]/M["m00"])

    cv.circle(image, (cnt_x, cnt_y), 7, (0, 255, 0), -1)
    cv.drawContours(image, [cnt], -1, (0, 0, 255), 2)
    cv.putText(image, type , (cnt_x - 20, cnt_y - 20),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)

    return cnt_x, cnt_y


def binarize(image):
    bilateral = cv.bilateralFilter(image,5,150,150)
    #gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image = cv.equalizeHist(bilateral)
    image = cv.blur(image, (3,3))
    ret, thresh2 = cv.threshold(image, 127, 255,0) 
    canny = cv.Canny(bilateral,100,225,apertureSize=3) # canny on the binary of the img1
    return canny

def binarizeOneChannel(image):
    image = cv.equalizeHist(image)
    image = cv.blur(image, (3,3))
    ret, thresh2 = cv.threshold(image, 127, 255,0) 
    canny = cv.Canny(thresh2,200,450,apertureSize=3) # canny on the binary of the img1
    return canny

def CircleFilter():
    canvas = np.zeros((300, 300, 1), dtype="uint8")
    cv.circle(canvas,(150,150),100,(200,0,0),1)
    ret, circle_ref = cv.threshold(canvas, 127, 255,0)
    cv.imshow("circle ref",canvas)
    contours_circle,hierarchy = cv.findContours(circle_ref,2,1)
    return contours_circle[0]

def SquareFilter():
    canvas2 = np.zeros((600, 600, 1), dtype="uint8")
    cv.rectangle(canvas2,(10,10),(590,590),(200,0,0),9)
    ret, square_ref = cv.threshold(canvas2,127,255,0)
    cv.imshow("req ref",canvas2)
    contours_rect,hierarchy = cv.findContours(square_ref,2,1)
    return contours_rect[0]
