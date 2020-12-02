from PyQt5 import QtCore, QtGui, QtWidgets
import requests

url="127.0.0.1:8080/item/get-all"

class Ui_deleteItemWindow(object):
    def click(self):
        print()
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
        deleteItemWindow.setCentralWidget(self.centralwidget)

        self.chooseItemCombobox.clear()
        self.chooseItemCombobox.addItem('')
        itemsList= []
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                text = i['name']
                self.teamsList.addItem(text)

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
