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


from only_contours import *
from pipe_counting import *
from shape_detect import *
from watershed import *

#construct the argument parse and parse the arguments
#parser

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="path to image")
ap.add_argument("-p","--preprocessing", required=True, help="type of preprocessing")
args = vars(ap.parse_args())
