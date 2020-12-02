from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from urls import AuctionGetAll as getAll

global auctions

class Ui_auctionInfoWindow(object):
    def click(self):
        print()

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
        self.chooseAuctionButton.clicked.connect(self.click)
        auctionInfoWindow.setCentralWidget(self.centralwidget)

        self.chooseAuctionComboBox.clear()
        self.chooseAuctionComboBox.addItem('')
        auctions=[0]
        response=requests.get(getAll)
        print(response.status_code)
        if response.status_code==200:
            json=response.json()
            print(json)
            for i in json:
                text=i['id']
                self.chooseAuctionComboBox.addItem(text)
                auctions.append(text)



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
