from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from KioskPresenter import KioskPresenter
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

        self.startOrderButton = QPushButton("주문 시작", mainWidget)
        self.startOrderButton.setGeometry(QRect(170, 490, 260, 90))
        startOrderFont = QFont()
        startOrderFont.setPointSize(13)
        self.startOrderButton.setFont(startOrderFont)
        
        self.adminUIButton = QPushButton("관리자 도구", mainWidget)
        self.adminUIButton.setGeometry(QRect(450, 750, 130, 30))
        self.adminUIButton.clicked.connect(self.presenter.openAdminWindow)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = KioskUI()
    mywindow.show()
    app.exec_()