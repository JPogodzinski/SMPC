from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from biddersWindow import Ui_MainWindow
from itemsWindow import Ui_itemWindow
from auctionWindow import Ui_auctionsWindow

class Ui_adminStartWindow(object):
    def showBidders(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def showAuctions(self):
        self.window = QMainWindow()
        self.ui = Ui_auctionsWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def showItems(self):
        self.window = QMainWindow()
        self.ui = Ui_itemWindow()
        self.ui.setupUi(self.window)
        self.window.show()

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
        self.auctionButton.clicked.connect(self.showAuctions)

        self.biddersButton = QtWidgets.QPushButton(self.centralwidget)
        self.biddersButton.setObjectName("biddersButton")
        self.verticalLayout.addWidget(self.biddersButton)
        self.biddersButton.clicked.connect(self.showBidders)

        self.itemsButton = QtWidgets.QPushButton(self.centralwidget)
        self.itemsButton.setObjectName("itemsButton")
        self.verticalLayout.addWidget(self.itemsButton)
        self.itemsButton.clicked.connect(self.showItems)

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
