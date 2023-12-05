# -*- coding: utf-8 -*-

################################################################################
<<<<<<< Updated upstream
## Form generated from reading UI file 'KookminKioskBiNAZG.ui'
=======
## Form generated from reading UI file 'KookminKioskkcPhVg.ui'
>>>>>>> Stashed changes
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
<<<<<<< Updated upstream
import sys
=======


>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
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
=======
#if QT_CONFIG(tooltip)
        KookminKiosk.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        KookminKiosk.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        KookminKiosk.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        KookminKiosk.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(KookminKiosk)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 601, 801))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.MenuTab = QTabWidget(self.page)
        self.MenuTab.setObjectName(u"MenuTab")
        self.MenuTab.setGeometry(QRect(0, 0, 581, 521))
>>>>>>> Stashed changes
        self.MenuTab.setStyleSheet(u"background-color:rgb(254, 255, 178)")
        self.MenuTab.setIconSize(QSize(20, 20))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
<<<<<<< Updated upstream
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 571, 521))
=======
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 571, 491))
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        self.MenuButton.setMinimumSize(QSize(120, 140))
        font3 = QFont()
        font3.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font3.setPointSize(10)
        self.MenuButton.setFont(font3)
        self.MenuButton.setStyleSheet(u"background-color:white")

        self.MenuGrid.addWidget(self.MenuButton, 0, 0, 1, 1)
=======
        self.MenuButton.setMinimumSize(QSize(120, 120))
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font1.setPointSize(10)
        self.MenuButton.setFont(font1)
        self.MenuButton.setStyleSheet(u"background-color:white")

        self.MenuGrid.addWidget(self.MenuButton, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
>>>>>>> Stashed changes

        self.MenuTab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
<<<<<<< Updated upstream
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 571, 521))
=======
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 571, 491))
>>>>>>> Stashed changes
        self.MenuGrid_2 = QGridLayout(self.gridLayoutWidget_2)
        self.MenuGrid_2.setObjectName(u"MenuGrid_2")
        self.MenuGrid_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.MenuGrid_2.setContentsMargins(0, 0, 0, 0)
        self.MenuButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.MenuButton_2.setObjectName(u"MenuButton_2")
        sizePolicy1.setHeightForWidth(self.MenuButton_2.sizePolicy().hasHeightForWidth())
        self.MenuButton_2.setSizePolicy(sizePolicy1)
        self.MenuButton_2.setMinimumSize(QSize(120, 140))
<<<<<<< Updated upstream
        self.MenuButton_2.setFont(font3)
=======
        self.MenuButton_2.setFont(font1)
>>>>>>> Stashed changes
        self.MenuButton_2.setStyleSheet(u"background-color:white")

        self.MenuGrid_2.addWidget(self.MenuButton_2, 0, 0, 1, 1)

        self.MenuTab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
<<<<<<< Updated upstream
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 571, 521))
=======
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 571, 491))
>>>>>>> Stashed changes
        self.MenuGrid_3 = QGridLayout(self.gridLayoutWidget_3)
        self.MenuGrid_3.setObjectName(u"MenuGrid_3")
        self.MenuGrid_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.MenuGrid_3.setContentsMargins(0, 0, 0, 0)
        self.MenuButton_3 = QPushButton(self.gridLayoutWidget_3)
        self.MenuButton_3.setObjectName(u"MenuButton_3")
        sizePolicy1.setHeightForWidth(self.MenuButton_3.sizePolicy().hasHeightForWidth())
        self.MenuButton_3.setSizePolicy(sizePolicy1)
        self.MenuButton_3.setMinimumSize(QSize(120, 140))
<<<<<<< Updated upstream
        self.MenuButton_3.setFont(font3)
=======
        self.MenuButton_3.setFont(font1)
>>>>>>> Stashed changes
        self.MenuButton_3.setStyleSheet(u"background-color:white")

        self.MenuGrid_3.addWidget(self.MenuButton_3, 0, 0, 1, 1)

        self.MenuTab.addTab(self.tab_3, "")
