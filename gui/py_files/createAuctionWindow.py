from PyQt5 import QtCore, QtGui, QtWidgets
import requests


from urls import BidderGetAll as bidderGetAll
from urls import ItemGetAll as itemGetAll
from urls import AuctionAdd as urlAdd


class Ui_MainWindow(object):
    def createAuction(self):
        text = self.itemsCombobox.currentText()
        i = text.split(' ', 1)
        resp=requests.post(urlAdd, json={"item":i[0]})
        print(resp.status_code)
        if resp.status_code == 200:
            self.response1.setText("Added item to auction correctly")
            print(resp.content)
            json=resp.json()
            for i in range(len(json)):
               auctionId = json[i]['auctionId']
               print(auctionId)

        else:
            self.response1.setText("Something went wrong")

    def addBidders(self):
        print()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 298)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.itemLabel = QtWidgets.QLabel(self.centralwidget)
        self.itemLabel.setObjectName("itemLabel")
        self.verticalLayout.addWidget(self.itemLabel)
        self.itemsCombobox = QtWidgets.QComboBox(self.centralwidget)
        self.itemsCombobox.setObjectName("itemsCombobox")
        self.verticalLayout.addWidget(self.itemsCombobox)
        self.biddersLabel = QtWidgets.QLabel(self.centralwidget)
        self.biddersLabel.setObjectName("biddersLabel")
        self.verticalLayout.addWidget(self.biddersLabel)
        self.biddersCombo1 = QtWidgets.QComboBox(self.centralwidget)
        self.biddersCombo1.setObjectName("biddersCombo1")
        self.verticalLayout.addWidget(self.biddersCombo1)
        self.biddersCombo2 = QtWidgets.QComboBox(self.centralwidget)
        self.biddersCombo2.setObjectName("biddersCombo2")
        self.verticalLayout.addWidget(self.biddersCombo2)
        self.biddersCombo3 = QtWidgets.QComboBox(self.centralwidget)
        self.biddersCombo3.setObjectName("biddersCombo3")
        self.verticalLayout.addWidget(self.biddersCombo3)
        self.biddersCombo4 = QtWidgets.QComboBox(self.centralwidget)
        self.biddersCombo4.setObjectName("biddersCombo4")
        self.verticalLayout.addWidget(self.biddersCombo4)
        self.biddersCombo5 = QtWidgets.QComboBox(self.centralwidget)
        self.biddersCombo5.setObjectName("biddersCombo5")
        self.verticalLayout.addWidget(self.biddersCombo5)
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.verticalLayout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.createAuction)

        self.response1 = QtWidgets.QLabel(self.centralwidget)
        self.response1.setText("")
        self.response1.setObjectName("response")
        self.verticalLayout.addWidget(self.response1)

        self.biddersCombo1.clear()
        self.biddersCombo1.addItem('')
        self.biddersCombo2.clear()
        self.biddersCombo2.addItem('')
        self.biddersCombo3.clear()
        self.biddersCombo3.addItem('')
        self.biddersCombo4.clear()
        self.biddersCombo4.addItem('')
        self.biddersCombo5.clear()
        self.biddersCombo5.addItem('')
        resp = requests.get(bidderGetAll)
        if resp.status_code == 200:
            json = resp.json()
            print(json)
            for i in json:
                text = str(i['bidderId'])+' '+i['firstName'] + ' ' + i['surname']
                self.biddersCombo1.addItem(text)
                self.biddersCombo2.addItem(text)
                self.biddersCombo3.addItem(text)
                self.biddersCombo4.addItem(text)
                self.biddersCombo5.addItem(text)

        self.itemsCombobox.clear()
        self.itemsCombobox.addItem('')
        resp = requests.get(itemGetAll)
        if resp.status_code == 200:
            json = resp.json()
            print(json)
            for i in json:
                text = str(i['itemId'])+' '+i['name']
                self.itemsCombobox.addItem(text)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Create Auction"))
        self.itemLabel.setText(_translate("MainWindow", "Choose item"))
        self.biddersLabel.setText(_translate("MainWindow", "Choose bidders (1-5)"))
        self.createButton.setText(_translate("MainWindow", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
