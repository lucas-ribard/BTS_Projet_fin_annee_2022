import cv2

img = cv2.imread("Ressources/fraise.jpg")
print(img.shape)
imgResize = cv2.resize(img,(1800,1200))



cv2.imshow("image",img)
cv2.imshow("image_2",imgResize)
cv2.waitKey()