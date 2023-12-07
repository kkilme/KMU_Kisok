# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enternumsCjGFt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EnterNum(object):
    def setupUi(self, EnterNum):
        if not EnterNum.objectName():
            EnterNum.setObjectName(u"EnterNum")
        EnterNum.resize(435, 141)
        font = QFont()
        font.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        EnterNum.setFont(font)
        self.desc = QLabel(EnterNum)
        self.desc.setObjectName(u"desc")
        self.desc.setGeometry(QRect(20, 10, 281, 51))
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font1.setPointSize(14)
        self.desc.setFont(font1)
        self.horizontalLayoutWidget = QWidget(EnterNum)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 80, 401, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Cancel = QPushButton(self.horizontalLayoutWidget)
        self.Cancel.setObjectName(u"Cancel")
        self.Cancel.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.Cancel)

        self.OK = QPushButton(self.horizontalLayoutWidget)
        self.OK.setObjectName(u"OK")
        self.OK.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.OK)

        self.num = QLineEdit(EnterNum)
        self.num.setObjectName(u"num")
        self.num.setGeometry(QRect(310, 20, 111, 31))
        self.num.setAlignment(Qt.AlignCenter)

        self.retranslateUi(EnterNum)

        QMetaObject.connectSlotsByName(EnterNum)
    # setupUi

    def retranslateUi(self, EnterNum):
        EnterNum.setWindowTitle(QCoreApplication.translate("EnterNum", u"\uc218\ub7c9\uc744 \uc785\ub825\ud558\uc138\uc694", None))
        self.desc.setText(QCoreApplication.translate("EnterNum", u"\uc218\ub7c9\uc744 \uc785\ub825\ud558\uc138\uc694 (\ucd5c\ub300 10): ", None))
        self.Cancel.setText(QCoreApplication.translate("EnterNum", u"\ucde8\uc18c", None))
        self.OK.setText(QCoreApplication.translate("EnterNum", u"\ud655\uc778", None))
        self.num.setPlaceholderText(QCoreApplication.translate("EnterNum", u"1", None))
    # retranslateUi

