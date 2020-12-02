# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SMPC/gui/old_guis/bidderInfoWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bidderInfoWindow(object):
    def setupUi(self, bidderInfoWindow):
        bidderInfoWindow.setObjectName("bidderInfoWindow")
        bidderInfoWindow.resize(640, 74)
        self.centralwidget = QtWidgets.QWidget(bidderInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseBidderComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseBidderComboBox.setObjectName("chooseBidderComboBox")
        self.verticalLayout.addWidget(self.chooseBidderComboBox)
        self.chooseBidderButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseBidderButton.setObjectName("chooseBidderButton")
        self.verticalLayout.addWidget(self.chooseBidderButton)
        bidderInfoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(bidderInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(bidderInfoWindow)

    def retranslateUi(self, bidderInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        bidderInfoWindow.setWindowTitle(_translate("bidderInfoWindow", "Bidder Info"))
        self.chooseBidderButton.setText(_translate("bidderInfoWindow", "Get info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bidderInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_bidderInfoWindow()
    ui.setupUi(bidderInfoWindow)
    bidderInfoWindow.show()
    sys.exit(app.exec_())
