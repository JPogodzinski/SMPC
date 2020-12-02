from PyQt5 import QtCore, QtGui, QtWidgets
import requests


class Ui_itemInfoWindow(object):
    def setupUi(self, itemInfoWindow):
        itemInfoWindow.setObjectName("itemInfoWindow")
        itemInfoWindow.resize(640, 74)
        self.centralwidget = QtWidgets.QWidget(itemInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseItemComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseItemComboBox.setObjectName("chooseItemComboBox")
        self.verticalLayout.addWidget(self.chooseItemComboBox)
        self.chooseItemButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseItemButton.setObjectName("chooseItemButton")
        self.verticalLayout.addWidget(self.chooseItemButton)
        itemInfoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(itemInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(itemInfoWindow)

    def retranslateUi(self, itemInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        itemInfoWindow.setWindowTitle(_translate("itemInfoWindow", "Item Info"))
        self.chooseItemButton.setText(_translate("itemInfoWindow", "Get info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    itemInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_itemInfoWindow()
    ui.setupUi(itemInfoWindow)
    itemInfoWindow.show()
    sys.exit(app.exec_())
