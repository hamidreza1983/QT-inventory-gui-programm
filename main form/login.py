from PyQt5.QtWidgets import QWidget, QApplication
import sys


class Window(QWidget):
    #def __init__(self):
    #    super().__init__()
    #    self.setUI()

    def setUI(self):
        self.setWindowTitle('Test Window')
        self.setGeometry(300, 300, 300, 300)
        self.setMinimumSize(300, 300)
        self.setMaximumSize(300, 300)
        #self.setFixedSize(300, 300)
        #self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj1 = Window()
    obj1.setUI()
    obj1.show()
    sys.exit(app.exec_())