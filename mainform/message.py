from PyQt5.QtWidgets import  QMessageBox, QWidget

class Message(QWidget):


    def UserInputError(self):
        #msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        #msg.setWindowTitle("Warning")
        #msg.setText("username or password is incorrect")
        #msg.setStandardButtons(QMessageBox.Ok)
        #msg.exec_()
        QMessageBox.critical(self, "Error", "username or password is incorrect", QMessageBox.Ok)

    def ConnectionFailed(self):

        QMessageBox.warning(self, "connection failed", "cant connect to database\ncheck cable or network device", QMessageBox.Ok)


    def UserCreatedSuccessfully(self):
        QMessageBox.information(self, "Success", "User created successfully", QMessageBox.Ok)


    def SelectOneOfCheckBox(self):
        QMessageBox.warning(self, "Warning", "Please select one of the checkbox", QMessageBox.Ok)