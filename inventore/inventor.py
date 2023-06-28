from PyQt5.QtWidgets import (
                            QWidget, QApplication, QLabel, QPushButton, 
                            QLineEdit, QTextEdit, QCheckBox, QRadioButton,
                            QComboBox, QGroupBox, QMainWindow, QSpinBox
                            )
from PyQt5.QtGui import QIcon, QFont
import os
import sys
from mysql.connector import connect

class InventorPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setui()

    def setui(self):
        # -----------> Basic Window
        self.setWindowTitle('Inventor Panel')
        self.setGeometry(300, 300,400, 355)
        self.setWindowIcon(QIcon("inventor.ico"))
        self.setFixedSize(400,355)
        #------------> Groupbox1
        self.group1 = QGroupBox("Create new or update product", self)
        self.group1.move(10, 10)
        self.group1.resize(380,250)
        #------------> Group1 QLable
        self.lable1 = QLabel("Product name",self.group1)
        self.lable1.move(10,30)
        self.lable2 = QLabel("Product type",self.group1)
        self.lable2.move(10,65)
        self.lable3 = QLabel("Number of product",self.group1)
        self.lable3.move(10,100)
        self.lable7 = QLabel("Buy Price", self.group1)
        self.lable7.move(10,135)
        self.lable8 = QLabel("Sell Price", self.group1)
        self.lable8.move(10,170)
        self.lable5 = QLabel("user",self.group1)
        self.lable5.setHidden(True)
        self.lable6 = QLabel("pass",self.group1)
        self.lable6.setHidden(True)
#        ------------> Group1 QLineedit
        self.lineedit1 = QLineEdit(self.group1)
        self.lineedit1.move(130, 28)
        self.lineedit1.resize(225,23)
        self.lineedit2 = QLineEdit(self.group1)
        self.lineedit2.move(130, 130)
        self.lineedit2.resize(225,23)
        self.lineedit3 = QLineEdit(self.group1)
        self.lineedit3.move(130, 165)
        self.lineedit3.resize(225,23)
#        #------------> Group1 QComboBox
        self.combobox1 = QComboBox(self.group1)
        self.combobox1.move(130, 63)
        self.combobox1.addItems(["KG", "Pieces"])
        #------------> Group1 QSpinBox
        self.spinner1 = QSpinBox(self.group1)
        self.spinner1.move(130, 95)
        self.spinner1.resize(120,23)
        self.spinner1.setMaximum(1000000)

        #------------> Group1 QPushButton
        self.button1 = QPushButton("Insert or update on database", self.group1)
        self.button1.move(90, 210)
        self.button1.resize(200,30)
        self.button1.clicked.connect(self.update_db)

        #------------> GroupBox2
        self.group2 = QGroupBox("Delete product", self)
        self.group2.move(10, 265)
        self.group2.resize(380, 80)
        #------------> Group2 QLable
        self.lable4 = QLabel("Product code",self.group2)
        self.lable4.move(10,35)
        #------------> Group2 QLineedit
        self.lineedit4 = QLineEdit(self.group2)
        self.lineedit4.move(100, 30)
        self.lineedit4.resize(160,23)
        #------------> Group2 QPushButton
        self.button2 = QPushButton("Delete product", self.group2)
        self.button2.move(270, 30)
        self.button2.resize(100,23)
        self.button2.clicked.connect(self.delete_product)



        self.show()
    
    def update_db(self):
        from core.message import Message
        
        message = Message()

        self.db_user = connect(
            host = os.environ.get('dbhost'),
            username = self.lable5.text(),
            password = self.lable6.text(),
            database = 'store',
            )
        self.cur = self.db_user.cursor()

        try:

            assert len(self.lineedit1.text()) > 0
            assert len(self.lineedit2.text()) > 0
            assert len(self.lineedit3.text()) > 0
            assert self.spinner1.value() > 0
            assert self.lineedit2.text().isnumeric()
            assert self.lineedit3.text().isnumeric()


            self.cur.execute(
                        f"SELECT total_product FROM goods WHERE product_name='{self.lineedit1.text()}'" 
            )   

            old_total_product = list(self.cur)[0][0]

            self.cur.execute(
                                
                            f"""
                            UPDATE goods
                            SET
                            total_product={self.spinner1.value()+int(old_total_product)},
                            product_buy_price={self.lineedit2.text()},
                            product_sell_price={self.lineedit3.text()},
                            date=CURRENT_TIMESTAMP
                            WHERE product_name='{self.lineedit1.text()}';"""

            )
            self.db_user.commit()
            self.db_user.close()
            message.DatabaseUpdatedSuccessfully()

        except AssertionError:
            message.DatabaseInputError()

        except:
            self.cur.execute(
                f"""INSERT INTO goods
                (product_name,product_type,product_buy_price,product_sell_price,total_product)
                value
                (
                    '{self.lineedit1.text()}',
                    '{self.combobox1.currentText()}',
                     {self.lineedit2.text()},
                     {self.lineedit3.text()},
                     {self.spinner1.value()});"""
            )
            self.db_user.commit()
            self.db_user.close()
            message.DatabaseUpdatedSuccessfully()

    def delete_product(self):
        from core.message import Message

        message = Message()

        self.db_user = connect(
            host = 'localhost',
            username = 'root',
            password = 'root',
            database = 'store',
            )

        self.cur = self.db_user.cursor()

        try:
            assert len(self.lineedit4.text()) > 0
            assert self.lineedit4.text().isnumeric()

            self.cur.execute(
                "SELECT * FROM goods WHERE id=%i;" % int(self.lineedit4.text())
                )

            if len(list(self.cur)) == 0 :
                raise ValueError

            self.cur.execute(
                "DELETE FROM goods WHERE id=%i;" % int(self.lineedit4.text())
                )

            self.db_user.commit()
            self.db_user.close()

            message.ProductDeletedSuccessfully()

        except AssertionError:
            message.DatabaseInputError()

        except ValueError:
             message.ProductNotFound()
           

        



if __name__ == '__main__':
    app = QApplication(sys.argv)    
    obj1 = InventorPanel()
    sys.exit(app.exec_())