import cv2

#variable cap importe la vid des ressources
cap = cv2.VideoCapture("Ressources/Wheatley Crab.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("crab",img)
    #ajoute un delais          attend pour que l'utilisateur entre la touche q pour s'arreter"
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break
