from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from bidderInfoWindow import Ui_bidderInfoWindow
from addBidderWindow import Ui_addBidderWindow
from deleteBidderWindow import Ui_deleteBidderWindow

class Ui_MainWindow(object):
    def showAdd(self):
        self.window = QMainWindow()
        self.ui = Ui_addBidderWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def showDelete(self):
        self.window = QMainWindow()
        self.ui = Ui_deleteBidderWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def showInfo(self):
        self.window = QMainWindow()
        self.ui = Ui_bidderInfoWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 136)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bidders"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.getInfoButton.setText(_translate("MainWindow", "Get info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
