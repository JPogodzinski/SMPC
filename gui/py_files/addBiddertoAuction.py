from PyQt5 import QtCore, QtGui, QtWidgets
import requests


from urls import BidderGetAll as bidderGetAll
from urls import AuctionGetAll as auctionGetAll
from urls import AuctionAddBidder as urlAddBidder



class Ui_addBiddertoAuction(object):
    def addBidder(self):
        id = self.auctionCombobox.currentText()
        bid1 = self.biddersCombo1.currentText()
        bid1 = bid1.split(' ', 1)
        send = requests.post(urlAddBidder.format(id, bid1[0]))
        if send.status_code==200:
            self.response.setText("Added bidder to auction correctly")
        else:
            self.response.setText(send.text)

    def setupUi(self, addBiddertoAuction):
        addBiddertoAuction.setObjectName("addBiddertoAuction")
        addBiddertoAuction.resize(640, 174)
        self.centralwidget = QtWidgets.QWidget(addBiddertoAuction)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.auctionLabel = QtWidgets.QLabel(self.centralwidget)
        self.auctionLabel.setObjectName("auctionLabel")
        self.verticalLayout.addWidget(self.auctionLabel)
        self.auctionCombobox = QtWidgets.QComboBox(self.centralwidget)
        self.auctionCombobox.setObjectName("auctionCombobox")
        self.verticalLayout.addWidget(self.auctionCombobox)
        self.biddersLabel = QtWidgets.QLabel(self.centralwidget)
        self.biddersLabel.setObjectName("biddersLabel")
        self.verticalLayout.addWidget(self.biddersLabel)
        self.biddersCombo1 = QtWidgets.QComboBox(self.centralwidget)
        self.biddersCombo1.setObjectName("biddersCombo1")
        self.verticalLayout.addWidget(self.biddersCombo1)
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.verticalLayout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.addBidder)
        self.response = QtWidgets.QLabel(self.centralwidget)
        self.response.setText("")
        self.response.setObjectName("response")
        self.verticalLayout.addWidget(self.response)
        addBiddertoAuction.setCentralWidget(self.centralwidget)

        self.auctionCombobox.clear()
        self.auctionCombobox.addItem('')
        response = requests.get(auctionGetAll)
        if response.status_code == 200:
            json = response.json()
            for i in json:
                text = str(i['auctionId'])
                self.auctionCombobox.addItem(text)

        self.biddersCombo1.clear()
        self.biddersCombo1.addItem('')
        resp = requests.get(bidderGetAll)
        if resp.status_code == 200:
            json = resp.json()
            for i in json:
                text = str(i['bidderId']) + ' ' + i['firstName'] + ' ' + i['surname']
                self.biddersCombo1.addItem(text)

        self.retranslateUi(addBiddertoAuction)
        QtCore.QMetaObject.connectSlotsByName(addBiddertoAuction)

    def retranslateUi(self, addBiddertoAuction):
        _translate = QtCore.QCoreApplication.translate
        addBiddertoAuction.setWindowTitle(_translate("addBiddertoAuction", "Add bidder to auction"))
        self.auctionLabel.setText(_translate("addBiddertoAuction", "Choose auction"))
        self.biddersLabel.setText(_translate("addBiddertoAuction", "Choose bidders (max 5 bidders in auction)"))
        self.createButton.setText(_translate("addBiddertoAuction", "Add bidder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addBiddertoAuction = QtWidgets.QMainWindow()
    ui = Ui_addBiddertoAuction()
    ui.setupUi(addBiddertoAuction)
    addBiddertoAuction.show()
    sys.exit(app.exec_())
