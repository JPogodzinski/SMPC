from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from itemInfoWindow import Ui_itemInfoWindow
from deleteItemWindow import Ui_deleteItemWindow
from addItemWindow import Ui_addItemWindow


class Ui_itemWindow(object):
    def showAdd(self):
        self.window = QMainWindow()
        self.ui = Ui_addItemWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def showDelete(self):
        self.window = QMainWindow()
        self.ui = Ui_deleteItemWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def showInfo(self):
        self.window = QMainWindow()
        self.ui = Ui_itemInfoWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, itemWindow):
        itemWindow.setObjectName("itemWindow")
        itemWindow.resize(640, 136)
        self.centralwidget = QtWidgets.QWidget(itemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.addButton.clicked.connect(self.showAdd)

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.deleteButton.clicked.connect(self.showDelete)

        self.getInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.getInfoButton.setObjectName("getInfoButton")
        self.verticalLayout.addWidget(self.getInfoButton)
        self.getInfoButton.clicked.connect(self.showInfo)


        itemWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(itemWindow)
        QtCore.QMetaObject.connectSlotsByName(itemWindow)

    def retranslateUi(self, itemWindow):
        _translate = QtCore.QCoreApplication.translate
        itemWindow.setWindowTitle(_translate("itemWindow", "Items"))
        self.addButton.setText(_translate("itemWindow", "Add"))
        self.deleteButton.setText(_translate("itemWindow", "Delete"))
        self.getInfoButton.setText(_translate("itemWindow", "Get info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    itemWindow = QtWidgets.QMainWindow()
    ui = Ui_itemWindow()
    ui.setupUi(itemWindow)
    itemWindow.show()
    sys.exit(app.exec_())
