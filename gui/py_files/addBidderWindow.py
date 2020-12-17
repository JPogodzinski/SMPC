from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from urls import BidderAdd as urlAdd

class Ui_addBidderWindow(object):
    def click(self):
        self.response.setText('')
        firstName=self.firstNameInput.text()
        surname=self.surnameInput.text()
        resp=requests.post(urlAdd, json={
            "firstName":firstName,
            "surname":surname
        })
        if resp.status_code==200:
            self.response.setText("Added bidder correctly")
        else:
            self.response.setText(resp.text)

    def setupUi(self, addBidderWindow):
        addBidderWindow.setObjectName("addBidderWindow")
        addBidderWindow.resize(640, 123)
        self.centralwidget = QtWidgets.QWidget(addBidderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNameInput.setObjectName("firstNameInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.firstNameInput)
        self.surnameLabel = QtWidgets.QLabel(self.centralwidget)
        self.surnameLabel.setObjectName("surnameLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.surnameLabel)
        self.surnameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameInput.setObjectName("surnameInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.surnameInput)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setObjectName("applyButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.applyButton)
        self.applyButton.clicked.connect(self.click)

        self.response = QtWidgets.QLabel(self.centralwidget)
        self.response.setText("")
        self.response.setObjectName("response")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.response)

        addBidderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(addBidderWindow)
        QtCore.QMetaObject.connectSlotsByName(addBidderWindow)

    def retranslateUi(self, addBidderWindow):
        _translate = QtCore.QCoreApplication.translate
        addBidderWindow.setWindowTitle(_translate("addBidderWindow", "Add Bidder"))
        self.firstNameLabel.setText(_translate("addBidderWindow", "First name"))
        self.surnameLabel.setText(_translate("addBidderWindow", "Surname"))
        self.applyButton.setText(_translate("addBidderWindow", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addBidderWindow = QtWidgets.QMainWindow()
    ui = Ui_addBidderWindow()
    ui.setupUi(addBidderWindow)
    addBidderWindow.show()
    sys.exit(app.exec_())
