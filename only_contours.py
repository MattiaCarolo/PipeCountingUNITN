from __future__ import print_function
from scipy.fftpack import shift
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage

import argparse
import imutils
import cv2

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

cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#loop over countours
for(i,c) in enumerate(cnts):
    ((x,y), _) = cv2.minEnclosingCircle(c)
    cv2.putText(image, "#{}".format(i + 1), (int(x) - 10, int(y)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv2.drawContours(image, [c], -1, (0,255,0), 2)

cv2.imshow("Image", image)

cv2.waitKey(5000)
cv2.destroyAllWindows()