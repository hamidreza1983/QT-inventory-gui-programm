from PyQt5.QtWidgets import  QMessageBox, QWidget

class Message(QWidget):


    def UserInputError(self):
        return QMessageBox.critical(self, "Error", "username or password is incorrect\nmay one or some fields be empty", QMessageBox.Ok)

    def ConnectionFailed(self):
        return QMessageBox.warning(self, "connection failed", "cant connect to database\ncheck cable or network device\nmy be user is exists on database\nmy be access denied for this user or host", QMessageBox.Ok)


    def UserCreatedSuccessfully(self):
        return QMessageBox.information(self, "Success", "User created successfully", QMessageBox.Ok)


    def SelectOneOfCheckBox(self):
        return QMessageBox.warning(self, "Warning", "Please select one of the checkbox", QMessageBox.Ok)


    def UserDoesNotExist(self):
        return QMessageBox.warning(self, "Warning", "User does not exist", QMessageBox.Ok)


    def UserDeletedSuccessfully(self):
        return QMessageBox.information(self, "Success", "User deleted successfully", QMessageBox.Ok)


    def DatabaseUpdatedSuccessfully(self):
        return QMessageBox.information(self, "Success", "Database updated successfully", QMessageBox.Ok)


    def DatabaseInputError(self):
        return QMessageBox.critical(self, "Error", "Input data is not vali", QMessageBox.Ok)

    
    def ProductNotFound(self):
        return QMessageBox.warning(self, "Warning", "Product not found", QMessageBox.Ok)

    
    def ProductDeletedSuccessfully(self):
        return QMessageBox.information(self, "Success", "Product deleted successfully", QMessageBox.Ok)

