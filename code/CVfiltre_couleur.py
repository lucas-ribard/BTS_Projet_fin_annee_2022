import cv2
import numpy as np
print("package imported")
def empty(a):
    pass


cv2.namedWindow("Track")
cv2.resizeWindow("Track",640,240)
cv2.createTrackbar("Hue_Min","Track",0,179,empty)
cv2.createTrackbar("Hue_Max","Track",179,179,empty)
cv2.createTrackbar("Sat_Min","Track",0,255,empty)
cv2.createTrackbar("Sat_Max","Track",255,255,empty)
cv2.createTrackbar("Val_Min","Track",0,255,empty)
cv2.createTrackbar("Val_Max","Track",255,255,empty)
while True:
    img = cv2.imread("Ressources/champ.jpg")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue_Min","Track",)
    h_max = cv2.getTrackbarPos("Hue_Max", "Track", )
    s_min = cv2.getTrackbarPos("Sat_Min", "Track", )
    s_max = cv2.getTrackbarPos("Sat_Max", "Track", )
    v_min = cv2.getTrackbarPos("Val_Min", "Track", )
    v_max = cv2.getTrackbarPos("Val_Max", "Track", )


    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgRes = cv2.bitwise_and(img,img,mask=mask)


#afficher l'image
    imgHor = np.hstack((img, imgRes,))
    cv2.imshow("hor", imgHor)
    #cv2.imshow("mask", mask)
    #cv2.imshow("res", imgRes)
    cv2.waitKey(1)