import cv2
print("package imported")

#crée une variable img et récupere l'image dans le dossier Ressources
img = cv2.imread("E:/BTS-SN2-IR/Projet/Ressources/champ.jpg")

#afficher l'image
cv2.imshow("Output", img)
#crée un délais d'affichage de x milisec , 0 = infinit
cv2.waitKey()