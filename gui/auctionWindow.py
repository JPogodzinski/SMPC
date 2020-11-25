# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pogoda/dev/SMPC/gui/auctionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_auctionsWindow(object):
    def setupUi(self, auctionsWindow):
        auctionsWindow.setObjectName("auctionsWindow")
        auctionsWindow.resize(640, 105)
        self.centralwidget = QtWidgets.QWidget(auctionsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.verticalLayout.addWidget(self.createButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.getInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.getInfoButton.setObjectName("getInfoButton")
        self.verticalLayout.addWidget(self.getInfoButton)
        auctionsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(auctionsWindow)
        QtCore.QMetaObject.connectSlotsByName(auctionsWindow)

    def retranslateUi(self, auctionsWindow):
        _translate = QtCore.QCoreApplication.translate
        auctionsWindow.setWindowTitle(_translate("auctionsWindow", "Auctions"))
        self.createButton.setText(_translate("auctionsWindow", "Create"))
        self.deleteButton.setText(_translate("auctionsWindow", "Delete"))
        self.getInfoButton.setText(_translate("auctionsWindow", "Get info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    auctionsWindow = QtWidgets.QMainWindow()
    ui = Ui_auctionsWindow()
    ui.setupUi(auctionsWindow)
    auctionsWindow.show()
    sys.exit(app.exec_())
