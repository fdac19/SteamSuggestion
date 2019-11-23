# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SteamSuggestion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sublist as child
import filter

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 200, 466, 159))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 0, 2, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout.addWidget(self.comboBox_5, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 270, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 380, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 30, 591, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 380, 431, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 440, 113, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.newtab)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Genres"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Action"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Strategy"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "RPG"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Simulation"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Adventure"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Years"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2019"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "2018"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "2017"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "2016"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "2015"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Platforms"))
        self.comboBox.setItemText(1, _translate("MainWindow", "windows"))
        self.comboBox.setItemText(2, _translate("MainWindow", "mac"))
        self.comboBox.setItemText(3, _translate("MainWindow", "linux"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Required Age"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "16+"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "18+"))
        self.label.setText(_translate("MainWindow", "Filter Attributes:"))
        self.label_2.setText(_translate("MainWindow", "Show Result by:"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Welcome to SteamSuggestion!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the Filter to help you choose Steam Games which is you may love!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#fc0107;\">Step 1</span>: Select some game attributes to help you filter more than 27,000 steam game such as Platforms, Publisher etc.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#fc0107;\">Step 2</span>: Select a keyword to sort all of fit games </p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Sort By Positive Rating"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Sort By Average Play Time "))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Sort By Price Highest to Lowest"))
        self.pushButton.setText(_translate("MainWindow", "Go"))

    def newtab(self):

        args = ['','','','',0]


        args[0] = str(self.comboBox.currentText())
        #plat
        if args[0] == 'Platforms':
            args[0] = ''


        stext = str(self.comboBox_2.currentText())
        #sort

        if "Positive" in stext:
            args[4] = 0

        if "Play Time" in stext:
            args[4] = 1

        if "Price" in stext:
            args[4] = 2


        args[1] = str(self.comboBox_3.currentText())

        if args[1] == "Genres":
            args[1] = ''

        args[2] = str(self.comboBox_4.currentText())

        if args[2] == "Years":
            args[2] = ''


        args[3] = str(self.comboBox_5.currentText())
        if args[3] == '16+':
            args[3] = '16'
        if args[3] == '18+':
            args[3] = '18'

        if args[3] == 'Required Age':
            args[3] = ''

        print(args)

        print(filter.run(args))

        glist = filter.run(args)

        Dialog = QtWidgets.QDialog()
        ui = child.Ui_Form(glist)

        ui.setupUi(Dialog,glist)
        Dialog.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

