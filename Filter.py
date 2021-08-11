import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret == False:
        continue

    cv2.imshow("Video Frame", frame)

    key_pressed = cv2.waitKey(1) & 0xff
    if key_pressed == ord('q'):
        break

while True:
    ret, frame = cap.read()

    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == False:
        continue

    cv2.imshow("Gray Frame", grey_frame)

    key_pressed = cv2.waitKey(1) & 0xff

    if key_pressed == ord('q'):
        break

while True:
    ret, frame = cap.read()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if ret == False:
        continue

    cv2.imshow("RGB Frame", rgb_frame)

    key_pressed = cv2.waitKey(1) & 0xff

    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
