# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'center_content_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BlogFormCenterContent(object):
    def setupUi(self, BlogFormCenterContent):
        BlogFormCenterContent.setObjectName("BlogFormCenterContent")
        BlogFormCenterContent.resize(506, 232)
        BlogFormCenterContent.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(BlogFormCenterContent)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.blog_article_label = QtWidgets.QLabel(BlogFormCenterContent)
        self.blog_article_label.setText("")
        self.blog_article_label.setObjectName("blog_article_label")
        self.horizontalLayout_2.addWidget(self.blog_article_label)
        self.blog_stick_label = QtWidgets.QLabel(BlogFormCenterContent)
        self.blog_stick_label.setAlignment(QtCore.Qt.AlignCenter)
        self.blog_stick_label.setObjectName("blog_stick_label")
        self.horizontalLayout_2.addWidget(self.blog_stick_label)
        self.blog_title_button = QtWidgets.QPushButton(BlogFormCenterContent)
        self.blog_title_button.setText("")
        self.blog_title_button.setFlat(True)
        self.blog_title_button.setObjectName("blog_title_button")
        self.horizontalLayout_2.addWidget(self.blog_title_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.blog_content_text = QtWidgets.QTextBrowser(BlogFormCenterContent)
        self.blog_content_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blog_content_text.setObjectName("blog_content_text")
        self.verticalLayout.addWidget(self.blog_content_text)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.blog_time_label = QtWidgets.QLabel(BlogFormCenterContent)
        self.blog_time_label.setText("")
        self.blog_time_label.setObjectName("blog_time_label")
        self.horizontalLayout.addWidget(self.blog_time_label)
        self.blog_classify_button = QtWidgets.QPushButton(BlogFormCenterContent)
        self.blog_classify_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.blog_classify_button.setText("")
        self.blog_classify_button.setFlat(True)
        self.blog_classify_button.setObjectName("blog_classify_button")
        self.horizontalLayout.addWidget(self.blog_classify_button)
        self.blog_comment_button = QtWidgets.QPushButton(BlogFormCenterContent)
        self.blog_comment_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.blog_comment_button.setText("")
        self.blog_comment_button.setFlat(True)
        self.blog_comment_button.setObjectName("blog_comment_button")
        self.horizontalLayout.addWidget(self.blog_comment_button)
        self.blog_views_label = QtWidgets.QLabel(BlogFormCenterContent)
        self.blog_views_label.setText("")
        self.blog_views_label.setObjectName("blog_views_label")
        self.horizontalLayout.addWidget(self.blog_views_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.blog_readmore_button = QtWidgets.QPushButton(BlogFormCenterContent)
        self.blog_readmore_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.blog_readmore_button.setFlat(True)
        self.blog_readmore_button.setObjectName("blog_readmore_button")
        self.horizontalLayout.addWidget(self.blog_readmore_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(BlogFormCenterContent)
        QtCore.QMetaObject.connectSlotsByName(BlogFormCenterContent)

    def retranslateUi(self, BlogFormCenterContent):
        _translate = QtCore.QCoreApplication.translate
        self.blog_stick_label.setText(_translate("BlogFormCenterContent", "置顶"))
        self.blog_readmore_button.setText(_translate("BlogFormCenterContent", "+ 阅读全文"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlogFormCenterContent = QtWidgets.QWidget()
    ui = Ui_BlogFormCenterContent()
    ui.setupUi(BlogFormCenterContent)
    BlogFormCenterContent.show()
    sys.exit(app.exec_())

