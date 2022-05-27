import cv2 as cv
from cv2 import THRESH_BINARY_INV
import numpy as np
from cv2 import getStructuringElement
img = cv.imread("pipe.jpeg")
a = 10

#img = cv.imread("pipe1.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = cv.equalizeHist(gray)
gray_blurred = cv.blur(gray,(3,3),7)
edges = cv.Canny(gray_blurred,100,200,apertureSize = 3, L2gradient = True)
kernel = np.array(([0,a,a,a,a,a,0],[a,a,a,0,a,a,a],[a,a,0,0,0,a,a],[a,a,a,0,a,a,a],[0,a,a,a,a,a,0]))

edges = cv.dilate(edges,(6,6),iterations= 4)
cv.imshow("edges",edges)
#print(kernel)
filtred_edges = cv.filter2D(edges,2,kernel)
th3 = cv.adaptiveThreshold(edges,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,5,2)
cv.imshow("filtered:",th3)

detected_circles = cv.HoughCircles(th3,                   
cv.HOUGH_GRADIENT_ALT, 3, 19, param1 = 400,
               param2 = 0.2, minRadius = 13, maxRadius = 27)

# detected_circles = cv.HoughCircles(th3,                   
# cv.HOUGH_GRADIENT, 1, 10, param1 = 100,
#                param2 = 50, minRadius = 0, maxRadius = 17)
  
# Draw circles that are detected.
if detected_circles is not None:
  
    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))
  
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        # Draw the circumference of the circle.
        cv.circle(img, (a, b), r, (0, 255, 0), 2)
  
        # Draw a small circle (of radius 1) to show the center.
        cv.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv.imshow("Detected Circle", img)
cv.imshow('Input', img)
#print(len(detected_circles[0]))
cv.waitKey()