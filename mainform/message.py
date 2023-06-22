from PyQt5.QtWidgets import  QMessageBox, QWidget

class Message(QWidget):


    def Error(self):
        #msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        #msg.setWindowTitle("Warning")
        #msg.setText("username or password is incorrect")
        #msg.setStandardButtons(QMessageBox.Ok)
        #msg.exec_()
        QMessageBox.critical(self, "Error", "username or password is incorrect", QMessageBox.Ok)