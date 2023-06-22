from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, 
                            QLineEdit, QTextEdit, QCheckBox, QRadioButton,
                            QComboBox, QMessageBox)

from PyQt5.QtGui import QIcon, QFont
import message
import os
import sys
from mysql.connector import connect
from admin import PanelAdmin

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        # -----------> Basic Window
        self.setWindowTitle('Login form')
        self.setGeometry(300, 300, 300, 100)
        self.setFixedSize(300,100)
        self.setWindowIcon(QIcon("icon.ico"))
        #------------> QLable
        self.lable1 = QLabel("username",self)
        self.lable1.move(10,10)
        self.lable2 = QLabel("password",self)
        self.lable2.move(10,40)
        #------------> Lineedit
        self.line1 = QLineEdit(self)
        self.line1.resize(230,20)
        self.line1.move(60,10)
        self.line2 = QLineEdit(self)
        self.line2.resize(230,20)
        self.line2.move(60,40)
        self.line2.setEchoMode(QLineEdit.Password)
        #------------> Button
        self.btn1 = QPushButton("Login", self)
        self.btn1.move(215,70)
        self.btn1.clicked.connect(self.login)
        self.btn2 = QPushButton("Cancel", self)
        self.btn2.move(60,70)
        self.show()

    def login(self):
        # CREATE ENVIRONMENT VARIABLES AND RESTART AND UPDATE WINDOWS
            if self.line1.text() == os.getenv("dbmysqluser") and self.line2.text() == os.getenv("dbmysqlpassword"):
                try:
                    self.con = connect(
                                        host=os.getenv("dbhost"),
                                        username=self.line1.text(),
                                        password=self.line2.text(),
                                       )
                    admin_panel.show()
                    self.close()

                except:
                    message.ConnectionFailed()
                    
            else:
                message.UserInputErrorError()

       

        
if __name__ == '__main__':
    app = QApplication(sys.argv)    
    obj1 = Window()
    admin_panel = PanelAdmin()
    message = message.Message()
    sys.exit(app.exec_())