import cv2
import numpy as np
def empty(a):
    pass

url = "http://admin:pwe9vv@10.201.36.161:80/videostream.cgi"

kernel = np.ones((3,3),np.uint8)
cap = cv2.VideoCapture(url)


cv2.namedWindow("Track")
cv2.resizeWindow("Track", 500, 500)
#Point A valeur X et Y
cv2.createTrackbar("PT_A_X", "Track", 0, 640, empty)
cv2.createTrackbar("PT_A_Y", "Track", 0, 480, empty)
#Point B valeur X et Y
cv2.createTrackbar("PT_B_X", "Track", 640, 640, empty)
cv2.createTrackbar("PT_B_Y", "Track", 0, 480, empty)
#Point C valeur X et Y
cv2.createTrackbar("PT_C_X", "Track", 0, 640, empty)
cv2.createTrackbar("PT_C_Y", "Track", 480, 480, empty)
#Point D valeur X et Y
cv2.createTrackbar("PT_D_X", "Track", 640, 640, empty)
cv2.createTrackbar("PT_D_Y", "Track", 480, 480, empty)

while True:
    ret, frame = cap.read()

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ptax = cv2.getTrackbarPos("PT_A_X", "Track", )
    ptay = cv2.getTrackbarPos("PT_A_Y", "Track", )

    ptbx = cv2.getTrackbarPos("PT_B_X", "Track", )
    ptby = cv2.getTrackbarPos("PT_B_Y", "Track", )

    ptcx = cv2.getTrackbarPos("PT_C_X", "Track", )
    ptcy = cv2.getTrackbarPos("PT_C_Y", "Track", )

    ptdx = cv2.getTrackbarPos("PT_D_X", "Track", )
    ptdy = cv2.getTrackbarPos("PT_D_Y", "Track", )

    pt_A = [ptax, ptay]
    pt_B = [ptbx, ptby]
    pt_C = [ptcx, ptcy]
    pt_D = [ptdx, ptdy]

    width, height = 640, 480

    input_pt = np.float32([[pt_A], [pt_B], [pt_C], [pt_D]])
    output_pt = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(input_pt, output_pt)
    imgOutput = cv2.warpPerspective(imgGray, matrix, (width, height))

    # afficher l'image
    cv2.imshow("Frame", imgOutput)
    # cv2.imshow("mask", mask)
    # cv2.imshow("res", imgRes)
    cv2.waitKey(1)