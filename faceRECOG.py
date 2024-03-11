import numpy

from PyQt5.QtWidgets import QWidget

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, QTimer
import sys
import cv2
import os
import face_recognition

from facerecogGUI import Ui_Widget

def nameList(nameofImg):
    if nameofImg.startswith("SG", 0):
        return "Subhadip Guchhait"


class faceRECOG(QWidget):
    def __init__(self):
        super(faceRECOG, self).__init__()
        print("Setting up GUI")
        self.faceUI = Ui_Widget()
        self.faceUI.setupUi(self)

        self.name = None
        self.videoCapture_ = None
        self.name = None
        

        self.faceUI.exitButton.clicked.connect(self.close)
        self.runProg()

    def runProg(self):
        videopath = "C:\\Users\\subha\\Desktop\\Final/face-recognition.gif "
        self.videoCapture_ = videopath
        self.starVideo(self.videoCapture_)


    @pyqtSlot()
    def starVideo(self, cameraName):
        print("Encoding started")
        if len(cameraName) == 1:
            self.capture = cv2.VideoCapture(cameraName)
        self.timer = QTimer(self)
        path = 'Images'
        if not os.path.exists(path):
            os.mkdir(path)

        images = []  #Images of faces
        self.classNames = []  # Name of images
        self.encodeList = []  # Encoding of faces

        photoList = os.listdir(path)

        for cl in photoList:
            currentImage = cv2.imread(f"{path}/{cl}")
            images.append(currentImage)
            self.classNames.append(os.path.splitext(cl)[0])

        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
            self.encodeList.append(encodes_cur_frame)
        print("Face encode sucessfully")
        self.timer.timeout.connect(self.updateFrames)
        self.timer.start(10)

    def updateFrames(self):
        self.capture = cv2.VideoCapture(self.videoCapture_)
        ret, self.image = self.capture.read()
        self.displayImage(self.image, self.encodeList, self.classNames, 1)

    def displayImage(self, image, encodeList, className, window=1):
        image = cv2.resize(image, (571, 441))
        try:
            image = self.faceRec(image, encodeList, className)
        except:
            print("Cannot show image")
            format = QImage.Format_Indexed8
            if len(image.shape) == 3:
                if image.shape[2] == 4:
                    qformat = QImage.format_RGBA8888
                else:
                    qformat = QImage.Format_RGB888
            outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
            outImage = outImage.rgbSwapped()


            if window == 1:
                self.faceUI.videoBack.setPixmap(QPixmap.fromImage(outImage))
                self.faceUI.videoBack.setScaledContents(True)
                if self.name == "Subhadip Guchhait":
                    self.connectToJervisMainFile()

    def faceRec(self, image, encodeList, className):
        faces_cur_frame = face_recognition.face_locations(image)
        encodes_cur_frame = face_recognition.face_encodings(image, faces_cur_frame)

        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
            match = face_recognition.compare_faces(encodeList, encodeFace, tolerance=0.50)
            face_dis = face_recognition.face_distance(encodeList, encodeFace)
            self.name = "Unknown"
            bestMatchIndex = numpy.argmin(face_dis)

            if match[bestMatchIndex]:
                self.name = className[bestMatchIndex]
                self.name = nameList(self.name)
                y1, x2, y2, x1 = faceLoc
                cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(image, self.name, (x1 - 6, y2 + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 1)


    def connectToJervisMainFile(self):
        from subprocess import call
        self.close()
        call(["python", "loginWindowMAIN.py"])


if __name__ == "__main__":
    while True:
        app = QApplication(sys.argv)
        ui = faceRECOG()
        ui.show()
        sys.exit(app.exec_())