from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from auctionInfoWindow import Ui_auctionInfoWindow
from addBiddertoAuction import Ui_addBiddertoAuction
from startAuction import Ui_startAuction
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

    def showStart(self):
        self.window = QMainWindow()
        self.ui = Ui_startAuction()
        self.ui.setupUi(self.window)
        self.window.show()

    def showAddBidder(self):
        self.window = QMainWindow()
        self.ui = Ui_addBiddertoAuction()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, auctionsWindow):
        auctionsWindow.setObjectName("auctionsWindow")
        auctionsWindow.resize(640, 167)
        self.centralwidget = QtWidgets.QWidget(auctionsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startAuctionButton = QtWidgets.QPushButton(self.centralwidget)
        self.startAuctionButton.setObjectName("startAuctionButton")
        self.verticalLayout.addWidget(self.startAuctionButton)
        self.startAuctionButton.clicked.connect(self.showStart)

        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.verticalLayout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.showCreate)

        self.addBidderstoAuctionButton = QtWidgets.QPushButton(self.centralwidget)
        self.addBidderstoAuctionButton.setObjectName("addBidderstoAuctionButton")
        self.verticalLayout.addWidget(self.addBidderstoAuctionButton)
        self.addBidderstoAuctionButton.clicked.connect(self.showAddBidder)

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
        self.startAuctionButton.setText(_translate("auctionsWindow", "Start auction"))
        self.createButton.setText(_translate("auctionsWindow", "Create"))
        self.addBidderstoAuctionButton.setText(_translate("auctionsWindow", "Add bidders to auction"))
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
