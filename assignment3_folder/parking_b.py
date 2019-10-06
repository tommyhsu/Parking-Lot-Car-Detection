import numpy as np
import cv2
import glob
import os
import xml.dom.minidom
import xml.etree.ElementTree as ET

def create_pos_neg_txt(img_name, file_type, im_width, im_height):

    if file_type == 'Neg':
        path = r'C:\Users\Tommy\Anaconda3\Library\bin\Neg'
        #open('Neg.txt')
        line =  path + '\\' +  img_name + '\n'
        #print(line)
        f = open(r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\Neg_Pos\Neg\Neg.txt','a')
        f.write(line)
        #print(line)

    elif file_type == 'Pos':
        line = img_name + ' 1 0 0' + ' ' + str(im_width) + ' ' + str(im_height) +  '\n'
        f = open(r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\Neg_Pos\Pos\Pos.txt', 'a')
        f.write(line)
        #print(line)

def main():
    path = (r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\sunny')
    files = os.listdir(path)
    #print(files)
    count = 1
    stop = 1
    #print(files)
    for i in range(1, len(files)):
        xml_file = glob.glob(path + '\\'  + files[i] +  '\\*.xml' )
        stop += 1
        print(stop)
        if stop > 4:
            break
        #print(path + '\\'   + files[i])
        for j in xml_file:
            image_path, ex = os.path.splitext(j)
            img = cv2.imread(image_path + '.jpg')
            #print(j)
            tree = ET.ElementTree(file = j)
            root = tree.getroot()
            for space in root:
                num = (space.get('occupied'))
                point_x = []
                point_y = []
                #print(num)
                #print(space.attrib)
                for contour in space.iter('point'):
                    point_x.append(contour.get('x'))
                    point_y.append(contour.get('y'))
                    #print(point_x)
                x1 = int(max(point_x))
                x2 = int(min(point_x))
                y1 = int(max(point_y))
                y2 = int(min(point_y))
                #print(x1, x2, y1, y2)
                cropped_img = img[y2:y1, x2:x1]
                if num == '0':
                    path_neg = (r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\Neg_Pos\Neg\Neg_img')
                    a = cv2.imwrite(os.path.join(path_neg, str(count) +  '.jpg'), cropped_img)
                    #print(a)
                    if (a == True):
                        img_name = str(count) + '.jpg'
                        #print(img_name)
                        count += 1
                        #print("neg",count)
                        file_type = 'Neg'
                        create_pos_neg_txt(img_name, file_type,0,0)
                if num == '1':
                    path_pos = (r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\Neg_Pos\Pos\Pos_img')
                    #cropped_img = cv2.resize(cropped_img,(30,30))
                    a = cv2.imwrite(os.path.join(path_pos, str(count) +  '.jpg'), cropped_img)
                    #print(count,a)
                    if (a == True ):
                        img_name = str(count) + '.jpg'
                        #print(img_name)
                        im_width, im_height = np.shape(cropped_img)[:2]
                        count += 1
                        #print("pos", count)
                        file_type = 'Pos'
                        create_pos_neg_txt(img_name, file_type, im_width, im_height)
                    #print("1")
    #create_pos_neg_txt()
if __name__ == "__main__":
    main()


