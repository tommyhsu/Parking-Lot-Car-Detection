import numpy as np
import cv2
import glob
import os
import xml.dom.minidom
import xml.etree.ElementTree as ET

def create_pos_neg_txt(img_name, file_type, im_width, im_height):

     if file_type == 'Pos':
        line = img_name + ' 1 0 0' + ' ' + str(im_width) + ' ' + str(im_height) +  '\n'
        f = open(r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\Pic_Pos\Pos.txt', 'a')
        f.write(line)
        #print(line)

def main():
    path_a = (r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1a\sunny')
    path_b = (r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking1b\sunny')
    path_2 = (r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\parking2\sunny')
    files = os.listdir(path_a)
    files_b = os.listdir(path_b)
    files_2 = os.listdir(path_2)
    count = 1
    stop = 1
    #print(files)

    for i in range(1, len(files)):
        xml_file = glob.glob(path_a + '\\' + files[i] +  '\\' + '\\*.xml')
        stop += 1
        print(stop)
        if stop > 2:
            break
    # print(path + '\\'   + files[i])
        for j in xml_file:
            print(j)
            image_path, ex = os.path.splitext(j)
            print(image_path)
            img = cv2.imread(image_path + '.jpg')
            #print(img)
            tree = ET.ElementTree(file=j)
            #print(tree)
            root = tree.getroot()
            for space in root:
                num = (space.get('occupied'))
                point_x = []
                point_y = []
                # print(num)
                # print(space.attrib)
                for contour in space.iter('point'):
                    point_x.append(contour.get('x'))
                    point_y.append(contour.get('y'))
                    print(point_x)
                x1 = int(max(point_x))
                x2 = int(min(point_x))
                y1 = int(max(point_y))
                y2 = int(min(point_y))
                # print(x1, x2, y1, y2)
                cropped_img = img[y2:y1, x2:x1]
                rot = np.rot90(cropped_img)
                if num == '1':
                    path_pos = (r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\Pic_Pos')
                    a = cv2.imwrite(os.path.join(path_pos, str(count) + '.jpg'), cropped_img)
                    # print(a)
                    a = cv2.imwrite(os.path.join(path_pos, str(count) + '.jpg'), cropped_img)
                    # print(a)
                    if (a == True):
                        img_name = str(count) + '.jpg'
                        im_width, im_height = np.shape(cropped_img)[:2]
                        # print(im_width,im_height)
                        count += 1
                        # print("pos", count)
                        file_type = 'Pos'
                        create_pos_neg_txt(img_name, file_type, im_width, im_height)
                    b = cv2.imwrite(os.path.join(path_pos, str('ro') +  str(count) + '.jpg'), rot)
                    if (b == True):
                        img_name = 'ro' + str(count) + '.jpg'
                        im_width, im_height = np.shape(rot)[:2]
                        # print(im_width,im_height)
                        count += 1
                        # print("pos", count)
                        file_type = 'Pos'
                        create_pos_neg_txt(img_name, file_type, im_width, im_height)

                # print("1")
    # create_pos_neg_txt()


    stop = 1
    for i in range(1, len(files_b)):
        xml_file = glob.glob(path_b + '\\' + files_b[i] +  '\\' + '\\*.xml')
        stop += 1
        print(stop)
        if stop > 2:
            break
        # print(path + '\\'   + files[i])
        for j in xml_file:
            image_path, ex = os.path.splitext(j)
            img = cv2.imread(image_path + '.jpg')
            # print(j)
            tree = ET.ElementTree(file=j)
            root = tree.getroot()
            for space in root:
                num = (space.get('occupied'))
                point_x = []
                point_y = []
                # print(num)
                # print(space.attrib)
                for contour in space.iter('point'):
                    point_x.append(contour.get('x'))
                    point_y.append(contour.get('y'))
                    # print(point_x)
                x1 = int(max(point_x))
                x2 = int(min(point_x))
                y1 = int(max(point_y))
                y2 = int(min(point_y))
                # print(x1, x2, y1, y2)
                cropped_img = img[y2:y1, x2:x1]
                rot = np.rot90(cropped_img)
                if num == '1':
                    path_pos = (r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\Pic_Pos')
                    a = cv2.imwrite(os.path.join(path_pos, str(count) + '.jpg'), cropped_img)
                    # print(a)
                    if (a == True):
                        img_name =  str(count) + '.jpg'
                        im_width, im_height = np.shape(cropped_img)[:2]
                        # print(im_width,im_height)
                        count += 1
                        # print("pos", count)
                        file_type = 'Pos'
                        create_pos_neg_txt(img_name, file_type, im_width, im_height)
                    b = cv2.imwrite(os.path.join(path_pos,  str('ro') + str(count) + '.jpg'), rot)
                    if (b == True):
                        img_name = 'ro' + str(count) + '.jpg'
                        im_width, im_height = np.shape(rot)[:2]
                        # print(im_width,im_height)
                        count += 1
                        # print("pos", count)
                        file_type = 'Pos'
                        create_pos_neg_txt(img_name, file_type, im_width, im_height)

    stop = 1
    for i in range(1, len(files_2)):
        xml_file = glob.glob(path_2 + '\\' +  files_2[i] + '\\*.xml')
        stop += 1
        print(stop)
        if stop > 3:
            break
        # print(path + '\\'   + files[i])
        for j in xml_file:
            image_path, ex = os.path.splitext(j)
            img = cv2.imread(image_path + '.jpg')
            # print(j)
            tree = ET.ElementTree(file=j)
            root = tree.getroot()
            for space in root:
                num = (space.get('occupied'))
                point_x = []
                point_y = []
                # print(num)
                # print(space.attrib)
                for contour in space.iter('point'):
                    point_x.append(contour.get('x'))
                    point_y.append(contour.get('y'))
                    # print(point_x)
                x1 = int(max(point_x))
                x2 = int(min(point_x))
                y1 = int(max(point_y))
                y2 = int(min(point_y))
                # print(x1, x2, y1, y2)
                cropped_img = img[y2:y1, x2:x1]
                rot = np.rot90(cropped_img)
                if num == '1':
                    path_pos = (r'C:\Users\Tommy\Desktop\Spring_2018\Computer_vision\assignment3_folder\PKLot\Pic_Pos')
                    a = cv2.imwrite(os.path.join(path_pos, str(count) + '.jpg'), cropped_img)
                    # print(a)
                    if (a == True):
                        img_name = str(count) + '.jpg'
                        im_width, im_height = np.shape(cropped_img)[:2]
                        # print(im_width,im_height)
                        count += 1
                        # print("pos", count)
                        file_type = 'Pos'
                        create_pos_neg_txt(img_name, file_type, im_width, im_height)
                    b = cv2.imwrite(os.path.join(path_pos, str('ro') + str(count) + '.jpg'), rot)
                    if (b == True):
                        img_name = 'ro' + str(count) + '.jpg'
                        im_width, im_height = np.shape(rot)[:2]
                        # print(im_width,im_height)
                        count += 1
                        # print("pos", count)
                        file_type = 'Pos'
                        create_pos_neg_txt(img_name, file_type, im_width, im_height)


if __name__ == "__main__":
    main()


