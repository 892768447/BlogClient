# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'left_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BlogFormLeft(object):
    def setupUi(self, BlogFormLeft):
        BlogFormLeft.setObjectName("BlogFormLeft")
        BlogFormLeft.resize(300, 500)
        BlogFormLeft.setWindowTitle("")
        self.gridLayout = QtWidgets.QGridLayout(BlogFormLeft)
        self.gridLayout.setContentsMargins(20, 30, 20, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.blog_title_label = QtWidgets.QLabel(BlogFormLeft)
        self.blog_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.blog_title_label.setObjectName("blog_title_label")
        self.gridLayout.addWidget(self.blog_title_label, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.blog_head_label = QtWidgets.QPushButton(BlogFormLeft)
        self.blog_head_label.setText("")
        self.blog_head_label.setFlat(True)
        self.blog_head_label.setObjectName("blog_head_label")
        self.gridLayout.addWidget(self.blog_head_label, 0, 1, 1, 1)
        self.blog_menu_list = QtWidgets.QListWidget(BlogFormLeft)
        self.blog_menu_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blog_menu_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.blog_menu_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.blog_menu_list.setObjectName("blog_menu_list")
        self.gridLayout.addWidget(self.blog_menu_list, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        self.blog_search_widget = QtWidgets.QWidget(BlogFormLeft)
        self.blog_search_widget.setObjectName("blog_search_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.blog_search_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.blog_search_edit = QtWidgets.QLineEdit(self.blog_search_widget)
        self.blog_search_edit.setObjectName("blog_search_edit")
        self.horizontalLayout.addWidget(self.blog_search_edit)
        self.blog_search_button = QtWidgets.QPushButton(self.blog_search_widget)
        self.blog_search_button.setText("")
        self.blog_search_button.setObjectName("blog_search_button")
        self.horizontalLayout.addWidget(self.blog_search_button)
        self.gridLayout.addWidget(self.blog_search_widget, 2, 0, 1, 3)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(3, 4)

        self.retranslateUi(BlogFormLeft)
        QtCore.QMetaObject.connectSlotsByName(BlogFormLeft)

    def retranslateUi(self, BlogFormLeft):
        _translate = QtCore.QCoreApplication.translate
        self.blog_title_label.setText(_translate("BlogFormLeft", "Mzone"))
        self.blog_search_edit.setPlaceholderText(_translate("BlogFormLeft", "搜索..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlogFormLeft = QtWidgets.QWidget()
    ui = Ui_BlogFormLeft()
    ui.setupUi(BlogFormLeft)
    BlogFormLeft.show()
    sys.exit(app.exec_())

