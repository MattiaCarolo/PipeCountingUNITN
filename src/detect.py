from imagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2
import numpy as np


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# Kernel for edge enhancement
kernel = np.array([[0, 2 ,2 ,2, 0],
                   [2, 0, 0, 0, 2],
				   [2, 0, 0, 0, 2],
                   [2, 0, 0, 0, 2],
				   [0, 2 ,2 ,2, 0]])


# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread(args["image"])

#resized = imutils.resize(image, width=300)
#ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equ = cv2.equalizeHist(gray)
cannied = cv2.Canny(image,500,600,apertureSize=3)
#edges = cv2.dilate(cannied,(5	,5),iterations= 10)

#Edge enhancement 
#edges = cv2.filter2D(src=cannied, ddepth=-1, kernel=kernel)
cv2.imshow("Image", cannied)

cv2.waitKey(0)

blurred = cv2.GaussianBlur(cannied, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print(cnts)
print(len(cnts))
sd = ShapeDetector()

# loop over the contours
for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]))  #* ratio)
	cY = int((M["m01"] / M["m00"]) )#* ratio)
	shape = sd.detect(c)
	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	#c = c.astype("float")
	#c *= ratio
	#c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)

# show the output image and intermediate steps

cv2.imshow("Image", cannied)

cv2.waitKey(0)

cv2.imshow("Image", image)

#Hori = np.concatenate((edges, image), axis=1)

#cv2.imshow("Steps", Hori)

cv2.waitKey(0)