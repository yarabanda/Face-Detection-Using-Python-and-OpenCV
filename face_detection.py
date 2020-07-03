from cv2 import cv2


face_cascade = cv2.CascadeClassifier('C:\\Users\\Yara\\Desktop\\Python\\OpenCV_Detection\\haarcascade_frontalface_default.xml')

img = cv2.imread('friends.jpg')


#the classifier I used only works with grayscale images
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)


#Now we iterate over the detected faces and draw rectangles on them
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)


#display the output
cv2.imshow('img', img)
cv2.waitKey()
