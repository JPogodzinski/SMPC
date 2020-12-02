from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtWidgets import QTableWidgetItem

url="127.0.0.1:8080/item/get-all"

class Ui_listOfItemsWindow(object):
    def setupUi(self, listOfItemsWindow):
        listOfItemsWindow.setObjectName("listOfItemsWindow")
        listOfItemsWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(listOfItemsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        listOfItemsWindow.setCentralWidget(self.centralwidget)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(('Name', 'Year', 'Value'))
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        # response=requests.get(url)
        # if response.status_code==200:
        #     json=response.json()
        #     print(json)
        #     for i in json:
        #         name=i['name']
        #         year=i['year']
        #         value=i['value']
        #         rowPosition = self.tableWidget.rowCount()
        #         self.tableWidget.insertRow(rowPosition)
        #         self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(name))
        #         self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(year))
        #         self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(value))

        self.retranslateUi(listOfItemsWindow)
        QtCore.QMetaObject.connectSlotsByName(listOfItemsWindow)


    def retranslateUi(self, listOfItemsWindow):
        _translate = QtCore.QCoreApplication.translate
        listOfItemsWindow.setWindowTitle(_translate("listOfItemsWindow", "List of Items"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listOfItemsWindow = QtWidgets.QMainWindow()
    ui = Ui_listOfItemsWindow()
    ui.setupUi(listOfItemsWindow)
    listOfItemsWindow.show()
    sys.exit(app.exec_())
