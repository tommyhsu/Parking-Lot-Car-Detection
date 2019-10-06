import numpy as np
import cv2


parking_choose = input('Please input which parkinglot you want to detect (input a or b or 2) :')
if (parking_choose == 'a'):
    path_a = input('Please input image path:')
    #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\rainy\2013-01-21\2013-01-21_07_45_03
    print('parking_', parking_choose, 'Please use cascade_HAAR')
    img = cv2.imread( str(path_a) + '.jpg')
    print( str(path_a) + '.jpg')
    path = (str(path_a) + '.xml')
    car_cascade = cv2.CascadeClassifier(r'C:\Users\Tommy\Anaconda3\Library\bin\xml_ha\cascade_HAAR.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50, 50), maxSize=(100, 100))  ## parking_a and parking_b
if (parking_choose == 'b'):
    path_b = input('Please input image path:')
    print('parking_', parking_choose, 'Please use cascade_HAAR')
    #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\rainy\2013-03-16\2013-03-16_16_45_12
    img = cv2.imread(str(path_b) + '.jpg')
    path = (str(path_b) + '.xml')
    car_cascade = cv2.CascadeClassifier(r'C:\Users\Tommy\Anaconda3\Library\bin\xml_ha\cascade_HAAR.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50, 50),maxSize=(100, 100))  ## parking_a and parking_b

if (parking_choose == '2'):
    path_2 = input('Please input image path:')
    #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking2\rainy\2012-10-26\2012-10-26_08_54_32
    print('parking_', parking_choose, 'Please use cascade_HAAR')
    img = cv2.imread(str(path_2) + '.jpg')
    path = (str(path_2) + '.xml')
    car_cascade = cv2.CascadeClassifier(r'C:\Users\Tommy\Anaconda3\Library\bin\xml_new\cascade_LBP.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.2, 5, minSize=(30, 30))  # ,maxSize = (50, 50), flags = cv2.CASCADE_SCALE_IMAGE) # parking_2

# add this
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()