import os
import cv2
import cv2.aruco as aruco

dirPath = "../aruco_codes"

if not os.path.isdir(dirPath):
    try:
        os.mkdir(dirPath)
    except OSError:
        print ("Creation of the directory %s failed" % dirPath)
    else:
        print ("Successfully created the directory %s " % dirPath)

i = 11
while i < 67:
    modulo = i % 10
    levelNum = int((i-modulo) / 10)
    dirPath = "../aruco_codes/level%s" %levelNum
    if modulo == 1:        
        if not os.path.isdir(dirPath):
            try:
                os.mkdir(dirPath)
            except OSError:
                print ("Creation of the directory %s failed" % dirPath)
            else:
                print ("Successfully created the directory %s " % dirPath)

    ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_4X4_100)
    resultFileName = "marker%s.jpg" %i
    img = aruco.drawMarker(ARUCO_DICT, i, 700)
    cv2.imwrite(os.path.join(dirPath, resultFileName), img)
    
    if modulo == 6:
        i = i + 5
    else:
        i = i + 1
