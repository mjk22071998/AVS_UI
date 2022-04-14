import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Ui_Form(object):

    def __init__(self):
        self.filename = None
        self.file = None

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
        self.imageLable.setGeometry(QtCore.QRect(320, 16, 361, 501))
        self.imageLable.setObjectName("imageLable")
        self.actionOpen_File = QtWidgets.QAction(Form)
        self.actionOpen_File.setObjectName("actionOpen_File")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AVS UI"))
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
        self.imageLable.setText("Selected File Name: " + self.file)

    def decodeImageClicker(self):
        print("Decode Image clicked")
        os.system("python3 apktoimage.py " + self.filename + " ./images")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("APk Decoding Complete. Now you can create Image from bytecode")
        msg.setWindowTitle("APK decoding")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def displayImageClicker(self):
        print("Display Image clicked")
        image = "./" + self.file + ".png"
        pixmap = QPixmap(image)
        self.imageLable.setPixmap(pixmap)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.filename, path = QFileDialog.getOpenFileName(None, "Select APK file", ".",
                                                          "All Files (*.*)", options=options)
        self.file = QFileInfo(self.filename).fileName()
        if self.filename:
            print(self.filename)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
