from turtle import color
import cv2 as cv
from cv2 import imshow
from cv2 import matchShapes
import numpy as np

"""img used for testing are img15 (88 square pipes) and img16 (35 round pipes)"""
img1 = cv.imread('./data/img16.jpg',0)  #img7.jpg 48 pipe. img15 88 square pipe
img1 = cv.equalizeHist(img1)
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
for cnt in contourss:
    circ = cv.matchShapes(cnt1,cnt,1,0.0)
    rect = cv.matchShapes(cnt2,cnt,1,0.0)
    if circ < 0.0079: #precision of the matching
        c += 1
        print("cerchio", circ)
    if rect < 0.00045:    #0.082 img15
        r += 1
        print("rectangle",rect)
print("rect count: ",r)
print("circle count: ",c)

cv.imshow("img",thresh2)
cv.waitKey()