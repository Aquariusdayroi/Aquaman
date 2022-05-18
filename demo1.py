# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdemo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView, QAbstractItemView, QPushButton, QTableWidget, \
                            QTableWidgetItem, QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import module_BauCua


Numerator  = 0
Demoninator = 1


class Dictionary:
    def __init__(self, key, value):
        self.key = key
        self.value = value
Dices=[]
Face=['Bầu', 'Cua', 'Tôm', 'Cá', 'Gà', 'Nai']


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1329, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1341, 561))
        self.tabWidget.setMinimumSize(QtCore.QSize(741, 0))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")


      
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(350, 40, 131, 31))
        self.label.setObjectName("label")


        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(510, 370, 71, 31))
        self.textBrowser.setObjectName("textBrowser")
        # self.textBrowser.setText('1234')
        

        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(340, 100, 631, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)


        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(340, 370, 171, 31))
        self.label_2.setObjectName("label_2")


        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(470, 40, 61, 31))
        self.spinBox.setMaximum(9)
        self.spinBox.setObjectName("spinBox")


        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 370, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.readTableData)
        self.pushButton_2.clicked.connect(self.Compute)
        self.pushButton_2.clicked.connect(self.loadData1)
        self.pushButton_2.clicked.connect(self.loadData2)


        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(820, 30, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addinput)



        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")


        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(190, 40, 891, 411))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)


        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
       
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(QtGui.QColor(255, 127, 255))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 127, 255))
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 127, 255))
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 127, 255))
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 127, 255))
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 127, 255))
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(300)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)




        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1329, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addinput(self, MainWindow):
        rowCount=int(self.spinBox.text())
        self.tableWidget.setRowCount(rowCount)
        self.tableWidget_2.setRowCount((rowCount+1)*6)


    def readTableData(self, MainWindow):
        rowCount=int(self.spinBox.text())
        columCount=6
        global Dices
        Dices.clear()
        for i in range(rowCount): Dices.append([])
        for i in range(rowCount):
            Dices[i].clear()
            for j in range(columCount):
                item=self.tableWidget.item(i, j)
                if item and item.text():
                    Dices[i].append(int(item.text()))
                else:
                    Dices[i].append(0)

 # print(bc.tonghop)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Số xúc sắc</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bầu "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cua"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tôm"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cá"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gà"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Nai"))


        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Số Trường Hợp</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Run All"))
        self.pushButton.setText(_translate("MainWindow", "Add Input"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))

        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ghi Chú"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Số lần xảy ra theo thống kê"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Xác suất thống kê"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Hệ số của mỗi lần trúng"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tổng"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Số xúc sắc ra mặt đơn đã chọn "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))


    def Compute(self, MainWindow):
        # Initial
        global Numerator, Demoninator
        Numerator=0
        Demoninator=1
        print(Demoninator)
        TotalZero = 0
        TotalRequire = 0
        totalCase = 0
        rowCount=int(self.spinBox.text())
        for i in range(rowCount):
            SumOfFaceOfDice = 0
            for j in range(6):
                SumOfFaceOfDice=SumOfFaceOfDice+Dices[i][j]
            Demoninator=Demoninator * SumOfFaceOfDice
        # self.textBrowser.clear()
        if Demoninator==0:
            Numerator = 0
            self.show_popup(self) 
        else:
            self.textBrowser.setText(str(Demoninator))
    def show_popup(self, MainWindow):
        msg = QMessageBox()
        msg.setText("ERROR 404!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Retry)
        x = msg.exec_(   )


    def loadData1(self, MainWindow): #Ghi chú
        rowCount=int(self.spinBox.text())
        columCount=6
        row=0
        for i in range(columCount):
            for j in range(rowCount+1):
                self.tableWidget_2.setItem(row,0, QtWidgets.QTableWidgetItem('Trúng '+str(j)+' con '+Face[i]))
                self.tableWidget_2.setItem(row,3, QtWidgets.QTableWidgetItem(str(j)))
                row+=1

    def loadData2(self, MainWindow): # số lần xảy ra theo thống kê
        bc=module_BauCua.BauCua(Dices)
        bc.cal()
        rowCount=int(self.spinBox.text())
        columCount=6
        row=0
        print(Demoninator)
        for i in range(columCount):
            for j in range(rowCount+1):
                ans=round(bc.tonghop[j][i]*100/Demoninator, 7)
                ans2=round(bc.tonghop[j][i]*100/Demoninator*j, 7)
                self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(bc.tonghop[j][i])))
                self.tableWidget_2.setItem(row, 2,QtWidgets.QTableWidgetItem(str(ans)+'%'))
                self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(ans2)+'%'))
                self.tableWidget_2.setItem(row, 5, QtWidgets.QTableWidgetItem(str(j)))
                row+=1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
