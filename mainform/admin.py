from PyQt5.QtWidgets import (
                            QWidget, QApplication, QLabel, QPushButton, 
                            QLineEdit, QTextEdit, QCheckBox, QRadioButton,
                            QComboBox, QGroupBox
                            )

from PyQt5.QtGui import QIcon, QFont
import os
import sys


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
        #------------> Group1 QLineedit
        self.lineedit1 = QLineEdit(self.group1)
        self.lineedit1.move(60, 28)
        self.lineedit1.resize(250,23)
        self.lineedit2 = QLineEdit(self.group1)
        self.lineedit2.move(60, 58)
        self.lineedit2.resize(250,23)
        self.lineedit3 = QLineEdit(self.group1)
        self.lineedit3.move(60, 88)
        self.lineedit3.resize(250,23)
        #------------> Group1 QCheckBox
        self.checkBox1 = QCheckBox("admin", self.group1)
        self.checkBox1.move(318,35)
        self.checkBox2 = QCheckBox("inventor", self.group1)
        self.checkBox2.move(318,60)
        self.checkBox3 = QCheckBox("seller", self.group1)
        self.checkBox3.move(318,85)
        #------------> Group1 QPushButton
        self.button1 = QPushButton("Create user", self.group1)
        self.button1.move(85,120)
        self.button1.resize(200,30)
        #------------> GroupBox2
        self.group2 = QGroupBox("Delete user", self)
        self.group2.move(10, 180)
        self.group2.resize(380,60)
        #------------> Group2 QLable
        self.lable4 = QLabel("username",self.group2)
        self.lable4.move(10,28)
        #------------> Group2 QLineedit
        self.lineedit4 = QLineEdit(self.group2)
        self.lineedit4.move(84, 25)
        self.lineedit4.resize(200,25)
        #------------> Group2 QPushButton
        self.button2 = QPushButton("Create user", self.group2)
        self.button2.move(288,25)
        self.button2.resize(88,25)
        #------------> self
        self.button3 = QPushButton("Create user", self)
        self.button3.move(13,250)
        self.button3.resize(175,40)
        self.button4 = QPushButton("Create user", self)
        self.button4.move(210,250)
        self.button4.resize(175,40)
        self.button5 = QPushButton("Create user", self)
        self.button5.move(13,300)
        self.button5.resize(175,40)
        self.button6 = QPushButton("Create user", self)
        self.button6.move(210,300)
        self.button6.resize(175,40)
        self.button7 = QPushButton("Create user", self)
        self.button7.move(13,350)
        self.button7.resize(375,25)
        self.button8 = QPushButton("Create user", self)
        self.button8.move(13,380)
        self.button8.resize(375,25)


        
if __name__ == '__main__':
    app = QApplication(sys.argv)    
    obj1 = PanelAdmin()
    sys.exit(app.exec_())