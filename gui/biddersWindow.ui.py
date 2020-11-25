# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pogoda/dev/SMPC/gui/biddersWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 136)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bidders"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.getInfoButton.setText(_translate("MainWindow", "Get info"))
        self.getListButton.setText(_translate("MainWindow", "Get list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
