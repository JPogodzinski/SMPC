# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pogoda/dev/SMPC/gui/listOfItemsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listOfItemsWindow(object):
    def setupUi(self, listOfItemsWindow):
        listOfItemsWindow.setObjectName("listOfItemsWindow")
        listOfItemsWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(listOfItemsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listOfItems = QtWidgets.QListWidget(self.centralwidget)
        self.listOfItems.setObjectName("listOfItems")
        self.verticalLayout.addWidget(self.listOfItems)
        listOfItemsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(listOfItemsWindow)
        QtCore.QMetaObject.connectSlotsByName(listOfItemsWindow)

    def retranslateUi(self, listOfItemsWindow):
        _translate = QtCore.QCoreApplication.translate
        listOfItemsWindow.setWindowTitle(_translate("listOfItemsWindow", "List of Items"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listOfItemsWindow = QtWidgets.QMainWindow()
    ui = Ui_listOfItemsWindow()
    ui.setupUi(listOfItemsWindow)
    listOfItemsWindow.show()
    sys.exit(app.exec_())
