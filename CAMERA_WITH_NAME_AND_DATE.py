import cv2
from datetime import datetime
position = (1100,700)
size = 1
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0,0,255)
thick = 2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    time_srt = datetime.now().strftime("%H:%M:%M")
    cv2.putText(frame, time_srt, position, font, size, color, thick)
    cv2.putText(frame, "Валерія", (600, 20), font, size, (0,255,0, 1), thick)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()