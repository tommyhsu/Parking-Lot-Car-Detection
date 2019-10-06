import numpy as np
import cv2
import glob
import os
import xml.dom.minidom
import xml.etree.ElementTree as ET



def main():
    path_a = (r'C:\Users\Tommy\Anaconda3\Library\bin\pos_hum_1')
    files_a = os.listdir(path_a)
    i = 0
    for files in files_a:
        line = (  files  + ' 1 0 0 40 40' + '\n')
        f = open(r'C:\Users\Tommy\Anaconda3\Library\bin\pos_hum_1\pos_hum.txt', 'a')
        f.write(line)
        i += 1
    #print(files_a[0])


if __name__ == "__main__":
    main()


