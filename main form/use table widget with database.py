from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5.QtGui import QIcon
import os
import sys
from mysql.connector import connect


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        # -----------> Basic Window

        self.setWindowTitle('Test Window')
        self.setGeometry(300, 300, 600, 600)
        #self.setMinimumSize(300, 300)
        #self.setMaximumSize(300, 300)
        self.setWindowIcon(QIcon(os.path.dirname(__file__) + "/assets/icon.png"))
        #self.setStyleSheet("background-color: red;")
        #self.setFixedSize(300, 300)

        #------------> QLable
        con = connect(host="localhost",username="root",password="root",database="hamid")
        cur = con.cursor()
        cur.execute("select * from info")
        self.tb1 = QTableWidget(self)
        self.tb1.resize(600, 600)
        cur_list = list(cur)
        self.tb1.setColumnCount(len(cur_list[0]))
        self.tb1.setRowCount(len(cur_list))
        for row_index,column in enumerate(cur_list):

            for column_index , data in enumerate(column):
                item = QTableWidgetItem(str(data))
                self.tb1.setItem(row_index,column_index,item)
            
        cur.close()
        con.close()
        self.show()




        
        




        
if __name__ == '__main__':
    app = QApplication(sys.argv)    
    obj1 = Window()
    sys.exit(app.exec_())