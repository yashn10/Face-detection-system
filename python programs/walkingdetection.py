import cv2
from random import randrange as r


data = cv2.CascadeClassifier("../xml files/fullbody.xml")

cam = cv2.VideoCapture("../data/walking.avi")

while True:

    success, video = cam.read()

    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    coordinates = data.detectMultiScale(gray)

    x,y,w,h = coordinates[0]

    cv2.rectangle(video, (x,y), (x+w, y+h), (r(0, 200), r(0, 500), r(0, 300)), 2)

    cv2.imshow("full body detection", video)

    key = cv2.waitKey(1)
    if (key == 81 or key == 113):
        break


cam.release()
print("program running successfully")

