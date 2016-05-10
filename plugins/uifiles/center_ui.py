# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'center_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BlogFormCenter(object):
    def setupUi(self, BlogFormCenter):
        BlogFormCenter.setObjectName("BlogFormCenter")
        BlogFormCenter.resize(400, 400)
        BlogFormCenter.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(BlogFormCenter)
        self.verticalLayout.setContentsMargins(20, 35, 20, 35)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.blog_notice_widget = QtWidgets.QWidget(BlogFormCenter)
        self.blog_notice_widget.setObjectName("blog_notice_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.blog_notice_widget)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.blog_notice_label = QtWidgets.QLabel(self.blog_notice_widget)
        self.blog_notice_label.setAlignment(QtCore.Qt.AlignCenter)
        self.blog_notice_label.setObjectName("blog_notice_label")
        self.horizontalLayout.addWidget(self.blog_notice_label)
        self.blog_notice_content_label = QtWidgets.QLabel(self.blog_notice_widget)
        self.blog_notice_content_label.setText("")
        self.blog_notice_content_label.setObjectName("blog_notice_content_label")
        self.horizontalLayout.addWidget(self.blog_notice_content_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.blog_notice_widget)
        self.blog_center_widget = QtWidgets.QStackedWidget(BlogFormCenter)
        self.blog_center_widget.setObjectName("blog_center_widget")
        self.blog_list_page = QtWidgets.QWidget()
        self.blog_list_page.setObjectName("blog_list_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.blog_list_page)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.blog_list_widget = QtWidgets.QListWidget(self.blog_list_page)
        self.blog_list_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blog_list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.blog_list_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.blog_list_widget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.blog_list_widget.setObjectName("blog_list_widget")
        self.horizontalLayout_2.addWidget(self.blog_list_widget)
        self.blog_center_widget.addWidget(self.blog_list_page)
        self.blog_content_page = QtWidgets.QWidget()
        self.blog_content_page.setObjectName("blog_content_page")
        self.blog_center_widget.addWidget(self.blog_content_page)
        self.verticalLayout.addWidget(self.blog_center_widget)
        self.blog_progress_label = QtWidgets.QLabel(BlogFormCenter)
        self.blog_progress_label.setText("")
        self.blog_progress_label.setAlignment(QtCore.Qt.AlignCenter)
        self.blog_progress_label.setObjectName("blog_progress_label")
        self.verticalLayout.addWidget(self.blog_progress_label)
        self.blog_copyright_label = QtWidgets.QLabel(BlogFormCenter)
        self.blog_copyright_label.setOpenExternalLinks(True)
        self.blog_copyright_label.setObjectName("blog_copyright_label")
        self.verticalLayout.addWidget(self.blog_copyright_label)

        self.retranslateUi(BlogFormCenter)
        self.blog_center_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BlogFormCenter)

    def retranslateUi(self, BlogFormCenter):
        _translate = QtCore.QCoreApplication.translate
        self.blog_notice_label.setText(_translate("BlogFormCenter", "公告"))
        self.blog_copyright_label.setText(_translate("BlogFormCenter", "<html><head/><body><p><span style=\" color:#999999;\">COPYRIGHT © </span><a href=\"http://user.qzone.qq.com/892768447\"><span style=\" text-decoration: none; color:#666666;\">Irony.&quot;[讽刺]</span></a><span style=\" color:#999999;\"> | THEME BY </span><a href=\"http://user.qzone.qq.com/892768447\"><span style=\" text-decoration: none; color:#666666;\">Irony.&quot;[讽刺]</span></a></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlogFormCenter = QtWidgets.QWidget()
    ui = Ui_BlogFormCenter()
    ui.setupUi(BlogFormCenter)
    BlogFormCenter.show()
    sys.exit(app.exec_())

