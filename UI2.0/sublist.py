# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sublist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    #obje.glist = glist

    def __init__(self,glist):
        self.glist = glist


    def setupUi(self, Form,glist):

        print(glist)

        Form.setObjectName("Form")
        Form.resize(432, 319)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 431, 321))
        self.listWidget.setObjectName("listWidget")


        for i in range(20):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
        '''item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)'''

        self.retranslateUi(Form,glist)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form,glist):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)



        for i in range(len(glist)):


            item = self.listWidget.item(i)
            ##print(item)
            item.setText(_translate("Form", glist[i]))

        #item = self.listWidget.item(0)
        #item.setText(_translate("Form", "使命召唤"))
        #item = self.listWidget.item(1)
        #item.setText(_translate("Form", "Dota2"))
        #item = self.listWidget.item(2)
        #item.setText(_translate("Form", "War3"))
        #item = self.listWidget.item(3)
        #item.setText(_translate("Form", "Game4"))



        self.listWidget.setSortingEnabled(__sortingEnabled)


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())'''

