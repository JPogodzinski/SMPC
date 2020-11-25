# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pogoda/dev/SMPC/gui/deleteItemWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deleteItemWindow(object):
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
