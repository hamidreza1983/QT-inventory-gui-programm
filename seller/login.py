import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, 
                            QLineEdit, QTextEdit, QCheckBox, QRadioButton,
                            QComboBox, QMessageBox)

from PyQt5.QtGui import QIcon, QFont
from assets.info import Message


from mysql.connector import connect
from seller.seller import SellerPanel
from assets.dbconnection import *

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
        self.btn2.clicked.connect(exit)
        self.show()

    def login(self):

        # CREATE ENVIRONMENT VARIABLES AND RESTART AND UPDATE WINDOWS

        db_connection = Database(
            username=self.line1.text(),
            password=self.line2.text(),
            host=os.getenv("dbhost"),
            )

        if db_connection.connect():
            seller_panel.lable5.setText(self.line1.text())
            seller_panel.lable6.setText(self.line2.text())
            seller_panel.show()
            self.close()
            
        else:
            message.UserInputError()

       

        
if __name__ == '__main__':
    app = QApplication(sys.argv)    
    obj1 = Window()
    seller_panel = SellerPanel()
    message = Message()
    sys.exit(app.exec_())