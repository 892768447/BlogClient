# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'left_link_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BlogFormLeftLink(object):
    def setupUi(self, BlogFormLeftLink):
        BlogFormLeftLink.setObjectName("BlogFormLeftLink")
        BlogFormLeftLink.resize(94, 470)
        BlogFormLeftLink.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(BlogFormLeftLink)
        self.verticalLayout.setContentsMargins(12, 35, 12, 30)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.blog_qq_button = QtWidgets.QPushButton(BlogFormLeftLink)
        self.blog_qq_button.setText("")
        self.blog_qq_button.setObjectName("blog_qq_button")
        self.verticalLayout.addWidget(self.blog_qq_button)
        self.blog_group_button = QtWidgets.QPushButton(BlogFormLeftLink)
        self.blog_group_button.setText("")
        self.blog_group_button.setObjectName("blog_group_button")
        self.verticalLayout.addWidget(self.blog_group_button)
        self.blog_weixin_button = QtWidgets.QPushButton(BlogFormLeftLink)
        self.blog_weixin_button.setText("")
        self.blog_weixin_button.setObjectName("blog_weixin_button")
        self.verticalLayout.addWidget(self.blog_weixin_button)
        self.blog_login_button = QtWidgets.QPushButton(BlogFormLeftLink)
        self.blog_login_button.setText("")
        self.blog_login_button.setObjectName("blog_login_button")
        self.verticalLayout.addWidget(self.blog_login_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.blog_up_button = QtWidgets.QPushButton(BlogFormLeftLink)
        self.blog_up_button.setText("")
        self.blog_up_button.setObjectName("blog_up_button")
        self.verticalLayout.addWidget(self.blog_up_button)

        self.retranslateUi(BlogFormLeftLink)
        QtCore.QMetaObject.connectSlotsByName(BlogFormLeftLink)

    def retranslateUi(self, BlogFormLeftLink):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlogFormLeftLink = QtWidgets.QWidget()
    ui = Ui_BlogFormLeftLink()
    ui.setupUi(BlogFormLeftLink)
    BlogFormLeftLink.show()
    sys.exit(app.exec_())

