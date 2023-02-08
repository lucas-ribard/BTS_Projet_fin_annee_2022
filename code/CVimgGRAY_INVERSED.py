import cv2
print("package imported")

#crée une variable img et récupere l'image dans le dossier Ressources
img = cv2.imread("Ressources/champ.jpg")

#var imggray = img Blue Green Red to Gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(imgGray)


#afficher l'image
cv2.imshow("Gray",imgGray)
cv2.imshow("invert",invert)
#crée un délais d'affichage de x milisec , 0 = infinit
cv2.waitKey(0)