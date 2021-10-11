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
        print(fc.MilkObj.name)
    def loaddata(self):
        foods=[]
        row=0
        self.tablo.setRowCount(len(foods))
        for food in foods: #Sonuçları satırlar halinde tabloda gösteren döngü
            self.tablo.setItem(row,0,QtWidgets.QTableWidgetItem(food["sut"]))
            self.tablo.setItem(row, 1, QtWidgets.QTableWidgetItem(food["et"]))
            self.tablo.setItem(row, 2, QtWidgets.QTableWidgetItem(food["ekmek"]))
            row=row+1

if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.showMaximized()
    sys.exit(app.exec_())