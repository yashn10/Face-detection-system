import cv2
from random import randrange as r


data = cv2.CascadeClassifier('../xml files/face.xml')

webcam = cv2.VideoCapture(0)

while True:

    success, image = webcam.read()

    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    coordinates = data.detectMultiScale(grayimg)

    x,y,w,h = coordinates[0];

    cv2.rectangle(image, (x,y), (x+w, y+h), (r(0, 220), r(0, 220), r(0, 555)), 2)

    cv2.imshow("live video", image)
    key = cv2.waitKey(1)

    if(key == 81 or key == 113):
     break


webcam.release()

print("program running successfully")
