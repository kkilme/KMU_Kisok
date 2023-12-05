# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KookminKioskBiNAZG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
class Ui_KookminKiosk(object):
    def setupUi(self, KookminKiosk):
        if not KookminKiosk.objectName():
            KookminKiosk.setObjectName(u"KookminKiosk")
        KookminKiosk.resize(600, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(KookminKiosk.sizePolicy().hasHeightForWidth())
        KookminKiosk.setSizePolicy(sizePolicy)
        KookminKiosk.setMinimumSize(QSize(600, 800))
        KookminKiosk.setMaximumSize(QSize(600, 800))
        font = QFont()
        font.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        KookminKiosk.setFont(font)
        self.centralwidget = QWidget(KookminKiosk)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.ShoppingCartTable = QTableView(self.centralwidget)
        self.ShoppingCartTable.setObjectName(u"ShoppingCartTable")
        self.ShoppingCartTable.setGeometry(QRect(10, 570, 351, 221))
        self.ShoppingCartTable.setFont(font)
        self.PurchaseButton = QPushButton(self.centralwidget)
        self.PurchaseButton.setObjectName(u"PurchaseButton")
        self.PurchaseButton.setGeometry(QRect(400, 640, 160, 60))
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.PurchaseButton.setFont(font1)
        self.TotalPriceLabel = QLabel(self.centralwidget)
        self.TotalPriceLabel.setObjectName(u"TotalPriceLabel")
        self.TotalPriceLabel.setGeometry(QRect(380, 580, 191, 51))
        font2 = QFont()
        font2.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.TotalPriceLabel.setFont(font2)
        self.ResetShoppingcartButton = QPushButton(self.centralwidget)
        self.ResetShoppingcartButton.setObjectName(u"ResetShoppingcartButton")
        self.ResetShoppingcartButton.setGeometry(QRect(400, 720, 160, 60))
        self.ResetShoppingcartButton.setFont(font1)
        self.MenuTab = QTabWidget(self.centralwidget)
        self.MenuTab.setObjectName(u"MenuTab")
        self.MenuTab.setGeometry(QRect(10, 10, 581, 551))
        self.MenuTab.setStyleSheet(u"background-color:rgb(254, 255, 178)")
        self.MenuTab.setIconSize(QSize(20, 20))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 571, 521))
        self.MenuGrid = QGridLayout(self.gridLayoutWidget)
        self.MenuGrid.setObjectName(u"MenuGrid")
        self.MenuGrid.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.MenuGrid.setContentsMargins(0, 0, 0, 0)
        self.MenuButton = QPushButton(self.gridLayoutWidget)
        self.MenuButton.setObjectName(u"MenuButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MenuButton.sizePolicy().hasHeightForWidth())
        self.MenuButton.setSizePolicy(sizePolicy1)
        self.MenuButton.setMinimumSize(QSize(120, 140))
        font3 = QFont()
        font3.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font3.setPointSize(10)
        self.MenuButton.setFont(font3)
        self.MenuButton.setStyleSheet(u"background-color:white")

        self.MenuGrid.addWidget(self.MenuButton, 0, 0, 1, 1)

        self.MenuTab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 571, 521))
        self.MenuGrid_2 = QGridLayout(self.gridLayoutWidget_2)
        self.MenuGrid_2.setObjectName(u"MenuGrid_2")
        self.MenuGrid_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.MenuGrid_2.setContentsMargins(0, 0, 0, 0)
        self.MenuButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.MenuButton_2.setObjectName(u"MenuButton_2")
        sizePolicy1.setHeightForWidth(self.MenuButton_2.sizePolicy().hasHeightForWidth())
        self.MenuButton_2.setSizePolicy(sizePolicy1)
        self.MenuButton_2.setMinimumSize(QSize(120, 140))
        self.MenuButton_2.setFont(font3)
        self.MenuButton_2.setStyleSheet(u"background-color:white")

        self.MenuGrid_2.addWidget(self.MenuButton_2, 0, 0, 1, 1)

        self.MenuTab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 571, 521))
        self.MenuGrid_3 = QGridLayout(self.gridLayoutWidget_3)
        self.MenuGrid_3.setObjectName(u"MenuGrid_3")
        self.MenuGrid_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.MenuGrid_3.setContentsMargins(0, 0, 0, 0)
        self.MenuButton_3 = QPushButton(self.gridLayoutWidget_3)
        self.MenuButton_3.setObjectName(u"MenuButton_3")
        sizePolicy1.setHeightForWidth(self.MenuButton_3.sizePolicy().hasHeightForWidth())
        self.MenuButton_3.setSizePolicy(sizePolicy1)
        self.MenuButton_3.setMinimumSize(QSize(120, 140))
        self.MenuButton_3.setFont(font3)
        self.MenuButton_3.setStyleSheet(u"background-color:white")

        self.MenuGrid_3.addWidget(self.MenuButton_3, 0, 0, 1, 1)

        self.MenuTab.addTab(self.tab_3, "")
        KookminKiosk.setCentralWidget(self.centralwidget)

        self.retranslateUi(KookminKiosk)

        self.MenuTab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(KookminKiosk)
    # setupUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_KookminKiosk()
    ui.setupUi()
    sys.exit(app.exec_())