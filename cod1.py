from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QInputDialog, QFileDialog,QTableWidgetItem
import pyqtgraph as pg
import csv



def selectFile():
    fileName = (QFileDialog.getOpenFileName())
    print(fileName)

    with open(fileName[0]) as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:
            # print(row['Agriculture'], row['Industrial Sector'], row['Services Sector'],row['Gross Domestic Product (FC)'])
                dlg.tableWidget.setRowCount(70)
                # dlg.tableWidget.setItem(2 , 0, QtGui.QTableWidgetItem("text1"))
                dlg.tableWidget.setItem(i,0, QTableWidgetItem(row['Agriculture']))
                dlg.tableWidget.setItem(i,1, QTableWidgetItem(row['Industrial Sector']))
                dlg.tableWidget.setItem(i,2, QTableWidgetItem(row['Services Sector']))
                dlg.tableWidget.setItem(i,3, QTableWidgetItem(row['Gross Domestic Product (FC)']))
                i+=1



    # file1 = open(fileName[0],'r')
    # with file1:
    #     text = file1.read()
    #     dlg.textBrowser.setText(text)
def drawgraphs():
    pass



app = QtWidgets.QApplication([])
dlg = uic.loadUi("gui1.ui")
dlg.pushButton.clicked.connect(selectFile)
dlg.show()
app.exec()
