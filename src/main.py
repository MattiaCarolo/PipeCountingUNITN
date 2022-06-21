# import the necessary package
from cv2 import bilateralFilter
import matplotlib.pyplot as plt

import numpy as np
import argparse
import cv2 as cv
from homography import homography
from utils import *
CIRCLE_THRESH = 0.2
RECT_THRESH = 0.1

#parser

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="path to image")
args = vars(ap.parse_args())

#image loader
image = cv.imread(args["image"])
image2 = image

fcircle = CircleFilter()
fsquare = SquareFilter()
image_0 = cv.imread(args["image"],0)


image_1 = homography(image_0)


image_bin_0 = binarizeOneChannel(image_1)

Circles = list()
Rects = list()
images = []
contourss0,hierarchy = cv.findContours(image_bin_0,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
i = 0
for cnt in contourss0:#
    (x,y),radius = cv.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    #if radius < 10.0:
    #    continue
    circ = cv.matchShapes(fcircle,cnt,1,0.0)
    rect = cv.matchShapes(fsquare,cnt,1,0.0)

    if circ < 0.075: #precision of the matching
        cnt_x,cnt_y = findCentroid(cnt, image_1, "Circle")
        shape = {"type":"Circle", "centroid":(cnt_x,cnt_y)}
        #print("cerchio", circ)
        Circles.append(shape)
    if rect < 0.082:    #0.082 img15
        cnt_x,cnt_y = findCentroid(cnt,image_1, "Rectangle")
        shape = {"type":"Rectangle", "centroid":(cnt_x,cnt_y)}
        #print("rectangle",rect)
        Rects.append(shape)
    #i += 1
    #cv.imwrite("./GIFimages/" + str(i) + ".jpg", image)
    #images.append(imageio.imread("../GIFimages/" + str(i) + ".jpg"))
    

print("rect count: ",len(Rects))
print("circle count: ",len(Circles))
"""
circles = cv.HoughCircles(image_bin_0,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=40)

for i in circles[0,:]:
    # draw the outer circle
    cv.circle(image2,(i[0],i[1]),i[2],(255,0,0),2)
    # draw the center of the circle
    cv.circle(image2,(i[0],i[1]),2,(255,0,0),3)
"""
cv.imshow("source",image_0)
cv.imshow("thresh",image_bin_0)
#cv.imshow("result",image)
cv.imshow("houghes",image_1)
#imageio.mimsave('./movie.gif', images)

cv.waitKey()
cv.destroyAllWindows() 




"""
legacy method
c = 0
r = 0
Circles = list()
Rects = list()

image_bin = binarize(image)
cv.imshow("thresh",image_bin)

contourss,hierarchy = cv.findContours(image_bin,2,cv.CHAIN_APPROX_SIMPLE)


for cnt in contourss:

    circ = cv.matchShapes(fcircle,cnt,1,0.0)
    rect = cv.matchShapes(fsquare,cnt,1,0.0)

    if circ < 0.0079: #precision of the matching
        cnt_x,cnt_y = findCentroid(cnt, image)
        shape = {"type":"Circle", "centroid":(cnt_x,cnt_y)}
        c += 1
        print("cerchio", circ)
        Circles.append(shape)
    if rect < 0.00045:    #0.082 img15
        cnt_x,cnt_y = findCentroid(cnt,image)
        shape = {"type":"Rectangle", "centroid":(cnt_x,cnt_y)}
        r += 1
        print("rectangle",rect)
        Rects.append(shape)

print("rect count: ",r)
print("circle count: ",c)

cv.imshow("img",image)
#cv.waitKey()
#cv.destroyAllWindows() 
"""
