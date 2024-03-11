from PyQt5.QtWidgets import QWidget, QLineEdit

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import sys

from loginWindowGUI import Ui_loginWindowClass

class loginWindow(QWidget):
    def __init__(self):
        super(loginWindow, self).__init__()
        print("Setting up GUI")
        self.loginUI = Ui_loginWindowClass()
        self.loginUI.setupUi(self)

        self.loginUI.illegalEntry.hide()
        self.loginUI.passwordEntry.setEchoMode(QLineEdit.Password)
        self.loginUI.loginButton.clicked.connect(self.validateLogin)


        self.loginUI.illegalEntryMovie = QtGui.QMovie("C:\\Users\\subha\\Desktop\\Final/wron_Credential.gif")
        self.loginUI.illegalEntry.setMovie(self.loginUI.illegalEntryMovie)


        self.loginUI.retryButton.clicked.connect(self.retryButton)
        self.loginUI.exitButton.clicked.connect(self.close)

    def retryButton(self):
        self.loginUI.usernameEntry.clear()
        self.loginUI.passwordEntry.clear()
        self.stopMovie()

    def validateLogin(self):
        username = self.loginUI.usernameEntry.text()
        password = self.loginUI.passwordEntry.text()
        pu_file = open("username.txt","r")
        pu = pu_file.read()
        pw_file = open("password.txt","r")
        pw = pw_file.read()
        pw_file.close()
        if (password == pw and username == pu):
            print("Login success")
        else:
            self.playMovie()

    def playMovie(self):
        self.loginUI.illegalEntry.show()
        self.loginUI.illegalEntryMovie.start()
    def stopMovie(self):
        self.loginUI.illegalEntry.hide()
        self.loginUI.illegalEntryMovie.stop()

if __name__ == "__main__":
    while True:
        app = QApplication(sys.argv)
        ui = loginWindow()
        ui.show()
        sys.exit(app.exec_())