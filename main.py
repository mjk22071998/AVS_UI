# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'avs.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_Form(object):


    def __init__(self):
        self.selectFile = None
        self.fileName=""

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(723, 542)
        self.selectFile = QtWidgets.QPushButton(Form)
        self.selectFile.setGeometry(QtCore.QRect(30, 50, 141, 25))
        self.selectFile.setObjectName("selectFile")
        self.selectFile.clicked.connect(self.selectImageClicker)
        self.decodeFile = QtWidgets.QPushButton(Form)
        self.decodeFile.setGeometry(QtCore.QRect(30, 120, 141, 25))
        self.decodeFile.setObjectName("decodeFile")
        self.decodeFile.clicked.connect(self.decodeImageClicker)
        self.extractFeatures = QtWidgets.QPushButton(Form)
        self.extractFeatures.setGeometry(QtCore.QRect(30, 290, 141, 25))
        self.extractFeatures.setObjectName("extractFeatures")
        self.testAIModel = QtWidgets.QPushButton(Form)
        self.testAIModel.setGeometry(QtCore.QRect(30, 380, 141, 25))
        self.testAIModel.setObjectName("testAIModel")
        self.createImage = QtWidgets.QPushButton(Form)
        self.createImage.setGeometry(QtCore.QRect(30, 200, 141, 25))
        self.createImage.setObjectName("createImage")
        self.createImage.clicked.connect(self.displayImageClicker)
        self.imageLable = QtWidgets.QLabel(Form)
        self.imageLable.setGeometry(QtCore.QRect(480, 220, 67, 17))
        self.imageLable.setObjectName("imageLable")
        self.actionOpen_File = QtWidgets.QAction(Form)
        self.actionOpen_File.setObjectName("actionOpen_File")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.selectFile.setText(_translate("Form", "Select file"))
        self.decodeFile.setText(_translate("Form", "Decode file"))
        self.extractFeatures.setText(_translate("Form", "Extract features"))
        self.testAIModel.setText(_translate("Form", "Test AI model"))
        self.createImage.setText(_translate("Form", "Create image"))
        self.imageLable.setText(_translate("Form", "TextLabel"))
        self.actionOpen_File.setText(_translate("Form", "Open File"))

    def selectImageClicker(self):
        print("Select Image clicked")
        self.openFileNameDialog()

    def decodeImageClicker(self):
        print("Decode Image clicked")
        os.system("python3 apktoimage.py "+self.fileName+" .")

    def displayImageClicker(self):
        print("Select Image clicked")

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, path = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                     "APK Files (*.apk)", options=options)
        if self.fileName:
            print(self.fileName)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
