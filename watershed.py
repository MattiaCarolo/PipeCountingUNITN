# import the necessary package

from skimage.feature import peak_local_max
from skimage.segmentation import watershed

from scipy import ndimage
import matplotlib.pyplot as plt

import numpy as np
import argparse
import imutils
import cv2
from urllib3 import connection_from_url

#construct the argument parse and parse the arguments


#parser

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="path to image")
args = vars(ap.parse_args())

#image loader
image = cv2.imread(args["image"])
shifted = cv2.pyrMeanShiftFiltering(image,21,51)
#cv2.imshow("Input",shifted)

gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#cv2.imshow("Thresh", thresh)
#cv2.waitKey(0)

"""
compute the exact euclidean distance from every binary pixel
to the nearest zero pixel, then find peaks in this distance map

----

perform a connected component analyssi on the local peaks,
using 8-connectivity, then apply watershed algorithm
"""
D = ndimage.distance_transform_edt(thresh)
localMax = peak_local_max(D,indices=False, min_distance=20, labels=thresh)

# ----

markers = ndimage.label(localMax,structure=np.ones((3,3)))[0]
labels = watershed (-D, markers, mask=thresh)
print("[INFO] {} unique segments found".format(len(np.unique(labels)) - 1))

#loop over watershed labels

for label in np.unique(labels):
    if label == 0:
        continue
    
    # draw label region on the mask
    mask = np.zeros(gray.shape, dtype="uint8")
    mask[labels == label] = 255

    #detect countour on mask and take the largest
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts=cnts)
    c = max(cnts, key = cv2.contourArea)

    #draw a circle enclosing the object
    ((x,y), r) = cv2.minEnclosingCircle(c)
    cv2.circle(image, (int(x), int(y)), int(r), (0,255,0), 2)
    cv2.putText(image, "#{}".format(label),(int(x)-10, int(y)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,255), 2)


cv2.imshow("output", image)
cv2.waitKey(0)