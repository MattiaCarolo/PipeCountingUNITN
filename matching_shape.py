from turtle import color
import cv2 as cv
from cv2 import imshow
from cv2 import matchShapes
from matplotlib import image
import numpy as np


def findCentroid(cnt,image):
    M = cv.moments(cnt)
    cnt_x = int(M["m10"]/M["m00"])
    cnt_y = int(M["m01"]/M["m00"])

    cv.circle(image, (cnt_x, cnt_y), 7, (0, 255, 0), -1)
    cv.drawContours(image, [cnt], -1, (0, 0, 255), 2)

    return cnt_x, cnt_y


"""img used for testing are img15 (88 square pipes) and img16 (35 round pipes)"""
image1 = cv.imread('./data/img16.jpg',0)  #img7.jpg 48 pipe. img15 88 square pipe
#gray = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
img1 = cv.equalizeHist(image1)
img1 = cv.blur(img1, (3,3))

#creation of the circle and square to use as a reference for the matching
canvas = np.zeros((300, 300, 1), dtype="uint8")
canvas2 = np.zeros((600, 600, 1), dtype="uint8")

circle = cv.circle(canvas,(150,150),100,(200,0,0),10)
rect = cv.rectangle(canvas2,(10,10),(590,590),(200,0,0),9)

cv.imshow("circle ref",canvas)
cv.imshow("rectangle ref",canvas2)

ret, circle_ref = cv.threshold(canvas, 127, 255,0)
ret, square_ref = cv.threshold(canvas2,127,255,0)


#extracting contours of the circle and square reference
contours_circle,hierarchy = cv.findContours(circle_ref,2,1)
contours_rect,hierarchy = cv.findContours(square_ref,2,1)

cnt1 = contours_circle[0]
# computing contours and extracting contours and hierarchy of the image
ret, thresh2 = cv.threshold(img1, 127, 255,0) 
a = cv.Canny(thresh2,200,450,apertureSize=3) # canny on the binary of the img1
contourss,hierarchy = cv.findContours(a,2,1)

cv.imshow("canny",a)

cnt2 = contours_rect[0]
# c,r are the variable for the counting (circle, rectangle)
c = 0
r = 0
Circles = list()
Rects = list()
for cnt in contourss:

    circ = cv.matchShapes(cnt1,cnt,1,0.0)
    rect = cv.matchShapes(cnt2,cnt,1,0.0)
    if circ < 0.0079: #precision of the matching
        cnt_x,cnt_y = findCentroid(cnt, image1)
        shape = {"type":"Circle", "centroid":(cnt_x,cnt_y)}
        c += 1
        print("cerchio", circ)
        Circles.append(shape)
    if rect < 0.00045:    #0.082 img15
        cnt_x,cnt_y = findCentroid(cnt,image1)
        shape = {"type":"Rectangle", "centroid":(cnt_x,cnt_y)}
        r += 1
        print("rectangle",rect)
        Rects.append(shape)

print("rect count: ",r)
print("circle count: ",c)

cv.imshow("img",image1)
cv.waitKey()