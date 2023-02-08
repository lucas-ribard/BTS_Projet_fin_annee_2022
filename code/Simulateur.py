import math

import cv2

img = cv2.imread("E:/BTS-SN2-IR/Projet/Ressources/Fond simu.jpg")
pointsList = []


def mousePoints(event,x,y,flags,params):
    #si appuie sur clic gauche
       if event == cv2.EVENT_LBUTTONDOWN:
           #recup pointlist
           size = len(pointsList)
           #si entre 0 et chiffre  divisible par 2
           if size != 0 and size %2  != 0:
               #dessine un trait
               cv2.line(img,tuple(pointsList[round(((size-1)/3)*3)]),(x,y),(0,0,255),5)
           #dessine un rond rouge srr clic
           cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
           #sur clic
           pointsList.append([x,y])


def gradient(pt1,pt2):
    return(pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getAngle(pointList):
    pt1,pt2,pt3 = pointList [-3:]
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1,pt3)
    #mesure dangle en radiant
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    #angle radiant > degree
    angD = round(math.degrees(angR))

    return(angD)

while True :
    #si quantité de points est divisible par 3 et nest pas 0
    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        #apelle fonction
        angD=getAngle(pointsList)

        if angD <= 45 and angD > 0:
            print("tourne a droite,  l'angle est de",angD,"degrées")
            #gauche avance
            #droite recule

        if angD < 90 and angD >45 :
            print("Tourne légerement a Droite,  l'angle est de",angD,"degrées")
            # gauche avance
            # droite imobile

        if angD == 90:
            print("Avance,  l'angle est de",angD,"degrées")
            # gauche avance
            # droite avance

        if angD > -90 and angD < -45:
            print("tourne légerement a gauche,  l'angle est de",180-(-angD),"degrées")
            # gauche imobile
            # droite avance

        if angD >= -45 and angD < 0:
            print("tourne  a gauche,  l'angle est de",180-(-angD),"degrées")
            # gauche recule
            # droite avance



    cv2.imshow("result", img)
    cv2.setMouseCallback('result',mousePoints)
    #si appuie sur r , simu reset
    if cv2.waitKey(1) & 0xFF == ord("r"):
        img = cv2.imread("E:/BTS-SN2-IR/Projet/Ressources/Fond simu.jpg")
        pointsList = []
     #si uppuie sur q ferme la simu
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break