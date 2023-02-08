import cv2
import numpy as np

# lien de la cam  ; http://username:password@ip
url = "http://admin:pwe9vv@10.201.36.161:80/videostream.cgi"
kernel = np.ones((3,3),np.uint8)
# open the feed
cap = cv2.VideoCapture(url)

while True:
    # read next frame
    ret, frame = cap.read()

    # var imggray = img Blue Green Red to Gray
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # flou
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),0)
    #detection de bord
    imgCanny = cv2.Canny(imgBlur,100,100)
    #dilater les bords
    imgDilat = cv2.dilate(imgCanny, kernel, iterations=1)
    #erode les bords
    imgEroded = cv2.erode(imgDilat,kernel,iterations=1)

    #change la taille d'affichage
    imgResize4 = cv2.resize(imgDilat, (500, 400))
    imgResize3 = cv2.resize(imgCanny, (500, 400))
    imgResize2 = cv2.resize(imgEroded, (500, 400))
    imgResize1 = cv2.resize(frame, (500, 400))



    # affiche les images
    cv2.imshow('Babicam', frame)
    cv2.imshow('Babicam_Gray', imgGray)
    cv2.imshow('Babicam_Blur', imgBlur)
    cv2.imshow('Babicam_canny', imgCanny)
    cv2.imshow('Babicam_Dilat', imgDilat)
    cv2.imshow('Babicam_Erode', imgEroded)

    #affiche les images recadrés
    #cv2.imshow('Babicam_Dilat_RES', imgResize4)
    #cv2.imshow('Babicam_Canny_RES', imgResize3)
    #cv2.imshow('Babicam_Erode_RES', imgResize2)
    #cv2.imshow('Babicam_NORMAL_RES', imgResize1)

    #stack de 3 écrans (canny,dilat et eroded) dans une seule fenetre
    imgHor = np.hstack((imgCanny,imgDilat,imgEroded))
    cv2.imshow("hor",imgHor)



    # if user presses q quit program
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# close the connection and close all windows
cap.release()
cv2.destroyAllWindows()