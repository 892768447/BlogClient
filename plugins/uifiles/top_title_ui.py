# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'top_title_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BlogFormTitleBar(object):
    def setupUi(self, BlogFormTitleBar):
        BlogFormTitleBar.setObjectName("BlogFormTitleBar")
        BlogFormTitleBar.resize(500, 30)
        BlogFormTitleBar.setWindowTitle("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(BlogFormTitleBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.blog_min_button = QtWidgets.QPushButton(BlogFormTitleBar)
        self.blog_min_button.setText("")
        self.blog_min_button.setObjectName("blog_min_button")
        self.horizontalLayout.addWidget(self.blog_min_button)
        self.blog_max_button = QtWidgets.QPushButton(BlogFormTitleBar)
        self.blog_max_button.setText("")
        self.blog_max_button.setObjectName("blog_max_button")
        self.horizontalLayout.addWidget(self.blog_max_button)
        self.blog_close_button = QtWidgets.QPushButton(BlogFormTitleBar)
        self.blog_close_button.setText("")
        self.blog_close_button.setObjectName("blog_close_button")
        self.horizontalLayout.addWidget(self.blog_close_button)

        self.retranslateUi(BlogFormTitleBar)
        QtCore.QMetaObject.connectSlotsByName(BlogFormTitleBar)

    def retranslateUi(self, BlogFormTitleBar):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlogFormTitleBar = QtWidgets.QWidget()
    ui = Ui_BlogFormTitleBar()
    ui.setupUi(BlogFormTitleBar)
    BlogFormTitleBar.show()
    sys.exit(app.exec_())

