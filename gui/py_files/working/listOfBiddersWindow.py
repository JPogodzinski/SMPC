# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SMPC/gui/old_guis/listOfBiddersWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listOfBiddersWindow(object):
    def setupUi(self, listOfBiddersWindow):
        listOfBiddersWindow.setObjectName("listOfBiddersWindow")
        listOfBiddersWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(listOfBiddersWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listOfBidders = QtWidgets.QListWidget(self.centralwidget)
        self.listOfBidders.setObjectName("listOfBidders")
        self.verticalLayout.addWidget(self.listOfBidders)
        listOfBiddersWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(listOfBiddersWindow)
        QtCore.QMetaObject.connectSlotsByName(listOfBiddersWindow)

    def retranslateUi(self, listOfBiddersWindow):
        _translate = QtCore.QCoreApplication.translate
        listOfBiddersWindow.setWindowTitle(_translate("listOfBiddersWindow", "List of Bidders"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listOfBiddersWindow = QtWidgets.QMainWindow()
    ui = Ui_listOfBiddersWindow()
    ui.setupUi(listOfBiddersWindow)
    listOfBiddersWindow.show()
    sys.exit(app.exec_())
