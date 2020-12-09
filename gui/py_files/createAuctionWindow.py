from PyQt5 import QtCore, QtGui, QtWidgets
import requests


from urls import ItemGetAll as itemGetAll
from urls import AuctionAdd as urlAdd



class Ui_MainWindow(object):
    def createAuction(self):
        text = self.itemsCombobox.currentText()
        i = text.split(' ', 1)
        resp=requests.post(urlAdd, json={"item":i[0]})
        if resp.status_code == 200:
            json = resp.json()
            auctionId = json['auctionId']
            self.response.setText("Added item to auction correctly. Auction ID: "+str(auctionId))

        else:
            self.response.setText(resp.text)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 120)
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
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.verticalLayout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.createAuction)

        self.response = QtWidgets.QLabel(self.centralwidget)
        self.response.setText("")
        self.response.setObjectName("response")
        self.verticalLayout.addWidget(self.response)
        MainWindow.setCentralWidget(self.centralwidget)

        self.itemsCombobox.clear()
        self.itemsCombobox.addItem('')
        resp = requests.get(itemGetAll)
        if resp.status_code == 200:
            json = resp.json()
            print(json)
            for i in json:
                text = str(i['itemId']) + ' ' + i['name']
                self.itemsCombobox.addItem(text)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Create Auction"))
        self.itemLabel.setText(_translate("MainWindow", "Choose item"))
        self.createButton.setText(_translate("MainWindow", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
