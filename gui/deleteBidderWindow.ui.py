# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pogoda/dev/SMPC/gui/deleteBidderWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deleteBidderWindow(object):
    def setupUi(self, deleteBidderWindow):
        deleteBidderWindow.setObjectName("deleteBidderWindow")
        deleteBidderWindow.resize(640, 78)
        self.centralwidget = QtWidgets.QWidget(deleteBidderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseBidderCombobox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseBidderCombobox.setObjectName("chooseBidderCombobox")
        self.verticalLayout.addWidget(self.chooseBidderCombobox)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        deleteBidderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(deleteBidderWindow)
        QtCore.QMetaObject.connectSlotsByName(deleteBidderWindow)

    def retranslateUi(self, deleteBidderWindow):
        _translate = QtCore.QCoreApplication.translate
        deleteBidderWindow.setWindowTitle(_translate("deleteBidderWindow", "Delete Bidder"))
        self.deleteButton.setText(_translate("deleteBidderWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteBidderWindow = QtWidgets.QMainWindow()
    ui = Ui_deleteBidderWindow()
    ui.setupUi(deleteBidderWindow)
    deleteBidderWindow.show()
    sys.exit(app.exec_())
