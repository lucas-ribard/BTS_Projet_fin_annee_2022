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

    pt_A = [150, 260]
    pt_B = [400, 260]
    pt_C = [70, 480]
    pt_D = [470, 480]

    width, height = 640, 480

    input_pt = np.float32([[pt_A], [pt_B], [pt_C], [pt_D]])
    output_pt = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(input_pt, output_pt)
    imgOutput = cv2.warpPerspective(frame, matrix, (width, height))

    # afficher l'image
    cv2.imshow("input", frame)
    cv2.imshow("Output", imgOutput)

    # if user presses q quit program
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# close the connection and close all windows
cap.release()
cv2.destroyAllWindows()