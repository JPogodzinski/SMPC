from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from auctionInfoWindow import Ui_auctionInfoWindow
from createAuctionWindow import Ui_MainWindow as Ui_create
from deleteAuctionWindow import Ui_MainWindow as Ui_delete

class Ui_auctionsWindow(object):
    def showCreate(self):
        self.window = QMainWindow()
        self.ui = Ui_create()
        self.ui.setupUi(self.window)
        self.window.show()

    def showDelete(self):
        self.window = QMainWindow()
        self.ui = Ui_delete()
        self.ui.setupUi(self.window)
        self.window.show()

    def showShow(self):
        self.window = QMainWindow()
        self.ui = Ui_auctionInfoWindow()
        self.ui.setupUi(self.window)
        self.window.show()

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
        self.createButton.clicked.connect(self.showCreate)

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.deleteButton.clicked.connect(self.showDelete)

        self.getInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.getInfoButton.setObjectName("getInfoButton")
        self.verticalLayout.addWidget(self.getInfoButton)
        self.getInfoButton.clicked.connect(self.showShow)

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
