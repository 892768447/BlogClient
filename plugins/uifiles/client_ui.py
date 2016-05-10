# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BlogFormClient(object):
    def setupUi(self, BlogFormClient):
        BlogFormClient.setObjectName("BlogFormClient")
        BlogFormClient.resize(400, 300)
        self.vLayout = QtWidgets.QVBoxLayout(BlogFormClient)
        self.vLayout.setContentsMargins(0, 0, 0, 0)
        self.vLayout.setSpacing(0)
        self.vLayout.setObjectName("vLayout")
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setContentsMargins(0, 0, 0, 0)
        self.hLayout.setSpacing(0)
        self.hLayout.setObjectName("hLayout")
        self.vLayout.addLayout(self.hLayout)

        self.retranslateUi(BlogFormClient)
        QtCore.QMetaObject.connectSlotsByName(BlogFormClient)

    def retranslateUi(self, BlogFormClient):
        _translate = QtCore.QCoreApplication.translate
        BlogFormClient.setWindowTitle(_translate("BlogFormClient", "Blog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlogFormClient = QtWidgets.QWidget()
    ui = Ui_BlogFormClient()
    ui.setupUi(BlogFormClient)
    BlogFormClient.show()
    sys.exit(app.exec_())

