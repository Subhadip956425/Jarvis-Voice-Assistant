from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import sys

from jarvisMaingui import Ui_Widget



class mainFile(QDialog):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Setting up GUI")
        self.firstUI = Ui_Widget()
        self.firstUI.setupUi(self)


if __name__ == "__main__":
    while True:
        app = QApplication(sys.argv)
        ui = mainFile()
        ui.show()
        sys.exit(app.exec_())