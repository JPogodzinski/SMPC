from PyQt5 import QtCore, QtGui, QtWidgets
import requests

get="127.0.0.1:8080/auction/get-all"
delete="127.0.0.1:8080/auction/delete/{}"
global auctions

class Ui_MainWindow(object):
    def click(self):
        id=self.chooseAuctionComboBox.currentIndex()
        for i in auctions:
            if id==i:
                response=requests.delete(delete.format(i))
                print(response.status_code)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 74)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseAuctionCombobox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseAuctionCombobox.setObjectName("chooseAuctionCombobox")
        self.verticalLayout.addWidget(self.chooseAuctionCombobox)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.chooseAuctionCombobox.clear()
        self.chooseAuctionCombobox.addItem('')
        auctions = [0]
        response = requests.get(get)
        print(response.status_code)
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                text = i['id']
                self.chooseAuctionComboBox.addItem(text)
                auctions.append(text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delete Auction"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
