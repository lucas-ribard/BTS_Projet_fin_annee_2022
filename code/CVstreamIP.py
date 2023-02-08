import cv2

# lien de la cam  ; http://username:password@ip
url = "http://192.168.4.1:81/stream"

# open the feed
cap = cv2.VideoCapture(url)

while True:
    # read next frame
    ret, frame = cap.read()

    # show frame to user
    cv2.imshow('Babicam', frame)

    # if user presses q quit program
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# close the connection and close all windows
cap.release()
cv2.destroyAllWindows()