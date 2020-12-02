from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtWidgets import QTableWidgetItem

url="127.0.0.1:8080/bidder/get-all"


class Ui_listOfBiddersWindow(object):
    def setupUi(self, listOfBiddersWindow):
        listOfBiddersWindow.setObjectName("listOfBiddersWindow")
        listOfBiddersWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(listOfBiddersWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        listOfBiddersWindow.setCentralWidget(self.centralwidget)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(('First Name', 'Surname'))
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        # tableWindow.setCentralWidget(self.centralwidget)
        #
        # self.retranslateUi(tableWindow)
        # QtCore.QMetaObject.connectSlotsByName(tableWindow)

        self.retranslateUi(listOfBiddersWindow)
        QtCore.QMetaObject.connectSlotsByName(listOfBiddersWindow)

        self.setFixedSize(self.verticalLayout.sizeHint())

        # response=requests.get(url)
        # if response.status_code==200:
        #     json=response.json()
        #     print(json)
        #     for i in json:
        #         firstName=i['firstName']
        #         surname=i['surname']
        #         rowPosition = self.tableWidget.rowCount()
        #         self.tableWidget.insertRow(rowPosition)
        #         self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(firstName))
        #         self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(surname))

    def retranslateUi(self, listOfBiddersWindow):
        _translate = QtCore.QCoreApplication.translate
        listOfBiddersWindow.setWindowTitle(_translate("listOfBiddersWindow", "List of Bidders"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listOfBiddersWindow = QtWidgets.QMainWindow()
    ui = Ui_listOfBiddersWindow()
    ui.setupUi(listOfBiddersWindow)
    listOfBiddersWindow.show()
    sys.exit(app.exec_())
