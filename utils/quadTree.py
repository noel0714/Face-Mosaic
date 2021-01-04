import numpy as np
import cv2

img = []
imgQuad = []
imgGray = []
quadImg = []


def makeQuad(x1, y1, x2, y2):
    widthHalf = int(np.ceil((y2 + y1) / 2))
    heightHalf = int(np.ceil((x2 + x1) / 2))

    if x2 == heightHalf or y2 == widthHalf:
        mean = imgGray[x1:x2, y1:y2].sum() / (np.absolute(x2 - x1) * np.absolute(y2 - y1))
        msd = np.absolute((imgGray[x1:x2, y1:y2] - mean)).sum()

        if msd < 200:
            quadImg[x1:x2, y1:y2] = mean
            imgQuad[x1:x2, y1:y2] = img[x1, y1]
            return mean, True

        return mean, False


    mean1, isSame1 = makeQuad(x1, y1, heightHalf, widthHalf)
    mean2, isSame2 = makeQuad(x1, widthHalf, heightHalf, y2)
    mean3, isSame3 = makeQuad(heightHalf, y1, x2, widthHalf)
    mean4, isSame4 = makeQuad(heightHalf, widthHalf, x2, y2)

    isSame = isSame1 and isSame2 and isSame3 and isSame4
    mean = (mean1 + mean2 + mean3 + mean4) / 4

    if isSame:
        msd = np.absolute((imgGray[x1:x2, y1:y2] - mean)).sum() / 4

        if msd < 200:
            quadImg[x1:x2, y1:y2] = mean
            imgQuad[x1:x2, y1:y2] = img[x1, y1]
            return mean, True

    return mean, isSame


def oddToEven(img):
    imgWidth = img.shape[0]
    imgHeight = img.shape[1]

    if imgWidth % 2 != 0:
        # 차원수를 맞춰주기 위해 None을 넣어서 3차원으로 만들음
        img = np.vstack((img, img[None, -1, :, :]))

    if imgHeight % 2 != 0:
        img = np.hstack((img, img[:, None, -1, :]))

    return img


def quadSequeance(original):
    global imgGray, quadImg, img, imgQuad

    original = oddToEven(original)
    img = original.copy()
    imgQuad = original.copy()
    imgGray = cv2.cvtColor(original.copy(), cv2.COLOR_BGR2GRAY)
    quadImg = imgGray.copy()

    makeQuad(0, 0, img.shape[0], img.shape[1])

    return imgQuad.copy()


def main():
    original = cv2.imread("../test.jpg")
    temp = quadSequeance(original)

    cv2.imshow("gray", imgGray)
    cv2.imshow("quadImg", quadImg)
    cv2.imshow("img", img)
    cv2.imshow("imgQuad", temp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()