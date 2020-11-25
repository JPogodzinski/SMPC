# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pogoda/dev/SMPC/gui/itemsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_itemWindow(object):
    def setupUi(self, itemWindow):
        itemWindow.setObjectName("itemWindow")
        itemWindow.resize(640, 136)
        self.centralwidget = QtWidgets.QWidget(itemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.getInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.getInfoButton.setObjectName("getInfoButton")
        self.verticalLayout.addWidget(self.getInfoButton)
        self.getListButton = QtWidgets.QPushButton(self.centralwidget)
        self.getListButton.setObjectName("getListButton")
        self.verticalLayout.addWidget(self.getListButton)
        itemWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(itemWindow)
        QtCore.QMetaObject.connectSlotsByName(itemWindow)

    def retranslateUi(self, itemWindow):
        _translate = QtCore.QCoreApplication.translate
        itemWindow.setWindowTitle(_translate("itemWindow", "Items"))
        self.addButton.setText(_translate("itemWindow", "Add"))
        self.deleteButton.setText(_translate("itemWindow", "Delete"))
        self.getInfoButton.setText(_translate("itemWindow", "Get info"))
        self.getListButton.setText(_translate("itemWindow", "Get list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    itemWindow = QtWidgets.QMainWindow()
    ui = Ui_itemWindow()
    ui.setupUi(itemWindow)
    itemWindow.show()
    sys.exit(app.exec_())
