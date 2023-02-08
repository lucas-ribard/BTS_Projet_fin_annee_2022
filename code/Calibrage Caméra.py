import urllib.request

import cv2
import numpy as np


def empty(a):
    pass
#ajuste les parametres de la caméra
urllib.request.urlopen("http://192.168.4.1/control?var=framesize&val=8")
urllib.request.urlopen("http://192.168.4.1/control?var=lenc&val=0")

#TRACKER COULEUR
cv2.namedWindow("Track_color")
cv2.resizeWindow("Track_color", 640, 240)
cv2.createTrackbar("Hue_Min", "Track_color", 0, 179, empty)
cv2.createTrackbar("Hue_Max", "Track_color", 179, 179, empty)
cv2.createTrackbar("Sat_Min", "Track_color", 0, 255, empty)
cv2.createTrackbar("Sat_Max", "Track_color", 255, 255, empty)
cv2.createTrackbar("Val_Min", "Track_color", 0, 255, empty)
cv2.createTrackbar("Val_Max", "Track_color", 255, 255, empty)

#TRACKER POSITION
cv2.namedWindow("Track_pos")
cv2.resizeWindow("Track_pos", 400, 400)
#Point A valeur X et Y
cv2.createTrackbar("PT_A_X", "Track_pos", 0, 640, empty)
cv2.createTrackbar("PT_A_Y", "Track_pos", 0, 480, empty)
#Point B valeur X et Y
cv2.createTrackbar("PT_B_X", "Track_pos", 640, 640, empty)
cv2.createTrackbar("PT_B_Y", "Track_pos", 0, 480, empty)
#Point C valeur X et Y
cv2.createTrackbar("PT_C_X", "Track_pos", 0, 640, empty)
cv2.createTrackbar("PT_C_Y", "Track_pos", 480, 480, empty)
#Point D valeur X et Y
cv2.createTrackbar("PT_D_X", "Track_pos", 640, 640, empty)
cv2.createTrackbar("PT_D_Y", "Track_pos", 480, 480, empty)

# lien de la cam  ; http://username:password@ip
url = "http://192.168.4.1:81/stream"
# open the feed
cap = cv2.VideoCapture(url)



while True:
    # read next frame
    ret, frame = cap.read()
    #rotaionne l'image de 90°
    rotat = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    #filtre Gris
    imgGray = cv2.cvtColor(rotat, cv2.COLOR_BGR2GRAY)

#tracker couleur
    h_min = cv2.getTrackbarPos("Hue_Min", "Track_color", )
    h_max = cv2.getTrackbarPos("Hue_Max", "Track_color", )
    s_min = cv2.getTrackbarPos("Sat_Min", "Track_color", )
    s_max = cv2.getTrackbarPos("Sat_Max", "Track_color", )
    v_min = cv2.getTrackbarPos("Val_Min", "Track_color", )
    v_max = cv2.getTrackbarPos("Val_Max", "Track_color", )

#Tracker Positions
    ptax = cv2.getTrackbarPos("PT_A_X", "Track_pos", )
    ptay = cv2.getTrackbarPos("PT_A_Y", "Track_pos", )

    ptbx = cv2.getTrackbarPos("PT_B_X", "Track_pos", )
    ptby = cv2.getTrackbarPos("PT_B_Y", "Track_pos", )

    ptcx = cv2.getTrackbarPos("PT_C_X", "Track_pos", )
    ptcy = cv2.getTrackbarPos("PT_C_Y", "Track_pos", )

    ptdx = cv2.getTrackbarPos("PT_D_X", "Track_pos", )
    ptdy = cv2.getTrackbarPos("PT_D_Y", "Track_pos", )

    #positions des points
    pt_A = [ptax, ptay]
    pt_B = [ptbx, ptby]
    pt_C = [ptcx, ptcy]
    pt_D = [ptdx, ptdy]

    #taille d'image origine(ici cam)
    width, height = 500,500

    #mise en forme image
    input_pt = np.float32([[pt_A], [pt_B], [pt_C], [pt_D]])
    output_pt = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(input_pt, output_pt)
    imgOutput = cv2.warpPerspective(imgGray, matrix, (width, height))

    #export l'qimage redimensioné en carré pour mon masque
    cv2.imwrite('coconut.png', imgOutput)
    #vas lire l'image carré
    img = cv2.imread('coconut.png')
    # filtre HSV (pour mask) avec l'image importé
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #filtres de couleurs
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img, lower, upper)
    imgRes = cv2.bitwise_and(imgOutput, imgOutput, mask=mask)

    #inverse l'image
    invert = cv2.bitwise_not(imgRes)
    # afficher l'image
    imgRes = np.hstack((imgOutput,imgRes, invert,))
    cv2.imshow("Result", imgRes)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# close the connection and close all windows
cap.release()
cv2.destroyAllWindows()