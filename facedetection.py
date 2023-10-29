import cv2
from random import randrange as r

data = cv2.CascadeClassifier('face.xml');

# image = cv2.imread('painter1.png');

webcam = cv2.VideoCapture(0);

while True:

   success, image = webcam.read();

   # cv2.imshow("painter hai be",image);
   # cv2.waitKey();

   grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
   # cv2.imshow("painter hai be", grayimg);
   # cv2.waitKey();

   coordinates = data.detectMultiScale(grayimg);

   x,y,w,h = coordinates[0];

   cv2.rectangle(image, (x,y), (x+w, y+h), (r(0, 200), r(0, 200), r(0, 200)), 2);

   # cv2.imshow("painter hai be", image);
   cv2.imshow("main hu be", image);
   key = cv2.waitKey(1);

   if(key == 81 or key == 113):
    break


webcam.release();

print("project running successfully");

