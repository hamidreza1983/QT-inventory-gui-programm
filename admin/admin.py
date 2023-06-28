from PyQt5.QtWidgets import (
                            QWidget, QApplication, QLabel, QPushButton, 
                            QLineEdit, QTextEdit, QCheckBox, QRadioButton,
                            QComboBox, QGroupBox, QMainWindow
                            )
from PyQt5.QtGui import QIcon, QFont
import os
import sys
from mysql.connector import connect
import message
import dbconnection



class PanelAdmin(QWidget):

    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        # -----------> Basic Window
        self.setWindowTitle('Admin Panel')
        self.setGeometry(300, 300,400, 420)
        self.setWindowIcon(QIcon("admin.ico"))
        self.setFixedSize(400,420)
        #------------> Groupbox1
        self.group1 = QGroupBox("Create new user with deligate", self)
        self.group1.move(10, 10)
        self.group1.resize(380,160)
        #------------> Group1 QLable
        self.lable1 = QLabel("username",self.group1)
        self.lable1.move(10,30)
        self.lable2 = QLabel("password",self.group1)
        self.lable2.move(10,60)
        self.lable3 = QLabel("host ip",self.group1)
        self.lable3.move(10,90)
        self.lable5 = QLabel("user",self.group1)
        self.lable5.setHidden(True)
        self.lable6 = QLabel("pass",self.group1)
        self.lable6.setHidden(True)
        #------------> Group1 QLineedit
        self.lineedit1 = QLineEdit(self.group1)
        self.lineedit1.move(60, 28)
        self.lineedit1.resize(250,23)
        self.lineedit2 = QLineEdit(self.group1)
        self.lineedit2.move(60, 58)
        self.lineedit2.resize(250,23)
        self.lineedit2.setEchoMode(QLineEdit.Password)
        self.lineedit3 = QLineEdit(self.group1)
        self.lineedit3.move(60, 88)
        self.lineedit3.resize(250,23)
        #------------> Group1 QCheckBox
        self.checkBox1 = QCheckBox("admin", self.group1)
        self.checkBox1.move(318,35)
        self.checkBox1.stateChanged.connect(self.changeState)
        self.checkBox2 = QCheckBox("inventor", self.group1)
        self.checkBox2.move(318,60)
        self.checkBox2.stateChanged.connect(self.changeState)
        self.checkBox3 = QCheckBox("seller", self.group1)
        self.checkBox3.move(318,85)
        self.checkBox3.stateChanged.connect(self.changeState)
        #------------> Group1 QPushButton
        self.button1 = QPushButton("Create user", self.group1)
        self.button1.move(85,120)
        self.button1.resize(200,30)
        self.button1.clicked.connect(self.createuser)
        #------------> GroupBox2
        self.group2 = QGroupBox("Delete user", self)
        self.group2.move(10, 180)
        self.group2.resize(380,60)
        #------------> Group2 QLable
        self.lable4 = QLabel("username",self.group2)
        self.lable4.move(10,28)
        self.lable7 = QLabel("@",self.group2)
        self.lable7.move(188,28)
        #------------> Group2 QLineedit
        self.lineedit4 = QLineEdit(self.group2)
        self.lineedit4.move(84, 25)
        self.lineedit4.resize(100,25)
        self.lineedit5 = QLineEdit(self.group2)
        self.lineedit5.move(200, 25)
        self.lineedit5.resize(100,25)
        #------------> Group2 QPushButton
        self.button2 = QPushButton("Delete user", self.group2)
        self.button2.move(305,25)
        self.button2.resize(70,25)
        self.button2.clicked.connect(self.deleteuser)
        #------------> self
        self.button3 = QPushButton("Daily profit and loos", self)
        self.button3.move(13,250)
        self.button3.resize(175,40)
        self.button4 = QPushButton("Weekly profit and loos", self)
        self.button4.move(210,250)
        self.button4.resize(175,40)
        self.button5 = QPushButton("Mountly profit and loos", self)
        self.button5.move(13,300)
        self.button5.resize(175,40)
        self.button6 = QPushButton("Yearly profit and loos", self)
        self.button6.move(210,300)
        self.button6.resize(175,40)
        self.button7 = QPushButton("Total profit and loos", self)
        self.button7.move(13,350)
        self.button7.resize(375,25)
        self.button8 = QPushButton("Exit", self)
        self.button8.clicked.connect(exit)
        self.button8.move(13,380)
        self.button8.resize(375,25)
        #self.show()
        


    def changeState(self):
        if self.checkBox1.isChecked():
            self.checkBox2.setEnabled(False)
            self.checkBox3.setEnabled(False)

        elif self.checkBox2.isChecked():
            self.checkBox1.setEnabled(False)
            self.checkBox3.setEnabled(False)

        elif self.checkBox3.isChecked():
            self.checkBox1.setEnabled(False)
            self.checkBox2.setEnabled(False)
        else:
            self.checkBox1.setEnabled(True)
            self.checkBox2.setEnabled(True)
            self.checkBox3.setEnabled(True)

    def createuser(self):
        from message import Message

        message = Message()

        if self.checkBox1.isChecked():

            db_user = dbconnection.DatabaseUserManager(
                username=self.lable5.text(),
                password=self.lable6.text(),
                host=os.environ.get('dbhost'),
                newuser=self.lineedit1.text(),
                newpassword=self.lineedit2.text(),
                newhost=self.lineedit3.text(),
            )

            if db_user.create_admin_user():
                message.UserCreatedSuccessfully()

            else :
                message.ConnectionFailed()
        
        elif self.checkBox2.isChecked():

            db_user = dbconnection.DatabaseUserManager(
                username=self.lable5.text(),
                password=self.lable6.text(),
                host=os.environ.get('dbhost'),
                newuser=self.lineedit1.text(),
                newpassword=self.lineedit2.text(),
                newhost=self.lineedit3.text(),
            )

            if db_user.create_inventor_user():
                message.UserCreatedSuccessfully()
            
            else :
                message.ConnectionFailed()

        elif self.checkBox3.isChecked():
            db_user = dbconnection.DatabaseUserManager(
                username=self.lable5.text(),
                password=self.lable6.text(),
                host=os.environ.get('dbhost'),
                newuser=self.lineedit1.text(),
                newpassword=self.lineedit2.text(),
                newhost=self.lineedit3.text(),
            )
            if db_user.create_seller_user():
                message.UserCreatedSuccessfully()
            
            else : 
                message.ConnectionFailed()
        else :
            message.SelectOneOfCheckBox()
    
    def deleteuser(self):
        from message import Message
        message = Message()
        db_user = dbconnection.DatabaseUserManager(
                username=self.lable5.text(),
                password=self.lable6.text(),
                host=os.environ.get('dbhost'),
                newuser=self.lineedit4.text(),
                newhost=self.lineedit5.text(),
            )
        if db_user.delete_user():
            message.UserDeletedSuccessfully()
        
        else:
            message.UserDoesNotExist()




        
if __name__ == '__main__':
    app = QApplication(sys.argv)    
    obj1 = PanelAdmin()
    sys.exit(app.exec_())