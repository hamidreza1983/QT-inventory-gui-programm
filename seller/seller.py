import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import (
                            QWidget, QApplication, QLabel, QPushButton, 
                            QLineEdit, QTextEdit, QCheckBox, QRadioButton,
                            QComboBox, QGroupBox, QMainWindow, QSpinBox
                            )
from PyQt5.QtGui import QIcon, QFont

from mysql.connector import connect
from assets.info import Message



class SellerPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setui()