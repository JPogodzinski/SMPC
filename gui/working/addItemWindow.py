# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SMPC/gui/old_guis/addItemWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addItemWindow(object):
    def setupUi(self, addItemWindow):
        addItemWindow.setObjectName("addItemWindow")
        addItemWindow.resize(640, 159)
        self.centralwidget = QtWidgets.QWidget(addItemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setObjectName("nameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameInput)
        self.yearLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearLabel.setObjectName("yearLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.yearLabel)
        self.yearInput = QtWidgets.QLineEdit(self.centralwidget)
        self.yearInput.setObjectName("yearInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.yearInput)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setObjectName("applyButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.applyButton)
        self.valueInput = QtWidgets.QLineEdit(self.centralwidget)
        self.valueInput.setObjectName("valueInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.valueInput)
        self.valueLabel = QtWidgets.QLabel(self.centralwidget)
        self.valueLabel.setObjectName("valueLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.valueLabel)
        self.response = QtWidgets.QLabel(self.centralwidget)
        self.response.setText("")
        self.response.setObjectName("response")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.response)
        addItemWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(addItemWindow)
        QtCore.QMetaObject.connectSlotsByName(addItemWindow)

    def retranslateUi(self, addItemWindow):
        _translate = QtCore.QCoreApplication.translate
        addItemWindow.setWindowTitle(_translate("addItemWindow", "Add Item"))
        self.nameLabel.setText(_translate("addItemWindow", "Name"))
        self.yearLabel.setText(_translate("addItemWindow", "Year"))
        self.applyButton.setText(_translate("addItemWindow", "Apply"))
        self.valueLabel.setText(_translate("addItemWindow", "Value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addItemWindow = QtWidgets.QMainWindow()
    ui = Ui_addItemWindow()
    ui.setupUi(addItemWindow)
    addItemWindow.show()
    sys.exit(app.exec_())
