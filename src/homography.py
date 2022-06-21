# importing the module
import cv2
import numpy as np

def mouse_handler(event, x, y, flags, data) :
    
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(data['im'], (x,y),3, (0,0,255), 5, 16);
        cv2.imshow("Image", data['im']);
        if len(data['points']) < 4 :
            data['points'].append([x,y])


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

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        i.append((x,y))
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.circle(img,(x,y),5,(255, 0, 0),cv2.FILLED)
        cv2.imshow('image', img)

def homography(img):
    i = list()

    #cv2.imshow('image', img)
    #cv2.setMouseCallback('image', click_event)
    #cv2.waitKey(0)
 
    # close the window
    #cv2.destroyAllWindows()

    points = get_four_points(img)
    #cv2.destroyAllWindows()

    print(points)

    size = (500,600,3)

    pts_dst = np.array(
                    [
                        [0,0],
                        [size[0] - 1, 0],
                        [size[0] - 1, size[1] -1],
                        [0, size[1] - 1 ]
                    ], dtype=float)

    h, status = cv2.findHomography(points, pts_dst)
    im_dst = cv2.warpPerspective(img, h, size[0:2])

    cv2.imshow("Image", im_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return im_dst


# main function to experiment only with homography
if __name__=="__main__":
    
    i = list()

    # reading the image
    img = cv2.imread('data/img15.jpg')
 
    # displaying the image
    cv2.imshow('image', img)
 
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
 
    # close the window
    cv2.destroyAllWindows()

    print(i)

    points = np.vstack(i).astype(float)

    print(points)

    size = (500,600,3)

    pts_dst = np.array(
                    [
                        [0,0],
                        [size[0] - 1, 0],
                        [size[0] - 1, size[1] -1],
                        [0, size[1] - 1 ]
                    ], dtype=float)

    h, status = cv2.findHomography(points, pts_dst)
    im_dst = cv2.warpPerspective(img, h, size[0:2])

    cv2.imshow("Image", im_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()