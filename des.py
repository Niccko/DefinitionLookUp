# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 130, 761, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pickBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pickBtn.setGeometry(QtCore.QRect(20, 10, 171, 41))
        self.pickBtn.setObjectName("pickBtn")
        self.showDefBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showDefBtn.setGeometry(QtCore.QRect(20, 60, 171, 41))
        self.showDefBtn.setObjectName("showDefBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 581, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(790, 130, 301, 231))
        self.listWidget.setObjectName("listWidget")
        self.let1 = QtWidgets.QListWidget(self.centralwidget)
        self.let1.setGeometry(QtCore.QRect(790, 10, 41, 111))
        self.let1.setObjectName("let1")
        item = QtWidgets.QListWidgetItem()
        self.let1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let1.addItem(item)
        self.let5 = QtWidgets.QListWidget(self.centralwidget)
        self.let5.setGeometry(QtCore.QRect(1050, 10, 41, 111))
        self.let5.setObjectName("let5")
        item = QtWidgets.QListWidgetItem()
        self.let5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let5.addItem(item)
        self.let2 = QtWidgets.QListWidget(self.centralwidget)
        self.let2.setGeometry(QtCore.QRect(850, 10, 41, 111))
        self.let2.setObjectName("let2")
        item = QtWidgets.QListWidgetItem()
        self.let2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let2.addItem(item)
        self.let3 = QtWidgets.QListWidget(self.centralwidget)
        self.let3.setGeometry(QtCore.QRect(920, 10, 41, 111))
        self.let3.setObjectName("let3")
        item = QtWidgets.QListWidgetItem()
        self.let3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let3.addItem(item)
        self.let4 = QtWidgets.QListWidget(self.centralwidget)
        self.let4.setGeometry(QtCore.QRect(990, 10, 41, 111))
        self.let4.setObjectName("let4")
        item = QtWidgets.QListWidgetItem()
        self.let4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.let4.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        self.menuChange_file = QtWidgets.QMenu(self.menubar)
        self.menuChange_file.setObjectName("menuChange_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChange_File = QtWidgets.QAction(MainWindow)
        self.actionChange_File.setObjectName("actionChange_File")
        self.menuChange_file.addAction(self.actionChange_File)
        self.menubar.addAction(self.menuChange_file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pickBtn.setText(_translate("MainWindow", "Pick word"))
        self.showDefBtn.setText(_translate("MainWindow", "Show definition"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        __sortingEnabled = self.let1.isSortingEnabled()
        self.let1.setSortingEnabled(False)
        item = self.let1.item(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.let1.item(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.let1.item(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.let1.item(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.let1.item(4)
        item.setText(_translate("MainWindow", "E"))
        item = self.let1.item(5)
        item.setText(_translate("MainWindow", "F"))
        self.let1.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.let5.isSortingEnabled()
        self.let5.setSortingEnabled(False)
        item = self.let5.item(0)
        item.setText(_translate("MainWindow", "Y"))
        item = self.let5.item(1)
        item.setText(_translate("MainWindow", "Z"))
        self.let5.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.let2.isSortingEnabled()
        self.let2.setSortingEnabled(False)
        item = self.let2.item(0)
        item.setText(_translate("MainWindow", "G"))
        item = self.let2.item(1)
        item.setText(_translate("MainWindow", "H"))
        item = self.let2.item(2)
        item.setText(_translate("MainWindow", "I"))
        item = self.let2.item(3)
        item.setText(_translate("MainWindow", "J"))
        item = self.let2.item(4)
        item.setText(_translate("MainWindow", "K"))
        item = self.let2.item(5)
        item.setText(_translate("MainWindow", "L"))
        self.let2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.let3.isSortingEnabled()
        self.let3.setSortingEnabled(False)
        item = self.let3.item(0)
        item.setText(_translate("MainWindow", "M"))
        item = self.let3.item(1)
        item.setText(_translate("MainWindow", "N"))
        item = self.let3.item(2)
        item.setText(_translate("MainWindow", "O"))
        item = self.let3.item(3)
        item.setText(_translate("MainWindow", "P"))
        item = self.let3.item(4)
        item.setText(_translate("MainWindow", "Q"))
        item = self.let3.item(5)
        item.setText(_translate("MainWindow", "R"))
        self.let3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.let4.isSortingEnabled()
        self.let4.setSortingEnabled(False)
        item = self.let4.item(0)
        item.setText(_translate("MainWindow", "S"))
        item = self.let4.item(1)
        item.setText(_translate("MainWindow", "T"))
        item = self.let4.item(2)
        item.setText(_translate("MainWindow", "U"))
        item = self.let4.item(3)
        item.setText(_translate("MainWindow", "V"))
        item = self.let4.item(4)
        item.setText(_translate("MainWindow", "W"))
        item = self.let4.item(5)
        item.setText(_translate("MainWindow", "X"))
        self.let4.setSortingEnabled(__sortingEnabled)
        self.menuChange_file.setTitle(_translate("MainWindow", "File"))
        self.actionChange_File.setText(_translate("MainWindow", "Change File"))