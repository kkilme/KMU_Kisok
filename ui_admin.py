# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminOtRQUy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        self.centralwidget.setFont(font)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 700, 300))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 130, 231, 31))
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font1.setPointSize(13)
        self.label.setFont(font1)
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(360, 130, 131, 31))
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(510, 130, 93, 31))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.tableWidget = QTableWidget(self.page_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 70, 411, 211))
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 30, 211, 31))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(520, 140, 121, 31))
        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(520, 210, 121, 31))
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(470, 70, 211, 61))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 10, 701, 51))
        font2 = QFont()
        font2.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font2.setPointSize(19)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.pushButton_6 = QPushButton(self.page_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(170, 120, 131, 91))
        self.pushButton_7 = QPushButton(self.page_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(410, 120, 131, 91))
        self.pushButton_8 = QPushButton(self.page_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(310, 240, 93, 28))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 701, 41))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.tableWidget_2 = QTableWidget(self.page_4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(90, 60, 531, 161))
        self.pushButton_4 = QPushButton(self.page_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(250, 240, 93, 28))
        self.pushButton_5 = QPushButton(self.page_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(380, 240, 93, 28))
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AdminHelper", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638\ub97c \uc785\ub825\ud558\uc138\uc694:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ub300\uae30\uc911\uc778 \uc8fc\ubb38", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uba54\ub274 \uad00\ub9ac", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\ud1b5\uacc4 \ud655\uc778", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uad00\ub9ac\uc790 \ub3c4\uad6c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\ud1b5\uacc4 \ud655\uc778", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\uc77c\ubcc4 \ub9e4\ucd9c \ud655\uc778", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\uba54\ub274\ubcc4 \ub9e4\ucd9c \ud655\uc778", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\ub3cc\uc544\uac00\uae30", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uba54\ub274 \uad00\ub9ac", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\uba54\ub274 \ucd94\uac00", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\ub3cc\uc544\uac00\uae30", None))
    # retranslateUi

