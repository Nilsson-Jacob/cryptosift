import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import crunch as crunch
from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QInputDialog

import threading
import time


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Analyse")
        self.text = QtWidgets.QLabel("Analyse crypto", 
                                     alignment=QtCore.Qt.AlignCenter)
        self.input = QLineEdit()
        self.input2 = QLineEdit()

        self.label = QLabel()
        self.label.setText("Currency:")

        self.label2 = QLabel()
        self.label2.setText("Days to analyse:")

        self.label3 = QLabel()

        self.layout1 = QtWidgets.QVBoxLayout(self)
        self.layout1.setSpacing(10)

        self.layout1.addWidget(self.text)
        self.layout1.addWidget(self.label)       
        self.layout1.addWidget(self.input)

        self.layout1.addWidget(self.label2)
        self.layout1.addWidget(self.input2)
        self.layout1.setContentsMargins(100,100,100,100)
        self.layout1.addWidget(self.button)
        self.layout1.addWidget(self.label3)
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):


        while not crunch.getData(self.input.text(), int(self.input2.text())):
            self.label3.setText("Crunching numbers..")

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)    

def start():
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(600, 400)
    widget.show()

    sys.exit(app.exec())