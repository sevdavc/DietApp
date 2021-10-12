import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog
import sqlite3
import foodclass as fc

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("untitled.ui",self)
        self.tablo.setColumnWidth(6,129) #6.sütunun genişliğini 129px'e sabitledik.
        self.hesapla.clicked.connect(self.loaddata)
        self.sonsifirla.clicked.connect(self.tablo.clearContents)
        self.degsifirla.clicked.connect(self.degerlerisifirla)
        print(fc.MilkObj.name)
        self.area=["bread1","bread2"]

    def loaddata(self):
        foods=[fc.MilkObj,fc.FatObj]
        row=0
        self.tablo.setRowCount(len(foods))
        for food in foods: #Sonuçları satırlar halinde tabloda gösteren döngü
            self.tablo.setItem(row,0,QtWidgets.QTableWidgetItem(str(food.change)))
            self.tablo.setItem(row, 1, QtWidgets.QTableWidgetItem(str(food.fat)))
            row=row+1

    """def degerlerisifirla(self): //çözülmedi
        for item in self.area:
            print(item)
            self.item.clear"""



if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.showMaximized()
    sys.exit(app.exec_())