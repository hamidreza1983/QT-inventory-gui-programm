from PyQt5.QtWidgets import  QMessageBox, QWidget

class Message(QWidget):


    def UserInputError(self):
        return QMessageBox.critical(self, "Error", "username or password is incorrect\nmay one or some fields be empty", QMessageBox.Ok)

    def ConnectionFailed(self):
        return QMessageBox.warning(self, "connection failed", "cant connect to database\ncheck cable or network device\nmy be user is exists on database", QMessageBox.Ok)


    def UserCreatedSuccessfully(self):
        return QMessageBox.information(self, "Success", "User created successfully", QMessageBox.Ok)


    def SelectOneOfCheckBox(self):
        return QMessageBox.warning(self, "Warning", "Please select one of the checkbox", QMessageBox.Ok)

    def UserDoesNotExist(self):
        return QMessageBox.warning(self, "Warning", "User does not exist", QMessageBox.Ok)

    def UserDeletedSuccessfully(self):
        return QMessageBox.information(self, "Success", "User deleted successfully", QMessageBox.Ok)

