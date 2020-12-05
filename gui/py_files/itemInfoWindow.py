from PyQt5 import QtCore, QtGui, QtWidgets
import requests

from urls import ItemGetAll as urlGetAll
from urls import ItemGet as urlGet

class Ui_itemInfoWindow(object):
    def click(self):
        text = self.chooseItemComboBox.currentText()
        i = text.split(' ', 1)
        send = requests.get(urlGet.format(i[0]))
        if send.status_code == 200:
            json = send.json()
            self.nameOutput.setText(json['name'])
            self.valueOutput.setText(str(json['value']))
            self.yearOutput.setText(str(json['year']))


    def setupUi(self, itemInfoWindow):
        itemInfoWindow.setObjectName("itemInfoWindow")
        itemInfoWindow.resize(640, 161)
        self.centralwidget = QtWidgets.QWidget(itemInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.yearLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearLabel.setObjectName("yearLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.yearLabel)
        self.valueLabel = QtWidgets.QLabel(self.centralwidget)
        self.valueLabel.setObjectName("valueLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.valueLabel)
        self.nameOutput = QtWidgets.QLabel(self.centralwidget)
        self.nameOutput.setText("")
        self.nameOutput.setObjectName("nameOutput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameOutput)
        self.yearOutput = QtWidgets.QLabel(self.centralwidget)
        self.yearOutput.setText("")
        self.yearOutput.setObjectName("yearOutput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.yearOutput)
        self.valueOutput = QtWidgets.QLabel(self.centralwidget)
        self.valueOutput.setText("")
        self.valueOutput.setObjectName("valueOutput")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.valueOutput)
        self.chooseItemComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseItemComboBox.setObjectName("chooseItemComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.chooseItemComboBox)
        self.chooseItemButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseItemButton.setObjectName("chooseItemButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.chooseItemButton)
        itemInfoWindow.setCentralWidget(self.centralwidget)

        self.chooseItemButton.clicked.connect(self.click)

        self.chooseItemComboBox.clear()
        self.chooseItemComboBox.addItem('')
        resp = requests.get(urlGetAll)
        if resp.status_code == 200:
            json = resp.json()
            print(json)
            for i in json:
                text = str(i['itemId']) + ' ' + i['name']
                self.chooseItemComboBox.addItem(text)

        self.retranslateUi(itemInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(itemInfoWindow)

    def retranslateUi(self, itemInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        itemInfoWindow.setWindowTitle(_translate("itemInfoWindow", "Item Info"))
        self.nameLabel.setText(_translate("itemInfoWindow", "Name"))
        self.yearLabel.setText(_translate("itemInfoWindow", "Year"))
        self.valueLabel.setText(_translate("itemInfoWindow", "Value"))
        self.chooseItemButton.setText(_translate("itemInfoWindow", "Get info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    itemInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_itemInfoWindow()
    ui.setupUi(itemInfoWindow)
    itemInfoWindow.show()
    sys.exit(app.exec_())
