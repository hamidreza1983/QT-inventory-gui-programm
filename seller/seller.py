import os
import sys
from datetime import date
from time import strftime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import (
                            QWidget, QApplication, QLabel, QPushButton, 
                            QLineEdit, QTextEdit, QCheckBox, QRadioButton,
                            QComboBox, QGroupBox, QMainWindow, QSpinBox,QFrame,
                            QTableWidget
                            )
from PyQt5.QtGui import QIcon, QFont

from mysql.connector import connect
from assets.info import Message



class SellerPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setui()

    def setui(self):
        # -----------> Basic Window
        self.setWindowTitle('Seller Panel')
        self.setGeometry(300, 300,500, 555)
        self.setWindowIcon(QIcon("seller.ico"))
        self.setFixedSize(500,555)
        #------------> Line 1
        self.line1 = QFrame(self)
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.line1.setLineWidth(1)
        self.line1.setMidLineWidth(1)
        self.line1.resize(500,1)
        self.line1.move(0,95)
        self.line2 = QFrame(self)
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.line2.setLineWidth(1)
        self.line2.setMidLineWidth(1)
        self.line2.resize(500,1)
        self.line2.move(0,150)
        #------------> self Label
        self.lable1 = QLabel("Customer",self)
        self.lable1.move(10,10)
        self.lable2 = QLabel("Phone",self)
        self.lable2.move(10,40)
        self.lable3 = QLabel("Customer type ",self)
        self.lable3.move(10,70)
        self.lable4 = QLabel("Invoice : ",self)
        self.lable4.move(350,10)
        self.lable5 = QLabel("Date : "+str(date.today()),self)
        self.lable5.move(350,40)
        self.lable6 = QLabel("Time : "+str(strftime("%H:%M:%S")),self)
        self.lable6.move(350,70)
        self.lable7 = QLabel("Product Code : ",self)
        self.lable7.move(10,115)
        #------------> self Lineedit
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.move(90,8)
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.move(90,38)
        self.lineedit3 = QLineEdit(self)
        self.lineedit3.move(90,112)
        self.lineedit3.resize(135,20)
        #------------> self ComboBox
        self.combobox1 = QComboBox(self)
        self.combobox1.move(90,68)
        self.combobox1.addItems(["Normal", "Vip"])
        self.combobox1.resize(135,20)
        #------------> self Button
        self.button1 = QPushButton("+",self)
        self.button1.setStyleSheet("color:green")
        self.button1.setFont(QFont("Arial", 20))
        self.button1.move(230,110)
        self.button1.resize(25,25)
        #------------> self table
        self.table = QTableWidget(self) 
        self.table.move(10,160)
        self.table.resize(480,200)


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SellerPanel()
    sys.exit(app.exec_())
