from PySide2.QtWidgets import QApplication
import sys
from UserUI import UserUI
from UserPresenter import UserPresenter

class KioskSystem():
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.UserUI = UserUI()
        self.UserPresenter = UserPresenter(self.UserUI)
        self.UserUI.assignPresenter(self.UserPresenter)
        self.UserUI.initUI()

    def StartKioskSystem(self):
        self.UserUI.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    kiosk = KioskSystem()
    kiosk.StartKioskSystem()