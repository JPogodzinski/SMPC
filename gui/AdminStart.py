# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pogoda/dev/SMPC/gui/AdminStart.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminStartWindow(object):
    def setupUi(self, adminStartWindow):
        adminStartWindow.setObjectName("adminStartWindow")
        adminStartWindow.resize(640, 105)
        self.centralwidget = QtWidgets.QWidget(adminStartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.auctionButton = QtWidgets.QPushButton(self.centralwidget)
        self.auctionButton.setObjectName("auctionButton")
        self.verticalLayout.addWidget(self.auctionButton)
        self.biddersButton = QtWidgets.QPushButton(self.centralwidget)
        self.biddersButton.setObjectName("biddersButton")
        self.verticalLayout.addWidget(self.biddersButton)
        self.itemsButton = QtWidgets.QPushButton(self.centralwidget)
        self.itemsButton.setObjectName("itemsButton")
        self.verticalLayout.addWidget(self.itemsButton)
        adminStartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(adminStartWindow)
        QtCore.QMetaObject.connectSlotsByName(adminStartWindow)

    def retranslateUi(self, adminStartWindow):
        _translate = QtCore.QCoreApplication.translate
        adminStartWindow.setWindowTitle(_translate("adminStartWindow", "Start"))
        self.auctionButton.setText(_translate("adminStartWindow", "Auctions"))
        self.biddersButton.setText(_translate("adminStartWindow", "Bidders"))
        self.itemsButton.setText(_translate("adminStartWindow", "Items"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminStartWindow = QtWidgets.QMainWindow()
    ui = Ui_adminStartWindow()
    ui.setupUi(adminStartWindow)
    adminStartWindow.show()
    sys.exit(app.exec_())
