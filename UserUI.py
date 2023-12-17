from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from UserPresenter import UserPresenter
from UITemplate import UITemplate

class UserUI(UITemplate):
    def __init__(self) -> None:
        super(UserUI, self).__init__()
        self.menugridSize = 4
    
    def initUI(self):
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
        self.MenuTab.setGeometry(QRect(20, 10, 560, 510))
        self.MenuTab.setStyleSheet(u"background-color:rgb(254, 255, 178)")
        
        self.foodmenutab = QWidget()
        self.foodgridLayoutWidget = QWidget(self.foodmenutab)
        self.foodgridLayoutWidget.setGeometry(QRect(0, 0, 550, 480))
        self.FoodGrid = QGridLayout(self.foodgridLayoutWidget)

        # self.testbutton = OrderMenuButton("test1\n\n2,000", self.foodgridLayoutWidget)
        # self.replaceDummyWidget(self.FoodGrid, self.testbutton, 0, 1)
        # self.testbutton2 = OrderMenuButton("test1\n\n2,000", self.foodgridLayoutWidget)
        # self.replaceDummyWidget(self.FoodGrid, self.testbutton2, 0, 0)
        # self.MenuGrid.addWidget(self.testbutton, 0,0,1,1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.MenuTab.addTab(self.foodmenutab, "Food")
        
        self.drinkmenutab = QWidget()
        self.foodgridLayoutWidget2 = QWidget(self.drinkmenutab)
        self.foodgridLayoutWidget2.setGeometry(QRect(0, 0, 550, 480))
        self.DrinkGrid = QGridLayout(self.foodgridLayoutWidget2)

        self.MenuTab.addTab(self.drinkmenutab, "Drink")
        
        self.setmenutab = QWidget()
        self.foodgridLayoutWidget3 = QWidget(self.setmenutab)
        self.foodgridLayoutWidget3.setGeometry(QRect(0, 0, 550, 480))
        self.SetGrid = QGridLayout(self.foodgridLayoutWidget3)

        self.MenuTab.addTab(self.setmenutab, "Set")
        
        # Total Price ============================================
        
        self.orderverticalLayoutWidget = QWidget(self.orderpage)
        self.orderverticalLayoutWidget.setGeometry(QRect(360, 540, 220, 250))
        self.orderverticalLayout = QVBoxLayout(self.orderverticalLayoutWidget)

        self.totalPriceLabel = QLabel("총 가격: 0 ₩", self.orderverticalLayoutWidget)
        self.totalPriceLabel.setMaximumSize(QSize(16777215, 50))
        totalpricefont = QFont()
        totalpricefont.setPointSize(14)
        self.totalPriceLabel.setFont(totalpricefont)

        self.orderverticalLayout.addWidget(self.totalPriceLabel)
        
        # Order Buttons ===========================================
        orderbuttonfont = QFont()
        orderbuttonfont.setPointSize(12)
        orderbuttonfont.setBold(True)
        orderbuttonfont.setWeight(75)
        
        self.PurchaseButton = QPushButton("결제하기", self.orderverticalLayoutWidget)
        self.PurchaseButton.setMinimumSize(QSize(150, 0))
        self.PurchaseButton.setMaximumSize(QSize(162, 16777215))
        self.PurchaseButton.setFont(orderbuttonfont)
        self.PurchaseButton.clicked.connect(self.presenter.processOrder)
        
        self.clearCartButton = QPushButton("장바구니 초기화", self.orderverticalLayoutWidget)
        self.clearCartButton.setMinimumSize(QSize(150, 0))
        self.clearCartButton.setMaximumSize(QSize(162, 16777215))
        self.clearCartButton.setFont(orderbuttonfont)
        
        self.CancleOrderButton = QPushButton("주문 취소", self.orderverticalLayoutWidget)
        self.CancleOrderButton.setMinimumSize(QSize(150, 0))
        self.CancleOrderButton.setMaximumSize(QSize(162, 16777215))
        self.CancleOrderButton.setFont(orderbuttonfont)
        self.CancleOrderButton.clicked.connect(self.changeUI)
        
        self.orderverticalLayout.addWidget(self.PurchaseButton, 0, Qt.AlignHCenter)
        self.orderverticalLayout.addWidget(self.clearCartButton, 0, Qt.AlignHCenter)
        self.orderverticalLayout.addWidget(self.CancleOrderButton, 0, Qt.AlignHCenter)
        
        # Cart table =====================================
        self.cartlabel = QLabel("장바구니", self.orderpage)
        self.cartlabel.setGeometry(QRect(90, 530, 190, 40))
        font4 = QFont()
        font4.setPointSize(17)
        font4.setBold(True)
        font4.setWeight(75)
        self.cartlabel.setFont(font4)
        self.cartlabel.setAlignment(Qt.AlignCenter)
        
        self.cartTable = QTableWidget(self.orderpage)
        self.cartTable.setGeometry(QRect(10, 580, 340, 210))
        self.cartTable.setColumnCount(5)
        self.cartTable.setRowCount(0)
        self.cartTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cartTable.setColumnWidth(0, 98)
        self.cartTable.setColumnWidth(1, 90)
        self.cartTable.setColumnWidth(2, 60)
        self.cartTable.setColumnWidth(3, 45)
        self.cartTable.setColumnWidth(4, 45)
        self.cartTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.cartTable.verticalHeader().setVisible(False)
        self.cartTable.setHorizontalHeaderLabels(["메뉴명", "가격", "수량", "-", "+"])
        
        self.clearCartButton.clicked.connect(lambda: self.presenter.clearCart())
        # ======================================
        self.stackedWidget.addWidget(self.orderpage)
        
        self.stackedWidget.setCurrentIndex(0)
        self.MenuTab.setCurrentIndex(0)
        
        # ============================
        self.presenter.loadMenu()
        self.move(400, 200)

    # 더미 위젯으로 그리드 채움
    def fillDummyWidgetOnGrid(self):
        def fill(grid):
            for row in range(self.menugridSize):
                for col in range(self.menugridSize):
                    dummy = DummyWidget(self)
                    grid.addWidget(dummy, row, col)
        fill(self.FoodGrid)
        fill(self.DrinkGrid)
        fill(self.SetGrid)

    # 그리드에서 위젯을 없애고 해당 자리에 다른 위젯 삽입    
    def replaceWidget(self, grid:QGridLayout, newwidget:QPushButton, y, x):
        oldwidget = grid.itemAtPosition(x, y).widget()
        grid.removeWidget(oldwidget)
        oldwidget.deleteLater()  # 위젯 삭제
        grid.addWidget(newwidget, x, y)
        
    def changeUI(self):
        if self.stackedWidget.currentIndex() == 0:
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.presenter.clearCart()
            self.MenuTab.setCurrentIndex(0)
            self.stackedWidget.setCurrentIndex(0)

    # 테이블에서 특정 스트링이 들어간 행의 번호를 찾음. 없으면 -1 리턴
    # 메뉴 이름으로 찾기때문에 column은 0번 고정
    def findRowinCart(self, string):
        table = self.cartTable
        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if item and string == item.text():
                return row
        return -1
    
    # gridlayout의 모든 위젯을 제거
    def clearGridLayout(self):
        def clear(grid):
            for i in reversed(range(grid.count())):
                item = grid.takeAt(i)
                if item.widget():
                    item.widget().deleteLater()  # 위젯 삭제
        clear(self.FoodGrid)
        clear(self.DrinkGrid)
        clear(self.SetGrid)
            
class DummyWidget(QWidget):
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = UserUI()
    mywindow.show()
    app.exec_()