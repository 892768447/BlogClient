# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'right_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BlogFormRight(object):
    def setupUi(self, BlogFormRight):
        BlogFormRight.setObjectName("BlogFormRight")
        BlogFormRight.resize(200, 300)
        BlogFormRight.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(BlogFormRight)
        self.verticalLayout.setContentsMargins(0, 15, 5, 35)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.blog_right_widget = QtWidgets.QTreeWidget(BlogFormRight)
        self.blog_right_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blog_right_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.blog_right_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.blog_right_widget.setIndentation(0)
        self.blog_right_widget.setRootIsDecorated(False)
        self.blog_right_widget.setAnimated(False)
        self.blog_right_widget.setHeaderHidden(True)
        self.blog_right_widget.setExpandsOnDoubleClick(False)
        self.blog_right_widget.setObjectName("blog_right_widget")
        self.verticalLayout.addWidget(self.blog_right_widget)

        self.retranslateUi(BlogFormRight)
        QtCore.QMetaObject.connectSlotsByName(BlogFormRight)

    def retranslateUi(self, BlogFormRight):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlogFormRight = QtWidgets.QWidget()
    ui = Ui_BlogFormRight()
    ui.setupUi(BlogFormRight)
    BlogFormRight.show()
    sys.exit(app.exec_())

