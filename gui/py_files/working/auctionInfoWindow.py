# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SMPC/gui/old_guis/auctionInfoWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_auctionInfoWindow(object):
    def setupUi(self, auctionInfoWindow):
        auctionInfoWindow.setObjectName("auctionInfoWindow")
        auctionInfoWindow.resize(640, 76)
        self.centralwidget = QtWidgets.QWidget(auctionInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseAuctionComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseAuctionComboBox.setObjectName("chooseAuctionComboBox")
        self.verticalLayout.addWidget(self.chooseAuctionComboBox)
        self.chooseAuctionButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseAuctionButton.setObjectName("chooseAuctionButton")
        self.verticalLayout.addWidget(self.chooseAuctionButton)
        auctionInfoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(auctionInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(auctionInfoWindow)

    def retranslateUi(self, auctionInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        auctionInfoWindow.setWindowTitle(_translate("auctionInfoWindow", "Auction Info"))
        self.chooseAuctionButton.setText(_translate("auctionInfoWindow", "Get info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    auctionInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_auctionInfoWindow()
    ui.setupUi(auctionInfoWindow)
    auctionInfoWindow.show()
    sys.exit(app.exec_())
