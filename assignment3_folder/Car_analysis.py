import numpy as np
import cv2
import xml.etree.ElementTree as ET

def main():
    while(1):
        parking_choose = input('Please input which parkinglot you want to detect (input a or b or 2) :')
        if (parking_choose == 'a'):
            path_a = input('Please input image path:')
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\cloudy\2013-01-16\2013-01-16_07_40_03
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\cloudy\2013-01-16\2013-01-16_17_45_14
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\cloudy\2012-12-12\2012-12-12_10_00_05
            # C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\cloudy\2012-12-12\2012-12-12_11_10_06
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\rainy\2013-01-21\2013-01-21_07_40_02
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\rainy\2013-01-21\2013-01-21_09_25_04
            # C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\rainy\2013-01-21\2013-01-21_08_15_03
            # C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\rainy\2013-01-21\2013-01-21_10_30_05
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
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\cloudy\2013-03-15\2013-03-15_06_35_00
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\cloudy\2013-03-15\2013-03-15_07_15_01
            # C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\cloudy\2013-03-15\2013-03-15_07_55_02
            # C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\cloudy\2013-03-15\2013-03-15_15_45_11
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\rainy\2013-03-19\2013-03-19_06_30_00
            # C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\rainy\2013-03-19\2013-03-19_07_25_01
            # C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\rainy\2013-03-19\2013-03-19_12_50_07
            img = cv2.imread(str(path_b) + '.jpg')
            path = (str(path_b) + '.xml')
            car_cascade = cv2.CascadeClassifier(r'C:\Users\Tommy\Anaconda3\Library\bin\xml_ha\cascade_HAAR.xml')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50, 50),maxSize=(100, 100))  ## parking_a and parking_b

        if (parking_choose == '2'):
            path_2 = input('Please input image path:')
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking2\rainy\2012-10-26\2012-10-26_08_54_32
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking2\rainy\2012-10-26\2012-10-26_07_24_27
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking2\cloudy\2012-10-31\2012-10-31_11_28_13
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking2\rainy\2012-09-16\2012-09-16_06_22_55
            #C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking2\cloudy\2012-11-08\2012-11-08_12_00_40
            print('parking_', parking_choose, 'Please use cascade_HAAR')
            img = cv2.imread(str(path_2) + '.jpg')
            path = (str(path_2) + '.xml')
            car_cascade = cv2.CascadeClassifier(r'C:\Users\Tommy\Anaconda3\Library\bin\xml_ha\cascade_HAAR.xml')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.2, 5, minSize=(30, 30))  # ,maxSize = (50, 50), flags = cv2.CASCADE_SCALE_IMAGE) # parking_2

        xml_file = ET.ElementTree(file=path)
        root = xml_file.getroot()
        count_TP = 0
        num_occ = 0
        count_FP = 0
        for child in root:
            num = (child.get('occupied'))
            point_x = []
            point_y = []
            for contour in child.iter('point'):
                point_x.append(contour.get('x'))
                point_y.append(contour.get('y'))
                #print(point_x)
                #print(point_y)
            x1 = int(max(point_x))
            x2 = int(min(point_x))
            y1 = int(max(point_y))
            y2 = int(min(point_y))
            cropped_img = img[y2:y1, x2:x1]
            #print(cropped_img)
            b = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0 , 0), 2)
            if (num == '1'):
                num_occ += 1
            for (x, y, w, h) in cars:
                cropped_img_g = img[y:y+h, x:x+w]
                #print(cropped_img)
                area_1 = (x1 - x2) * (y1 - y2)
                area_2 = (w) * (h)
                dx = min(x1, x+w) - max(x2, x)
                dy = min(y1, y + h) - max(y2, y)
                if (dx >= 0 and dy >= 0):
                    area_inter = dx * dy
                else:
                    area_inter = 0

                area_union = area_1 + area_2 - area_inter
                overlap =  float(area_inter / area_union)
                #print(overlap)
                mean_x = int(x + w / 2)
                mean_y = int(y + h / 2)
                if(overlap > 0.5):
                #if ((mean_x> x2 and mean_x < x1) and (mean_y > y2 and mean_y < y1)):
                    g = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    #print(g)
                    count_TP += 1
                else:
                    r =  cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255 ), 1)

        print('TP:',count_TP)
        print('num of occ:',num_occ)
        if(num_occ != 0):
            accuracy = (count_TP/num_occ) * 100
            ACC = str('accuracy :' + str(accuracy)[:5] + '%')
            print(ACC)
            cv2.imshow('img', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if(num_occ == 0):
            print('100%')
            cv2.imshow('img', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()