import cv2
from random import randrange as r


data = cv2.CascadeClassifier('../xml files/cars.xml')

cam = cv2.VideoCapture('../data/video1.avi')


while True:

    success, video = cam.read()

    grayimg = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    coordinates = data.detectMultiScale(grayimg)

    if len(coordinates) > 0:
        x, y, w, h = coordinates[0]
        cv2.rectangle(video, (x, y), (x+w, y+h), (r(0, 200), r(0, 400), r(0, 300)), 2)

    cv2.imshow("live video", video)
    
    key = cv2.waitKey(1)

    if (key == 81 or key == 113):
        break


cam.release()

print("program running successfully")

