from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from KioskPresenter import KioskPresenter
from OrderMenuButton import OrderMenuButton

class KioskUI(QMainWindow):
    def __init__(self) -> None:
        super(KioskUI, self).__init__()
        self.presenter = None
    
    def assignPresenter(self, presenter: KioskPresenter):
        self.presenter = presenter

    def initOrderUI(self):
        ...

    def initStartUI(self):
        self.setFixedSize(600, 800)
        self.setWindowTitle("Kookmin Kiosk")
        mainfont = QFont()
        mainfont.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515") # nanum godic
        self.setFont(mainfont)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        
        # ===============================
        
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QRect(0, 0, 600, 800))
                
        # Start UI ======================================
        
        self.mainpage = QWidget()
        
        self.mainVerticalLayoutWidget = QWidget(self.mainpage)
        self.mainVerticalLayoutWidget.setGeometry(QRect(90, 20, 410, 600))
        
        self.mainVerticalLayout = QVBoxLayout(self.mainVerticalLayoutWidget)
        self.mainVerticalLayout.setSpacing(150)
        
        self.KioskTitle = QLabel("Kookmin Kiosk", self.mainVerticalLayoutWidget)
        kioskTitleFont = QFont()
        kioskTitleFont.setPointSize(35)
        kioskTitleFont.setBold(True)
        kioskTitleFont.setWeight(75)
        self.KioskTitle.setFont(kioskTitleFont)
        self.KioskTitle.setAlignment(Qt.AlignCenter)

        self.mainVerticalLayout.addWidget(self.KioskTitle)
        
        self.startOrderButton = QPushButton("주문 시작", self.mainVerticalLayoutWidget)
        self.startOrderButton.setMinimumSize(QSize(200, 80))
        startOrderFont = QFont()
        startOrderFont.setPointSize(13)
        self.startOrderButton.setFont(startOrderFont)
        self.startOrderButton.clicked.connect(self.changeUI)
        
        self.mainVerticalLayout.addWidget(self.startOrderButton, 0, Qt.AlignHCenter)
        
        self.adminUIButton = QPushButton("관리자 도구", self.mainpage)
        self.adminUIButton.setGeometry(QRect(450, 750, 130, 30))
        self.adminUIButton.clicked.connect(self.presenter.openAdminWindow)
        
        self.stackedWidget.addWidget(self.mainpage)
        
        # Menu Grid+Tab Layout============================================
        
        self.orderpage = QWidget()
        
        self.MenuTab = QTabWidget(self.orderpage)
        self.MenuTab.setGeometry(QRect(0, 0, 580, 520))
        self.MenuTab.setStyleSheet(u"background-color:rgb(254, 255, 178)")
        
        self.foodmenutab = QWidget()
        self.foodgridLayoutWidget = QWidget(self.foodmenutab)
        self.foodgridLayoutWidget.setGeometry(QRect(0, 0, 570, 490))
        self.MenuGrid = QGridLayout(self.foodgridLayoutWidget)

        self.testbutton = OrderMenuButton("test1\n\n2,000", self.foodgridLayoutWidget)
        
        self.MenuGrid.addWidget(self.testbutton, 0,0,1,1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.MenuTab.addTab(self.foodmenutab, "Food")
        
        self.drinkmenutab = QWidget()
        self.foodgridLayoutWidget2 = QWidget(self.drinkmenutab)
        self.foodgridLayoutWidget2.setGeometry(QRect(0, 0, 570, 490))
        self.MenuGrid2 = QGridLayout(self.foodgridLayoutWidget2)

        self.MenuTab.addTab(self.drinkmenutab, "Drink")
        
        self.setmenutab = QWidget()
        self.foodgridLayoutWidget3 = QWidget(self.setmenutab)
        self.foodgridLayoutWidget3.setGeometry(QRect(0, 0, 570, 490))
        self.MenuGrid3 = QGridLayout(self.foodgridLayoutWidget3)

        self.MenuTab.addTab(self.setmenutab, "Set")
        
        # Total Price ============================================
        
        self.orderverticalLayoutWidget = QWidget(self.orderpage)
        self.orderverticalLayoutWidget.setGeometry(QRect(360, 540, 220, 250))
        self.orderverticalLayout = QVBoxLayout(self.orderverticalLayoutWidget)

        self.TotalPriceLabel = QLabel("총 가격: ", self.orderverticalLayoutWidget)
        self.TotalPriceLabel.setMaximumSize(QSize(16777215, 50))
        totalpricefont = QFont()
        totalpricefont.setPointSize(14)
        self.TotalPriceLabel.setFont(totalpricefont)

        self.orderverticalLayout.addWidget(self.TotalPriceLabel)
        
        # Order Buttons ===========================================
        orderbuttonfont = QFont()
        orderbuttonfont.setPointSize(12)
        orderbuttonfont.setBold(True)
        orderbuttonfont.setWeight(75)
        
        self.PurchaseButton = QPushButton("결제하기", self.orderverticalLayoutWidget)
        self.PurchaseButton.setMinimumSize(QSize(150, 0))
        self.PurchaseButton.setMaximumSize(QSize(162, 16777215))
        self.PurchaseButton.setFont(orderbuttonfont)
        
        self.ResetShoppingcartButton = QPushButton("장바구니 초기화", self.orderverticalLayoutWidget)
        self.ResetShoppingcartButton.setMinimumSize(QSize(150, 0))
        self.ResetShoppingcartButton.setMaximumSize(QSize(162, 16777215))
        self.ResetShoppingcartButton.setFont(orderbuttonfont)
        
        self.CancleOrderButton = QPushButton("주문 취소", self.orderverticalLayoutWidget)
        self.CancleOrderButton.setMinimumSize(QSize(150, 0))
        self.CancleOrderButton.setMaximumSize(QSize(162, 16777215))
        self.CancleOrderButton.setFont(orderbuttonfont)
        self.CancleOrderButton.clicked.connect(self.changeUI)
        
        self.orderverticalLayout.addWidget(self.PurchaseButton, 0, Qt.AlignHCenter)
        self.orderverticalLayout.addWidget(self.ResetShoppingcartButton, 0, Qt.AlignHCenter)
        self.orderverticalLayout.addWidget(self.CancleOrderButton, 0, Qt.AlignHCenter)
        
        # Cart table =====================================
        self.tableView = QTableView(self.orderpage)
        self.tableView.setGeometry(QRect(10, 540, 340, 250))
        # ======================================
        self.stackedWidget.addWidget(self.orderpage)
        
        self.stackedWidget.setCurrentIndex(0)
        self.MenuTab.setCurrentIndex(0)
        
    def changeUI(self):
        if self.stackedWidget.currentIndex() == 0:
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = KioskUI()
    mywindow.show()
    app.exec_()