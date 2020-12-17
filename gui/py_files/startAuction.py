from PyQt5 import QtCore, QtGui, QtWidgets
import requests

from urls import AuctionGetAll as auctionGetAll
from urls import AuctionStart as start

class Ui_startAuction(object):
    def click(self):
        id = self.auctionCombobox.currentText()
        resp = requests.post(start.format(id))
        if resp.status_code == 200:
            self.response.setText("Started auction correctly " + resp.text)
        else:
            self.response.setText(resp.text)


    def setupUi(self, startAuction):
        startAuction.setObjectName("startAuction")
        startAuction.resize(640, 120)
        self.centralwidget = QtWidgets.QWidget(startAuction)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.auctionLabel = QtWidgets.QLabel(self.centralwidget)
        self.auctionLabel.setObjectName("auctionLabel")
        self.verticalLayout.addWidget(self.auctionLabel)
        self.auctionCombobox = QtWidgets.QComboBox(self.centralwidget)
        self.auctionCombobox.setObjectName("auctionCombobox")
        self.verticalLayout.addWidget(self.auctionCombobox)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.startButton.clicked.connect(self.click)

        self.response = QtWidgets.QLabel(self.centralwidget)
        self.response.setText("")
        self.response.setObjectName("response")
        self.verticalLayout.addWidget(self.response)
        startAuction.setCentralWidget(self.centralwidget)

        self.auctionCombobox.clear()
        self.auctionCombobox.addItem('')
        response = requests.get(auctionGetAll)
        if response.status_code == 200:
            json = response.json()
            for i in json:
                text = str(i['auctionId'])
                self.auctionCombobox.addItem(text)

        self.retranslateUi(startAuction)
        QtCore.QMetaObject.connectSlotsByName(startAuction)

    def retranslateUi(self, startAuction):
        _translate = QtCore.QCoreApplication.translate
        startAuction.setWindowTitle(_translate("startAuction", "Start auction"))
        self.auctionLabel.setText(_translate("startAuction", "Choose auction"))
        self.startButton.setText(_translate("startAuction", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    startAuction = QtWidgets.QMainWindow()
    ui = Ui_startAuction()
    ui.setupUi(startAuction)
    startAuction.show()
    sys.exit(app.exec_())
