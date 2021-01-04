import cv2
import numpy as np
import os
import events

lower = np.array([0, 48, 80], dtype="uint8")
upper = np.array([20, 255, 255], dtype="uint8")
path = "D:/etc prof jang/origin/"


def readDir():
    global path

    list = os.listdir(path)
    imgList = [l for l in list if l.endswith(".jpg")]

    return imgList


def faceColor(img):
    global lower, upper

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    faceColorImg = cv2.inRange(hsv, lower, upper)

    return faceColorImg


def myshow(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getFaceImg(img, b0, b1, b2, b3):
    return img[b0 : b2, b1 : b3]


def doBilateralFiltering(img, b0, b1, b2, b3):
    biImg = cv2.bilateralFilter(img, 27, 80, 9)
    faceImg = getFaceImg(biImg, b0, b1, b2, b3)
    faceImg = cv2.resize(faceImg, dsize=(64, 64), interpolation=cv2.INTER_AREA)

    return biImg, faceImg


if __name__ == "__main__":
    imgList = readDir()

    for i in imgList:
        print("full path : {}".format(path + i))
        img = cv2.imread(path + i, cv2.IMREAD_COLOR)

        param = [img]
        cv2.namedWindow("bilateral filter")
        cv2.setMouseCallback("bilateral filter", events.drawRectangle, param)

        while True:
            cv2.imshow("bilateral filter", img)

            k = cv2.waitKey(1) & 0xFF
            if k == 27: break

        print(param[1:])

        '''
        biImg = doBilateralFiltering(img)
        myshow("bilateral filter", biImg)
        '''
