from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from urls import ItemDelete as urlDelete
from urls import ItemGetAll as urlGetAll


class Ui_deleteItemWindow(object):
    def click(self):
        text = self.chooseItemCombobox.currentText()
        i = text.split(' ', 1)
        send = requests.delete(urlDelete.format(i[0]))
        if send.status_code == 200:
            self.response.setText("Deleted item correctly")
        else:
            self.response.setText(send.text)

    def setupUi(self, deleteItemWindow):
        deleteItemWindow.setObjectName("deleteItemWindow")
        deleteItemWindow.resize(640, 74)
        self.centralwidget = QtWidgets.QWidget(deleteItemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseItemCombobox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseItemCombobox.setObjectName("chooseItemCombobox")
        self.verticalLayout.addWidget(self.chooseItemCombobox)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)

        self.deleteButton.clicked.connect(self.click)

        self.response = QtWidgets.QLabel(self.centralwidget)
        self.response.setText("")
        self.response.setObjectName("response")
        self.verticalLayout.addWidget(self.response)
        deleteItemWindow.setCentralWidget(self.centralwidget)


        self.chooseItemCombobox.clear()
        self.chooseItemCombobox.addItem('')
        resp = requests.get(urlGetAll)
        if resp.status_code == 200:
            json = resp.json()
            print(json)
            for i in json:
                text = str(i['itemId'])+' '+i['name']
                self.chooseItemCombobox.addItem(text)

        self.retranslateUi(deleteItemWindow)
        QtCore.QMetaObject.connectSlotsByName(deleteItemWindow)

    def retranslateUi(self, deleteItemWindow):
        _translate = QtCore.QCoreApplication.translate
        deleteItemWindow.setWindowTitle(_translate("deleteItemWindow", "Delete Item"))
        self.deleteButton.setText(_translate("deleteItemWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteItemWindow = QtWidgets.QMainWindow()
    ui = Ui_deleteItemWindow()
    ui.setupUi(deleteItemWindow)
    deleteItemWindow.show()
    sys.exit(app.exec_())
