from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QTableWidgetItem
import matplotlib.pyplot as plt
import pandas as pd
import csv

class Window:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.dlg = uic.loadUi("MainWindow.ui")
        self.dlg.SelectFile.clicked.connect(self.selectFile)
        self.dlg.barchart.clicked.connect(self.BarChart)
        self.dlg.show()
        app.exec()

    def selectFile(self):
        fileName = (QFileDialog.getOpenFileName())
        self.dlg.groupBox_3.lower()
        self.file=fileName[0]
        with open(fileName[0]) as csvfile:
            reader = csv.DictReader(csvfile)
            i = 0
            for row in reader:
                    self.dlg.data_table.setRowCount(70)
                    self.dlg.data_table.setItem(i, 0, QTableWidgetItem(row['Year']))
                    self.dlg.data_table.setItem(i, 1, QTableWidgetItem(row['Agriculture']))
                    self.dlg.data_table.setItem(i, 2, QTableWidgetItem(row['Industrial Sector']))
                    self.dlg.data_table.setItem(i, 3, QTableWidgetItem(row['Services Sector']))
                    self.dlg.data_table.setItem(i, 4, QTableWidgetItem(row['Gross Domestic Product (FC)']))
                    i+=1
    def BarChart(self):
        df= pd.read_csv(self.file)
        x = df['Year']
        agriculture = df['Agriculture']
        industry = df['Industrial Sector']
        services = df['Services Sector']
        domestic = df['Gross Domestic Product (FC)']
        df.describe()
        fig = plt.figure()
        fig.add_subplot(221)
        plt.bar(agriculture)
        plt.title("Agriculture")
        fig.add_subplot(222)
        plt.bar(x, industry)
        plt.title("industry")
        fig.add_subplot(223)
        plt.bar(x, services)
        plt.title("services")
        fig.add_subplot(224)
        plt.bar(x, domestic)
        plt.title("domestic")
        plt.show()


window= Window()