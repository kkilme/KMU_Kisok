from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from AdminPresenter import AdminPresenter
class AdminUI(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.presenter = None

    def assignPresenter(self, presenter: AdminPresenter):
        self.presenter = presenter
    
    def initUI(self):
        ...

    def initStartUI(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("Kiosk Manager")
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        mainfont = QFont()
        mainfont.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515") # nanum godic
        self.setFont(mainfont)

        self.label = QLabel("Kookmin Kiosk", mainWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 530, 240))
        kioskTitleFont = QFont()
        kioskTitleFont.setPointSize(35)
        kioskTitleFont.setBold(True)
        kioskTitleFont.setWeight(75)
        self.label.setFont(kioskTitleFont)
        self.label.setAlignment(Qt.AlignCenter)