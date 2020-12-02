import requests
from PyQt5 import QtCore, QtGui, QtWidgets

bidderIdList=[]

class Ui_deleteBidderWindow(object):
    def click(self):
        bidderId = str(self.playerComboBox.currentIndex())
        send = requests.post("127.0.1.1:8000/bidder/delete/{}".format(bidderId))
        print(send.status_code)

    def setupUi(self, deleteBidderWindow):
        deleteBidderWindow.setObjectName("deleteBidderWindow")
        deleteBidderWindow.resize(640, 78)
        self.centralwidget = QtWidgets.QWidget(deleteBidderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseBidderCombobox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseBidderCombobox.setObjectName("chooseBidderCombobox")
        self.verticalLayout.addWidget(self.chooseBidderCombobox)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.deleteButton.clicked.connect(self.click)
        deleteBidderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(deleteBidderWindow)
        QtCore.QMetaObject.connectSlotsByName(deleteBidderWindow)

        self.chooseBidderCombobox.clear()
        self.chooseBidderCombobox.addItem('')
        response = requests.get("127.0.0.1:8080/bidder/get-all")
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                text = i['firstName'] + ' ' + i['surname']
                bidderIdList.append(i['bidderId'])
                self.playerComboBox.addItem(text)
        print(bidderIdList)

    def retranslateUi(self, deleteBidderWindow):
        _translate = QtCore.QCoreApplication.translate
        deleteBidderWindow.setWindowTitle(_translate("deleteBidderWindow", "Delete Bidder"))
        self.deleteButton.setText(_translate("deleteBidderWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteBidderWindow = QtWidgets.QMainWindow()
    ui = Ui_deleteBidderWindow()
    ui.setupUi(deleteBidderWindow)
    deleteBidderWindow.show()
    sys.exit(app.exec_())
