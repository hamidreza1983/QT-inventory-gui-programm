from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, 
                            QLineEdit, QTextEdit, QCheckBox, QRadioButton,
                            QComboBox)

from PyQt5.QtGui import QIcon, QFont
import os
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        # -----------> Basic Window
        self.setWindowTitle('Test Window')
        self.setGeometry(300, 300, 600, 600)
        self.setMinimumSize(300, 300)
        self.setMaximumSize(300, 300)
        self.setWindowIcon(QIcon(os.path.dirname(__file__) + "/assets/icon.png"))
        #self.setStyleSheet("background-color: red;")
        #self.setFixedSize(300, 300)
        #------------> QLable
        self.lable1 = QLabel("hamid",self)
        self.lable1.move(10,10)
        self.lable1.setStyleSheet("color: red;")
        #------------> Pushbutton
        self.btn1 = QPushButton("Click Me", self)
        self.btn1.move(100, 100)
        self.btn1.resize(50,50)
        self.btn1.clicked.connect(self.clicked)
        #--------------------------------
        self.btn2 = QPushButton("Click Me2", self)
        self.btn2.move(200,200)
        self.btn2.resize(50,50)
        self.btn2.clicked.connect(self.clicked2)
        #------------> Lineedit
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.move(150, 100)
        self.lineedit1.textChanged.connect(self.text)
        #------------> Textedit
        self.textedit1 = QTextEdit(self)
        self.textedit1.move(250, 100)
        self.textedit1.textChanged.connect(self.text)
        #------------> Checkbox
        self.checkbox1 = QCheckBox("Check Me", self)
        self.checkbox1.move(100, 250)
        self.checkbox1.stateChanged.connect(self.check)
        #------------> Radiobutton
        self.radiobutton1 = QRadioButton("Radio Me", self)
        self.radiobutton1.move(50, 100)
        self.radiobutton1.clicked.connect(self.radio)
        #------------> Combobox
        self.combobox1 = QComboBox(self)
        self.combobox1.move(100, 100)
        #self.combobox1.addItem("Hamid")
        self.combobox1.addItems(["hamid", "reza", "mehrabi"])
        #self.combobox1.currentIndexChanged.connect(self.combo)
        self.combobox1.currentTextChanged.connect(self.combo)

    def clicked(self):
        self.lable1.setFont(QFont("Times New Roman", 20))
        self.lable1.setText("Im changed")
        self.lable1.setStyleSheet("color:blue;")
        self.lable1.resize(130,80)
        #self.btn2.setDisabled(True)
        self.lineedit1.setDisabled(False)
        #self.lineedit1.setEnabled(True)
        print(self.lable1.text())


    def clicked2(self):
        self.lineedit1.setText("im here")
        self.lineedit1.setDisabled(True)


    def text(self):
        print(self.textedit1.toPlainText())

    def check(self):
        print(self.checkbox1.isChecked())

    def radio(self):
        print(self.radiobutton1.isChecked())

    def combo(self,name):
        print(self.combobox1.currentText())
        

        
if __name__ == '__main__':
    app = QApplication(sys.argv)    
    obj1 = Window()
    sys.exit(app.exec_())