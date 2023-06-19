from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon
import os
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        # -----------> Basic Window
        self.setWindowTitle('Test Window')
        self.setGeometry(300, 300, 300, 300)
        self.setMinimumSize(300, 300)
        self.setMaximumSize(300, 300)
        self.setWindowIcon(QIcon(os.path.dirname(__file__) + "/icon.png"))
        self.setStyleSheet("background-color: red;")
        #self.setFixedSize(300, 300)
        #------------> QLable
        self.show()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj1 = Window()
    sys.exit(app.exec_())