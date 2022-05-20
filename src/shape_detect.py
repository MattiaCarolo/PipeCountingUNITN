import cv2
import numpy as np

# Load image
image = cv2.imread('img6.jpg', 0)
image = cv2.equalizeHist(image)
#image = cv2.Canny(image,500,600,apertureSize=3)
#image = cv2.dilate(image,(2,2),iterations=10)
# Set our filtering parameters
# Initialize parameter setting using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters
params.filterByArea = True
params.minArea = 100
params.maxArea = 500

# Set Circularity filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.3
params.maxCircularity = 1

# Set Convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.8
params.maxConvexity = 1

	
# Set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.3
params.maxInertiaRatio = 0.8

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
	
# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255),
						cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550),
			cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
print(text)
# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()

