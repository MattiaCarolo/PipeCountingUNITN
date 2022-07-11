# importing the module
import cv2
from cv2 import EVENT_RBUTTONDOWN
import numpy as np

def mouse_handler(event, x, y, flags, data) :
    
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(data['im'], (x,y),3, (0,0,255), 5, 16)
        cv2.imshow("Image", data['im'])
        if len(data['points']) < 4 :
            data['points'].append([x,y])
    '''
    if event == cv2.EVENT_MBUTTONDOWN:
        data['points'].append((0,data['im'].shape[1]))
        data['points'].append((data['im'].shape[0],data['im'].shape[1]))
        data['points'].append((data['im'].shape[0],0))
        data['points'].append((0,0))
    
    '''        
    


def get_four_points(im):
    
    # Set up data to send to mouse handler
    data = {}
    data['im'] = im.copy()
    data['points'] = []
    
    #Set the callback function for any mouse event
    cv2.imshow("Image",im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    cv2.waitKey(0)
    
    # Convert array to np.array
    points = np.vstack(data['points']).astype(float)
    
    return points

def homography(img,img_0):
    points = get_four_points(img)

    print(points)

    size = img.shape

    pts_dst = np.array(
                    [
                        [0,0],
                        [size[0] - 1, 0],
                        [size[0] - 1, size[1] -1],
                        [0, size[1] - 1 ]
                    ], dtype=float)

    h, status = cv2.findHomography(points, pts_dst)
    im_dst = cv2.warpPerspective(img, h, size[0:2])
    im_dst_0 = cv2.warpPerspective(img_0, h, size[0:2])

    cv2.imshow("Image", im_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return im_dst, im_dst_0