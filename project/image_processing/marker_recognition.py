import cv2
import cv2.aruco as aruco
import enum

save_image_counter = 0

class ScalingMode(enum.Enum): 
    PERCENTAGE = 1
    FIX_SIZE = 2
    NO = 3

## Constant parameters
ARUCO_PARAMETERS = aruco.DetectorParameters_create()
ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_4X4_100)


SCALING_PERCENT = 40
FIX_WIDTH = 1280
FIX_HEIGHT = 960

## ________________________________________________________________________

## Program
def marker_recognition(input_img, scalingMode):
    print("0")
    image = input_img
    print("1")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("2")
    # resize image
    if (scalingMode == ScalingMode.PERCENTAGE):   
        print("21") 
        width = int(gray.shape[1] * SCALING_PERCENT / 100)
        height = int(gray.shape[0] * SCALING_PERCENT / 100)
        dim = (width, height)
        resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
    elif (scalingMode == ScalingMode.FIX_SIZE):
        print("22")
        width = FIX_WIDTH
        height = FIX_HEIGHT
        dim = (width, height)
        resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
    else:
        resized = image


    resized = cv2.flip(resized, 1)
    print("3")
    # detect Aruco markers
    corners, ids, rejectedImgPoints = aruco.detectMarkers(resized, ARUCO_DICT, parameters=ARUCO_PARAMETERS)
    print('Ids: ', ids)
    print('Corners: ', corners)
    #print('imgPoints: ', rejectedImgPoints)
    print("4")
    # draw detected markers
    aruco.drawDetectedMarkers(resized, corners, ids)
    aruco.drawDetectedMarkers(resized, rejectedImgPoints, borderColor=(150, 150, 240))
    print("5")
    cv2.imwrite("result_pic.jpg", resized)
    #    save_image_counter = 1
       # cv2.imshow('result_img', resized)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return ids, corners
