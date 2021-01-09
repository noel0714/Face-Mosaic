import cv2


if __name__ == "__main__":
    trackerKCF = cv2.TrackerKCF_create()
    videoCapture = cv2.VideoCapture(0)

    for i in range(5):  # 5회 반복한다.
        _, frameNDArray = videoCapture.read()
        trackObjectTuple = cv2.selectROI("select", frameNDArray)  # 추적할 객체를 마우스로 드래그해 선택하고 스페이스 키나 엔터 키를 누른다. (시작점(y, x), width, height)
        result = trackerKCF.init(frameNDArray, trackObjectTuple)

    cv2.destroyAllWindows()

    while True:
        _, frameNDArray = videoCapture.read()
        isUpdated, trackObjectTuple = trackerKCF.update(frameNDArray)

        if isUpdated:
            x1 = (int(trackObjectTuple[0]), int(trackObjectTuple[1]))
            x2 = (int(trackObjectTuple[0] + trackObjectTuple[2]), int(trackObjectTuple[1] + trackObjectTuple[3]))

            cv2.rectangle(frameNDArray, x1, x2, (255, 0, 0), 2)

        cv2.imshow("track object", frameNDArray)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    videoCapture.release()
    cv2.destroyAllWindows()
