import numpy as np
import cv2


car_cascade = cv2.CascadeClassifier(r'C:\Users\Tommy\Anaconda3\Library\bin\xml_new\cascade.xml')
img = cv2.imread(r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\rainy\2013-01-21\2013-01-21_07_45_03.jpg')
#img = cv2.imread(r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking2\rainy\2012-09-21\2012-09-21_06_10_10.jpg')
#img = cv2.imread(r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\rainy\2013-01-16\2013-01-16_16_00_12.jpg')
#img = cv2.imread(r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\rainy\2013-02-26\2013-02-26_13_04_33.jpg')
#img = cv2.imread(r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\rainy\2013-03-16\2013-03-16_16_45_12.jpg')
#img = cv2.imread(r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\cloudy\2013-01-19\2013-01-19_07_50_03.jpg')
#img = cv2.imread(r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\rainy\2013-04-13\2013-04-13_07_05_01.jpg')

#while True:
#while True:

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50, 50),maxSize = (100, 100), flags = cv2.CASCADE_SCALE_IMAGE) # for LBP ########## Best ##############
#print(cars)
#cars = car_cascade.detectMultiScale(gray, 1.1, 1, minSize=(50, 50),maxSize = (100, 100), flags = cv2.CASCADE_SCALE_IMAGE) # for LBP
#cars = car_cascade.detectMultiScale(gray, 1.3, 15, minSize=(60, 60),maxSize = (130, 130), flags = cv2.CASCADE_SCALE_IMAGE) # for HAAR

# add this
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()