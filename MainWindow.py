import sys
import cv2

from UI.UI_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(sys.exit)
        self.ui.btn_video.clicked.connect(self.face_recognition)

    def face_recognition(self):

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        filename = QFileDialog.getOpenFileName(self, "Open Video", None,"Videos (*.mp4 *.webm *.mkv);; All files (*.*)")
        cap = cv2.VideoCapture(filename[0])

        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Display the output
            cv2.imshow('Face Recognition', frame)

            cv2.waitKey(30)
        cap.release()
        cv2.destroyAllWindows()