<<<<<<< Updated upstream
=======
        self.verticalLayoutWidget = QWidget(self.page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(360, 540, 221, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TotalPriceLabel = QLabel(self.verticalLayoutWidget)
        self.TotalPriceLabel.setObjectName(u"TotalPriceLabel")
        self.TotalPriceLabel.setMinimumSize(QSize(0, 0))
        self.TotalPriceLabel.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.TotalPriceLabel.setFont(font2)

        self.verticalLayout.addWidget(self.TotalPriceLabel)

        self.PurchaseButton = QPushButton(self.verticalLayoutWidget)
        self.PurchaseButton.setObjectName(u"PurchaseButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PurchaseButton.sizePolicy().hasHeightForWidth())
        self.PurchaseButton.setSizePolicy(sizePolicy2)
        self.PurchaseButton.setMinimumSize(QSize(150, 0))
        self.PurchaseButton.setMaximumSize(QSize(162, 16777215))
        font3 = QFont()
        font3.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.PurchaseButton.setFont(font3)
#if QT_CONFIG(statustip)
        self.PurchaseButton.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.PurchaseButton.setStyleSheet(u"alignment:Vcenter")
        self.PurchaseButton.setText(u"\uacb0\uc81c\ud558\uae30")

        self.verticalLayout.addWidget(self.PurchaseButton, 0, Qt.AlignHCenter)

        self.ResetShoppingcartButton = QPushButton(self.verticalLayoutWidget)
        self.ResetShoppingcartButton.setObjectName(u"ResetShoppingcartButton")
        self.ResetShoppingcartButton.setMinimumSize(QSize(150, 0))
        self.ResetShoppingcartButton.setFont(font3)

        self.verticalLayout.addWidget(self.ResetShoppingcartButton, 0, Qt.AlignHCenter)

        self.ResetShoppingcartButton_2 = QPushButton(self.verticalLayoutWidget)
        self.ResetShoppingcartButton_2.setObjectName(u"ResetShoppingcartButton_2")
        self.ResetShoppingcartButton_2.setMinimumSize(QSize(150, 0))
        self.ResetShoppingcartButton_2.setFont(font3)

        self.verticalLayout.addWidget(self.ResetShoppingcartButton_2, 0, Qt.AlignHCenter)

        self.tableView = QTableView(self.page)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 540, 341, 251))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayoutWidget_2 = QWidget(self.page_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(90, 20, 411, 601))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(150)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.KioskTitle = QLabel(self.verticalLayoutWidget_2)
        self.KioskTitle.setObjectName(u"KioskTitle")
        font4 = QFont()
        font4.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font4.setPointSize(33)
        font4.setBold(True)
        font4.setWeight(75)
        self.KioskTitle.setFont(font4)
        self.KioskTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.KioskTitle)

        self.StartOrderButton = QPushButton(self.verticalLayoutWidget_2)
        self.StartOrderButton.setObjectName(u"StartOrderButton")
        sizePolicy2.setHeightForWidth(self.StartOrderButton.sizePolicy().hasHeightForWidth())
        self.StartOrderButton.setSizePolicy(sizePolicy2)
        self.StartOrderButton.setMinimumSize(QSize(200, 80))
        self.StartOrderButton.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font5.setPointSize(13)
        self.StartOrderButton.setFont(font5)

        self.verticalLayout_2.addWidget(self.StartOrderButton, 0, Qt.AlignHCenter)

        self.AdminButton = QPushButton(self.page_2)
        self.AdminButton.setObjectName(u"AdminButton")
        self.AdminButton.setGeometry(QRect(480, 750, 93, 28))
        self.stackedWidget.addWidget(self.page_2)
>>>>>>> Stashed changes
        KookminKiosk.setCentralWidget(self.centralwidget)

        self.retranslateUi(KookminKiosk)

<<<<<<< Updated upstream
        self.MenuTab.setCurrentIndex(2)
=======
        self.stackedWidget.setCurrentIndex(1)
        self.MenuTab.setCurrentIndex(0)
>>>>>>> Stashed changes


        QMetaObject.connectSlotsByName(KookminKiosk)
    # setupUi

<<<<<<< Updated upstream
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_KookminKiosk()
    ui.setupUi()
    sys.exit(app.exec_())
=======
    def retranslateUi(self, KookminKiosk):
        KookminKiosk.setWindowTitle(QCoreApplication.translate("KookminKiosk", u"KookminKiosk", None))
        self.MenuButton.setText(QCoreApplication.translate("KookminKiosk", u"TestMenu1 \n"
"\n"
" 2,000\uc6d0", None))
        self.MenuTab.setTabText(self.MenuTab.indexOf(self.tab), QCoreApplication.translate("KookminKiosk", u"\uc74c\uc2dd", None))
        self.MenuButton_2.setText(QCoreApplication.translate("KookminKiosk", u"TestMenu1 \n"
"\n"
" 2,000\uc6d0", None))
        self.MenuTab.setTabText(self.MenuTab.indexOf(self.tab_2), QCoreApplication.translate("KookminKiosk", u"\uc74c\ub8cc", None))
        self.MenuButton_3.setText(QCoreApplication.translate("KookminKiosk", u"TestMenu1 \n"
"\n"
" 2,000\uc6d0", None))
        self.MenuTab.setTabText(self.MenuTab.indexOf(self.tab_3), QCoreApplication.translate("KookminKiosk", u"\uc138\ud2b8", None))
        self.TotalPriceLabel.setText(QCoreApplication.translate("KookminKiosk", u"\ucd1d \uae08\uc561: ", None))
        self.ResetShoppingcartButton.setText(QCoreApplication.translate("KookminKiosk", u"\uc7a5\ubc14\uad6c\ub2c8 \ucd08\uae30\ud654", None))
        self.ResetShoppingcartButton_2.setText(QCoreApplication.translate("KookminKiosk", u"\uc8fc\ubb38 \ucde8\uc18c", None))
        self.KioskTitle.setText(QCoreApplication.translate("KookminKiosk", u"Kookmin Kiosk", None))
        self.StartOrderButton.setText(QCoreApplication.translate("KookminKiosk", u"\uc8fc\ubb38 \uc2dc\uc791\ud558\uae30", None))
        self.AdminButton.setText(QCoreApplication.translate("KookminKiosk", u"\uad00\ub9ac\uc790 \ub3c4\uad6c", None))
    # retranslateUi

>>>>>>> Stashed changes
