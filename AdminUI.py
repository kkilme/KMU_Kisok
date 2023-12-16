from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class AdminUI(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.presenter = None

    def assignPresenter(self, presenter):
        self.presenter = presenter

    def initUI(self):
        self.setFixedSize(700, 300)
        self.setWindowTitle("Admin Helper")
        mainfont = QFont()
        mainfont.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515") # nanum godic
        mainWidget = QWidget(self)
        mainWidget.setFont(mainfont)
        self.setCentralWidget(mainWidget)
        
        # ===============================
        
        self.stackedWidget = QStackedWidget(mainWidget)
        self.stackedWidget.setGeometry(QRect(-1, -1, 700, 300))
        
        # 비밀번호 입력 페이지 ===============================
        
        self.page = QWidget()
        
        self.enterpassword = QLabel("비밀번호를 입력하세요: ", self.page)
        self.enterpassword.setGeometry(QRect(130, 130, 231, 31))
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font1.setPointSize(13)
        self.enterpassword.setFont(font1)
        
        self.passwordlineedit = QLineEdit(self.page)
        self.passwordlineedit.setGeometry(QRect(360, 130, 131, 31))
        self.passwordlineedit.setEchoMode(QLineEdit.Password)
        self.passwordlineedit.returnPressed.connect(lambda: self.presenter.authenticate(self.passwordlineedit.text()))
        
        self.passwordconfirm = QPushButton("확인", self.page)
        self.passwordconfirm.setGeometry(QRect(510, 130, 93, 31))
        self.passwordconfirm.clicked.connect(lambda: self.presenter.authenticate(self.passwordlineedit.text()))
        
        self.wrongpasswordlabel = QLabel("",self.page)
        self.wrongpasswordlabel.setGeometry(QRect(260, 170, 211, 41))
        font2 = QFont()
        font2.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font2.setPointSize(10)
        self.wrongpasswordlabel.setFont(font2)
        self.wrongpasswordlabel.setStyleSheet(u"color:red")
        self.wrongpasswordlabel.setAlignment(Qt.AlignCenter)
        
        self.stackedWidget.addWidget(self.page)
        
        # 메인화면 ================================
        
        self.page_2 = QWidget()
        
        self.orderqueuetable = QTableWidget(self.page_2)
        self.orderqueuetable.setGeometry(QRect(40, 70, 411, 211))
        self.orderqueuetable.setColumnCount(4)
        self.orderqueuetable.setRowCount(0)
        self.orderqueuetable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.orderqueuetable.setColumnWidth(0, 40)
        self.orderqueuetable.setColumnWidth(1, 200)
        self.orderqueuetable.setColumnWidth(2, 123)
        self.orderqueuetable.setColumnWidth(3, 39)
        self.orderqueuetable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.orderqueuetable.verticalHeader().setVisible(False)
        self.orderqueuetable.setHorizontalHeaderLabels(["#", "주문내역", "가격", "제거"])
        
        self.label_2 = QLabel("대기중인 주문", self.page_2)
        self.label_2.setGeometry(QRect(140, 30, 211, 31))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        
        self.label_3 = QLabel("관리자 도구", self.page_2)
        self.label_3.setGeometry(QRect(470, 70, 211, 61))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.statisticsbutton = QPushButton("통계 확인", self.page_2)
        self.statisticsbutton.setGeometry(QRect(520, 140, 121, 31))
        self.statisticsbutton.clicked.connect(lambda: self.changeUI(2))
        self.managemenubutton = QPushButton("메뉴 관리",self.page_2)
        self.managemenubutton.setGeometry(QRect(520, 210, 121, 31))
        self.managemenubutton.clicked.connect(lambda: self.changeUI(3))
        
        self.stackedWidget.addWidget(self.page_2)
        
        # 통계 확인 ================================
        
        self.page_3 = QWidget()
        
        self.label_5 = QLabel("통계 확인", self.page_3)
        self.label_5.setGeometry(QRect(0, 10, 701, 51))
        font2 = QFont()
        font2.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font2.setPointSize(19)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        
        self.dailyincomebutton = QPushButton("일별 매출 확인", self.page_3)
        self.dailyincomebutton.setGeometry(QRect(170, 120, 131, 91))
        self.incomepermenubutton = QPushButton("메뉴별 매출 확인", self.page_3)
        self.incomepermenubutton.setGeometry(QRect(410, 120, 131, 91))
        self.backbutton = QPushButton("돌아가기", self.page_3)
        self.backbutton.setGeometry(QRect(310, 240, 93, 28))
        self.backbutton.clicked.connect(lambda: self.changeUI(1))
        
        self.stackedWidget.addWidget(self.page_3)
        
        # 메뉴 관리 ================================
        
        self.page_4 = QWidget()

        self.label_4 = QLabel("메뉴 관리", self.page_4)
        self.label_4.setGeometry(QRect(0, 10, 701, 41))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.curmenutable = QTableWidget(self.page_4)
        self.curmenutable.setGeometry(QRect(90, 60, 531, 161))
        self.curmenutable.setColumnCount(6)
        self.curmenutable.setRowCount(0)
        self.curmenutable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.curmenutable.setColumnWidth(0, 45)
        self.curmenutable.setColumnWidth(1, 150)
        self.curmenutable.setColumnWidth(2, 105)
        self.curmenutable.setColumnWidth(3, 103)
        self.curmenutable.setColumnWidth(4, 50)
        self.curmenutable.setColumnWidth(5, 50)
        self.curmenutable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.curmenutable.verticalHeader().setVisible(False)
        self.curmenutable.setHorizontalHeaderLabels(["id", "메뉴명", "가격", "메뉴 타입", "수정", "삭제"])
        
        self.addmenubutton = QPushButton("메뉴 추가", self.page_4)
        self.addmenubutton.clicked.connect(lambda: self.presenter.createMenu())
        self.addmenubutton.setGeometry(QRect(250, 240, 93, 28))
        self.backbutton2 = QPushButton("돌아가기", self.page_4)
        self.backbutton2.setGeometry(QRect(380, 240, 93, 28))
        self.backbutton2.clicked.connect(lambda: self.changeUI(1))
        
        self.stackedWidget.addWidget(self.page_4)
        self.move(1200, 400)
    def changeUI(self, idx):
        self.stackedWidget.setCurrentIndex(idx)