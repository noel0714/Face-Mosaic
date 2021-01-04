author = "noel0714"

import cv2
import os
import bilateralFiltering as BF
import random_forest as RF
import test_widerface as TW


def isVideo(video):
    if not video.isOpened():
        print("The Video does not opened")
        exit()


def getImage(video):
    retval, img = video.read()

    if not retval:
        print("There are no grabbed image")
        exit()

    return img


def showImage(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    TW.initFaceDetector()

    path = "../videos/moon_frame blend.avi"
    video = cv2.VideoCapture(path)
    isVideo(video)

    img_info = []
    images = []
    count = 0

    while True:
        img = getImage(video)

        count += 1
        face_img, face_info = TW.findFace(img)
        img_info.append(face_info)
        images.append(img_info)

        showImage(face_img)



if __name__ == "__main__":
    main()