import urllib.request
import time
import cv2
import numpy as np

#ajuste les parametres de la caméra
urllib.request.urlopen("http://192.168.4.1/control?var=framesize&val=8")
urllib.request.urlopen("http://192.168.4.1/control?var=lenc&val=0")
arrayX=[]
arrayY=[]

def getContours(img):
    global arrayX
    global arrayY
    MoyX = 0
    MoyY = 0
    contours,hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
     area = cv2.contourArea(cnt)
     if 1000<area<4000:
                           #contours entier-couleur-eppaiseur
         cv2.drawContours(imgResult,cnt,-1,(255,0,0),2)
         peri= cv2.arcLength(cnt,True)
         approx = cv2.approxPolyDP(cnt,0.2*peri,True)
         x,y,w,h = cv2.boundingRect(approx)
         ValX = x + w // 2
         ValY = y + h // 2
        # dessine un cercle  ,   x    y ,epaiseur,(RGB)
         cv2.circle(imgFinal, (ValX, ValY), 20, (0, 255, 0), cv2.FILLED)
         cv2.circle(imgResult, (ValX, ValY), 5, (0, 0, 0), cv2.FILLED)
        #taille array
         for i in range(4):
             arrayX.append(int(ValX))
             arrayX = list(set(arrayX))
         print(arrayX)

         #compte nb d'élement dans la liste
         nbValX = len(arrayX)
         print("nombre valeur",nbValX)
         # moy via somme de ValX divisé par le nb d'élément
         MoyX = sum(arrayX) / nbValX
         print(MoyX)
        #transforme le float en int
         MoyX = int(MoyX)
         print('MoyY',MoyX)

         for i in range(4):
             arrayY.append(int(ValY))
             arrayY = list(set(arrayY))
         print(arrayY)

         #compte nb d'élement dans la liste
         nbValY = len(arrayY)
         print("nombre valeur",nbValY)
         # moy via somme de ValX divisé par le nb d'élément
         MoyY = sum(arrayY) / nbValY
         print(MoyY)
        #transforme le float en int
         MoyY = int(MoyY)
         print('MoyY',MoyY)


    return MoyX,MoyY

def affMoy(MoyX,MoyY):
    for i in range(1):
        # moyenne posé en rouge
        cv2.circle(imgResult, (MoyX, 20), 10, (0, 0, 255), cv2.FILLED)
        cv2.line(imgResult, (MoyX, 20),(190,500),(255,0,0),3)
    return

# lien de la cam  ; http://username:password@ip
url = "http://192.168.4.1:81/stream"
# open the feed
cap = cv2.VideoCapture(url)

while True:
    # read next frame
    ret, frame = cap.read()
    # rotaionne l'image de 90°
    rotat = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    #filtre Gris
    imgGray = cv2.cvtColor(rotat, cv2.COLOR_BGR2GRAY)

    #//parametrage d'image//
    #↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

    #positions des points
    pt_A = [111, 280]
    pt_B = [316, 282]
    pt_C = [45, 468]
    pt_D = [392, 458]

    # parametre de filtre(garde le gris, ignore le blanc
    myColor = [0, 179, 0, 250, 0, 250]
    # h_min,h_max,s_min,s_max,v_min,v_max

    #taille d'image origine(ici cam)
    width, height = 400, 296



    #mise en forme image
    input_pt = np.float32([[pt_A], [pt_B], [pt_C], [pt_D]])
    output_pt = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(input_pt, output_pt)
    imgOutput = cv2.warpPerspective(imgGray, matrix, (width, height))

    #export l'image redimensioné en carré pour mon masque
    cv2.imwrite('coconut.png', imgOutput)
    #vas lire l'image carré
    img = cv2.imread('coconut.png')
    # filtre HSV (pour mask) avec l'image importé
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    #filtres de couleurs
    lower = np.array([myColor[0], myColor[2], myColor[4]]) #H_min , S_min , V_min
    upper = np.array([myColor[1], myColor[3], myColor[5]]) #H max ,S max ,V max
    mask = cv2.inRange(img, lower, upper)
    imgRes = cv2.bitwise_and(imgOutput, imgOutput, mask=mask)

    #copy de imgResult
    imgResult = img.copy()
    imgFinal = img.copy()

    #recup les x,y du centre du mask
    MoyY,MoyX=getContours(mask)
    affMoy(MoyX,MoyY)

    # afficher l'image
    cv2.imshow("mask", mask)   #affiche masque
    cv2.imshow("Final", imgFinal)  #point sur image
    cv2.imshow("result", imgResult)  #contours et points
    arrayX = []
    arrayY = []
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# close the connection and close all windows
cap.release()
cv2.destroyAllWindows()
