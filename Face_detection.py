import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret, frame = cap.read()

    if ret == False:
        continue

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 128, 255), 2)
        # (0, 128, 255) is the BGR value

    cv2.imshow("Video Frame", frame)

    key_pressed = cv2.waitKey(1) & 0xff
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
