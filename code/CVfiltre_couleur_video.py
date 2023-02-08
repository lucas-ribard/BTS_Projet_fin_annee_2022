import cv2
import numpy as np
def empty(a):
    pass

# lien de la cam  ; http://username:password@ip
url = "http://admin:pwe9vv@10.201.36.161:80/videostream.cgi"
kernel = np.ones((3,3),np.uint8)
# open the feed
cap = cv2.VideoCapture(url)

cv2.namedWindow("Track")
cv2.resizeWindow("Track", 640, 240)
cv2.createTrackbar("Hue_Min", "Track", 0, 179, empty)
cv2.createTrackbar("Hue_Max", "Track", 179, 179, empty)
cv2.createTrackbar("Sat_Min", "Track", 0, 255, empty)
cv2.createTrackbar("Sat_Max", "Track", 255, 255, empty)
cv2.createTrackbar("Val_Min", "Track", 0, 255, empty)
cv2.createTrackbar("Val_Max", "Track", 255, 255, empty)
while True:
    # read next frame
    ret, frame = cap.read()



    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue_Min", "Track", )
    h_max = cv2.getTrackbarPos("Hue_Max", "Track", )
    s_min = cv2.getTrackbarPos("Sat_Min", "Track", )
    s_max = cv2.getTrackbarPos("Sat_Max", "Track", )
    v_min = cv2.getTrackbarPos("Val_Min", "Track", )
    v_max = cv2.getTrackbarPos("Val_Max", "Track", )

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgRes = cv2.bitwise_and(frame, frame, mask=mask)

    # afficher l'image
    imgRes = np.hstack((frame, imgRes,))
    cv2.imshow("hor", imgRes)
    # cv2.imshow("mask", mask)
    # cv2.imshow("res", imgRes)
    cv2.waitKey(1)