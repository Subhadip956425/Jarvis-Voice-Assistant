# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(995, 711)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(340, 0, 351, 81))
        self.label.setStyleSheet("border-image: url(C:/Users/subha/Desktop/Final/0000 (1).png);\n"
                                 "background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\subha\\Desktop\\Final/0000 (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.mainGIF = QtWidgets.QLabel(Dialog)
        self.mainGIF.setGeometry(QtCore.QRect(10, 80, 971, 511))
        self.mainGIF.setText("")
        self.mainGIF.setPixmap(QtGui.QPixmap("C:\\Users\\subha\\Desktop\\Final/jarvisfullgui.gif"))
        self.mainGIF.setScaledContents(True)
        self.mainGIF.setObjectName("mainGIF")
        self.StartButton = QtWidgets.QPushButton(Dialog)
        self.StartButton.setGeometry(QtCore.QRect(60, 610, 171, 61))
        self.StartButton.setStyleSheet("border-image: url(C:/Users/subha/Desktop/Final/0000.png);\n"
                                       "background-color: transparent;")
        self.StartButton.setObjectName("StartButton")
        self.LoginButton_2 = QtWidgets.QPushButton(Dialog)
        self.LoginButton_2.setGeometry(QtCore.QRect(460, 610, 171, 61))
        self.LoginButton_2.setStyleSheet("border-image: url(C:/Users/subha/Desktop/Final/0000 (3).png);\n"
                                         "background-color: transparent;\n"
                                         "")
        self.LoginButton_2.setObjectName("LoginButton_2")
        self.ExitButton_3 = QtWidgets.QPushButton(Dialog)
        self.ExitButton_3.setGeometry(QtCore.QRect(810, 610, 171, 61))
        self.ExitButton_3.setStyleSheet("border-image: url(C:/Users/subha/Desktop/Final/0000 (2).png);\n"
                                        "background-color: transparent;")
        self.ExitButton_3.setObjectName("ExitButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())