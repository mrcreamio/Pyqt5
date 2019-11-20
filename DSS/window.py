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
        self.dlg.Piechart.clicked.connect(self.SelectYear)
        self.dlg.showyear.clicked.connect(self.PieChart)
        self.dlg.compBar.clicked.connect(self.component_bar)
        self.dlg.var1.addItems(['Agriculture', 'Industrial Sector', 'Services Sector', 'Gross Domestic Product (FC)'])
        self.dlg.var2.addItems(['Agriculture', 'Industrial Sector', 'Services Sector', 'Gross Domestic Product (FC)'])
        self.dlg.showt.clicked.connect(self.t_test)
        self.dlg.rawdata.clicked.connect(self.dlg.groupBox_5.lower)
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
                    self.dlg.comboBox.addItem(row['Year'])

                    self.dlg.data_table.setItem(i, 0, QTableWidgetItem(row['Year']))
                    self.dlg.data_table.setItem(i, 1, QTableWidgetItem(row['Agriculture']))
                    self.dlg.data_table.setItem(i, 2, QTableWidgetItem(row['Industrial Sector']))
                    self.dlg.data_table.setItem(i, 3, QTableWidgetItem(row['Services Sector']))
                    self.dlg.data_table.setItem(i, 4, QTableWidgetItem(row['Gross Domestic Product (FC)']))
                    i+=1
    def BarChart(self):
        df= pd.read_csv(self.file)
        x = df['Year']
        print (x)
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
    #
    def SelectYear(self):
        self.dlg.data_table.lower()

    def PieChart(self):
        df = pd.read_csv(self.file)
        year = self.dlg.comboBox.currentText()
        int_year = int(year)
        data = df[df['Year'] == int_year]
        labels = ['Agriculture','Industrial Sector','Services Sector','Gross Domestic Product (FC)']
        values=[int(data['Agriculture']),int(data['Industrial Sector']),int(data['Services Sector']),int(data['Gross Domestic Product (FC)'])]
        plt.pie(values, labels=labels)
        plt.show()

    def component_bar(self):
        df = pd.read_csv(self.file)
        a = df['Agriculture']
        b = df['Industrial Sector']
        c = df['Services Sector']
        d = df['Gross Domestic Product (FC)']
        x = df['Year']
        x_indexes = np.arange(len(x))
        width = 0.2
        plt.bar(x_indexes - width, a, width=width, label='Agriculture')
        plt.bar(x_indexes - width - width, b, width=width, label='Industrial sector')
        plt.bar(x_indexes + width, c, width=width, label='Services Sector')
        plt.bar(x_indexes, d, width=width, label='Gross Domestic Product')
        plt.xticks(x_indexes, x)
        plt.xlabel('Years')
        plt.ylabel('Million Rupees')
        plt.legend()
        plt.show()

    def t_test(self):
        var1 = self.dlg.var1.currentText()
        var2 = self.dlg.var2.currentText()
        df = pd.read_csv(self.file)
        a = stats.ttest_ind(df[var1], df[var2])
        self.dlg.tOutput.setText(str("t value =" +str(a[0]) + " \n p value = " + str(a[1])+"\n"))


window= Window()