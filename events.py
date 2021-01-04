import cv2
import numpy as np
import random

first_x, first_y = 0, 0
click = False

def drawRectangle(e, x, y, flags, param):
    global first_x, first_y, click
    img = param[0]

    '''
    if e == cv2.EVENT_LBUTTONDOWN:
        click = True
        first_x, first_y = x, y
    
    elif e == cv2.EVENT_MOUSEMOVE:
        if click == True:
            #cv2.rectangle(img, (first_x, first_y), (x, y), (random.randrange(256), random.randrange(256), random.randrange(256)))
    '''

    if e == cv2.EVENT_LBUTTONUP:
        #cv2.rectangle(img, (first_x, first_y), (x, y), (random.randrange(256), random.randrange(256), random.randrange(256)))
        param.append([x, y])

if __name__ == "__main__":
    img = cv2.imread("D:/etc prof jang/origin/frame_759.340659.jpg")

    param = []
    cv2.namedWindow("event test")
    cv2.setMouseCallback("event test", drawRectangle, param)

    while True:
        cv2.imshow("event test", img)

        k = cv2.waitKey(1) & 0xFF
        if k == 27: break

    cv2.destroyAllWindows()

    print(param)