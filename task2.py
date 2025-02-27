import cv2
import numpy as np

def video_processing():
    ''' Вариант 8
        Слежка за меткой.
        В кадре отображаются горизонтальная и веритикальная
        прямые, которые пересекаются в центре метки.
    '''
    cap = cv2.VideoCapture(0)
    down_points = (900, 750)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)

            cv2.line(frame,(x+int(round(w/2)),y),(x+int(round(w/2)),y+h),(0, 255, 0),5)
            cv2.line(frame,(x,y+int(round(h/2))),(x+w,y+int(round(h/2))),(0, 255, 0),5)
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()


if __name__ == '__main__':
    video_processing()

cv2.waitKey(0)
cv2.destroyAllWindows()