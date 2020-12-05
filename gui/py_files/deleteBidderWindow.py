from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from urls import BidderDelete as urlDelete
from urls import BidderGetAll as urlGetAll


class Ui_deleteBidderWindow(object):
    def click(self):
        text=self.chooseBidderCombobox.currentText()
        i=text.split(' ',1)
        send = requests.delete(urlDelete.format(i[0]))
        if send.status_code == 200:
            self.response.setText("Deleted bidder correctly")
        else:
            self.response.setText("Something went wrong")


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
        self.response = QtWidgets.QLabel(self.centralwidget)
        self.response.setText("")
        self.response.setObjectName("response")
        self.verticalLayout.addWidget(self.response)
        deleteBidderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(deleteBidderWindow)
        QtCore.QMetaObject.connectSlotsByName(deleteBidderWindow)

        self.chooseBidderCombobox.clear()
        self.chooseBidderCombobox.addItem('')
        resp = requests.get(urlGetAll)
        if resp.status_code == 200:
            json = resp.json()
            print(json)
            for i in json:
                text = str(i['bidderId'])+' '+i['firstName'] + ' ' + i['surname']
                self.chooseBidderCombobox.addItem(text)

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
