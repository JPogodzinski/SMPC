from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from urls import AuctionGetAll as urlGetAll
from urls import AuctionDelete as urlDelete


class Ui_MainWindow(object):
    def click(self):
        id=self.chooseAuctionCombobox.currentIndex()
        resp=requests.delete(urlDelete.format(id))
        if resp.status_code==200:
            self.response.setText("Deleted auction correctly")
        else:
            self.response.setText(resp.text)


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
        self.deleteButton.clicked.connect(self.click)
        self.response = QtWidgets.QLabel(self.centralwidget)
        self.response.setText("")
        self.response.setObjectName("response")
        self.verticalLayout.addWidget(self.response)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.chooseAuctionCombobox.clear()
        self.chooseAuctionCombobox.addItem('')
        response = requests.get(urlGetAll)
        if response.status_code == 200:
            json = response.json()
            for i in json:
                text = str(i['auctionId'])
                self.chooseAuctionCombobox.addItem(text)

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
