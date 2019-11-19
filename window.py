from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QTableWidgetItem
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
from scipy import stats

class Window:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.dlg = uic.loadUi("MainWindow.ui")
        self.dlg.SelectFile.clicked.connect(self.selectFile)
        self.dlg.barchart.clicked.connect(self.BarChart)
        self.dlg.extrapolate.clicked.connect(self.extrapolate)
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
        # df.describe()
        fig = plt.figure()
        fig.add_subplot(221)
        plt.bar(x,agriculture)
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
    def extrapolate(self):
        df = pd.read_csv(self.file)
        a = df['Agriculture']
        b = df['Industrial Sector']
        c = df['Services Sector']
        d = df['Gross Domestic Product (FC)']
        x = df['Year']
        fig = plt.figure()
        fig.add_subplot(221)
        plt.plot(x, a, 'ro')
        z = np.polyfit(x, a, 20)
        f = np.poly1d(z)
        x2 = []
        for x1 in np.linspace(1950, 2020, 70):
            x2.append(x1)
        plt.plot(x2, f(x2), 'b+')
        
        fig.add_subplot(222)
    # #---------------------
        plt.plot(x, b, 'ro')    
        z = np.polyfit(x, b, 20)
        f = np.poly1d(z)
        x2 = []
        for x1 in np.linspace(1950, 2020, 70):
            x2.append(x1)
        plt.plot(x2, f(x2), 'b+')
        
        fig.add_subplot(223)
    # #---------------------
        plt.plot(x, c, 'ro')
        z = np.polyfit(x, c, 20)
        f = np.poly1d(z)
        x2 = []
        for x1 in np.linspace(1950, 2020, 70):
            x2.append(x1)
        plt.plot(x2, f(x2), 'b+')
        
        fig.add_subplot(224)
    # #---------------------
        plt.plot(x, d, 'ro')
        z = np.polyfit(x, d, 20)
        f = np.poly1d(z)
        x2 = []
        for x1 in np.linspace(1950, 2020, 70):
            x2.append(x1)
        plt.plot(x2, f(x2), 'b+')
        
        plt.show()
        
    # t test function
    # stats.ttest_ind(df['Agriculture'], df['Industrial Sector'])



window= Window()