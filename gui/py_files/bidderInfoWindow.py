from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from urls import BidderGetAll as urlGetAll
from urls import BidderGet as urlGet


class Ui_bidderInfoWindow(object):
    def click(self):
        text=self.chooseBidderComboBox.currentText()
        i=text.split(' ',1)
        send = requests.get(urlGet.format(i[0]))
        if send.status_code == 200:
            json=send.json()
            self.firstNameOutput.setText(json['firstName'])
            self.surnameOutput.setText(json['surname'])

    def setupUi(self, bidderInfoWindow):
        bidderInfoWindow.setObjectName("bidderInfoWindow")
        bidderInfoWindow.resize(640, 132)
        self.centralwidget = QtWidgets.QWidget(bidderInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.surnameLabel = QtWidgets.QLabel(self.centralwidget)
        self.surnameLabel.setObjectName("surnameLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.surnameLabel)
        self.firstNameOutput = QtWidgets.QLabel(self.centralwidget)
        self.firstNameOutput.setText("")
        self.firstNameOutput.setObjectName("firstNameOutput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.firstNameOutput)
        self.surnameOutput = QtWidgets.QLabel(self.centralwidget)
        self.surnameOutput.setText("")
        self.surnameOutput.setObjectName("surnameOutput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.surnameOutput)
        self.chooseBidderComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseBidderComboBox.setObjectName("chooseBidderComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.chooseBidderComboBox)
        self.chooseBidderButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseBidderButton.setObjectName("chooseBidderButton")
        self.chooseBidderButton.clicked.connect(self.click)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.chooseBidderButton)
        bidderInfoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(bidderInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(bidderInfoWindow)

        self.chooseBidderComboBox.clear()
        self.chooseBidderComboBox.addItem('')
        resp = requests.get(urlGetAll)
        if resp.status_code == 200:
            json = resp.json()
            print(json)
            for i in json:
                text = str(i['bidderId']) + ' ' + i['firstName'] + ' ' + i['surname']
                self.chooseBidderComboBox.addItem(text)

    def retranslateUi(self, bidderInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        bidderInfoWindow.setWindowTitle(_translate("bidderInfoWindow", "Bidder Info"))
        self.firstNameLabel.setText(_translate("bidderInfoWindow", "First Name"))
        self.surnameLabel.setText(_translate("bidderInfoWindow", "Surname"))
        self.chooseBidderButton.setText(_translate("bidderInfoWindow", "Get info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bidderInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_bidderInfoWindow()
    ui.setupUi(bidderInfoWindow)
    bidderInfoWindow.show()
    sys.exit(app.exec_())
