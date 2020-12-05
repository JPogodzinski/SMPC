from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from urls import AuctionGetAll as getAll


class Ui_auctionInfoWindow(object):
    def click(self):
        text = self.chooseAuctionComboBox.currentText()
        i = text.split(' ', 1)
        resp = requests.get(getAll.format(i[0]))
        if resp.status_code == 200:
            json = resp.json()
            for i in range(len(json)):
                self.auctionIDOutput.setText(str(json[i]['auctionId']))
                self.itemNameOutput.setText(str(json[i]['item']['name']))
                if json[i]['hasBeenFinished']:
                    self.soldOutput.setText('Yes maaaan')
                else:
                    self.soldOutput.setText('Not yet, my friend')

    def setupUi(self, auctionInfoWindow):
        auctionInfoWindow.setObjectName("auctionInfoWindow")
        auctionInfoWindow.resize(640, 161)
        self.centralwidget = QtWidgets.QWidget(auctionInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.auctionIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.auctionIDLabel.setObjectName("auctionIDLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.auctionIDLabel)
        self.itemNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.itemNameLabel.setObjectName("itemNameLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.itemNameLabel)
        self.soldLabel = QtWidgets.QLabel(self.centralwidget)
        self.soldLabel.setObjectName("soldLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.soldLabel)
        self.auctionIDOutput = QtWidgets.QLabel(self.centralwidget)
        self.auctionIDOutput.setText("")
        self.auctionIDOutput.setObjectName("auctionIDOutput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.auctionIDOutput)
        self.itemNameOutput = QtWidgets.QLabel(self.centralwidget)
        self.itemNameOutput.setText("")
        self.itemNameOutput.setObjectName("itemNameOutput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.itemNameOutput)
        self.soldOutput = QtWidgets.QLabel(self.centralwidget)
        self.soldOutput.setText("")
        self.soldOutput.setObjectName("soldOutput")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.soldOutput)
        self.chooseAuctionComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseAuctionComboBox.setObjectName("chooseAuctionComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.chooseAuctionComboBox)
        self.chooseAuctionButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseAuctionButton.setObjectName("chooseAuctionButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.chooseAuctionButton)
        auctionInfoWindow.setCentralWidget(self.centralwidget)

        self.chooseAuctionButton.clicked.connect(self.click)

        self.chooseAuctionComboBox.clear()
        self.chooseAuctionComboBox.addItem('')
        response = requests.get(getAll)
        print(response.status_code)
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                text=str(i['auctionId'])
                self.chooseAuctionComboBox.addItem(text)

        self.retranslateUi(auctionInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(auctionInfoWindow)

    def retranslateUi(self, auctionInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        auctionInfoWindow.setWindowTitle(_translate("auctionInfoWindow", "Auction Info"))
        self.auctionIDLabel.setText(_translate("auctionInfoWindow", "Auction ID"))
        self.itemNameLabel.setText(_translate("auctionInfoWindow", "Item name "))
        self.soldLabel.setText(_translate("auctionInfoWindow", "Sold?"))
        self.chooseAuctionButton.setText(_translate("auctionInfoWindow", "Get info"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    auctionInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_auctionInfoWindow()
    ui.setupUi(auctionInfoWindow)
    auctionInfoWindow.show()
    sys.exit(app.exec_())
