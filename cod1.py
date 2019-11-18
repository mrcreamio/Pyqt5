from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QInputDialog, QFileDialog

def selectFile():
    fileName = (str(QFileDialog.getOpenFileName()))
    print(fileName)
    file1 = open(fileName[0],'r')
    dlg.editor()
    with file1:
        text = file1.read()
        dlg.textBrowser.setText(text)


app = QtWidgets.QApplication([])
dlg = uic.loadUi("gui1.ui")
dlg.pushButton.clicked.connect(selectFile)
dlg.show()
app.exec()
