# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'numticketQIkWWx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(479, 577)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 100, 479, 150))
        self.label_2.setMaximumSize(QSize(16777215, 150))
        font = QFont()
        font.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font.setPointSize(52)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 30, 479, 45))
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(19)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 250, 481, 51))
        self.label_3.setMaximumSize(QSize(16777215, 100))
        font2 = QFont()
        font2.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font2.setPointSize(16)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 310, 381, 201))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 520, 171, 31))
        font3 = QFont()
        font3.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font3.setPointSize(12)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Order Complete", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\uc8fc\ubb38\uc774 \uc644\ub8cc\ub418\uc5c8\uc2b5\ub2c8\ub2e4.", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\uc8fc\ubb38 \ub0b4\uc5ed", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\ucd1d \uac00\uaca9: 10000", None))
    # retranslateUi

