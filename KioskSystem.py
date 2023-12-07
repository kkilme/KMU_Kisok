from PySide2.QtWidgets import QApplication
import sys
from KioskUI import KioskUI
from KioskPresenter import KioskPresenter

class KioskSystem():
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.KioskUI = KioskUI()
        self.KioskPresenter = KioskPresenter(self.KioskUI)
        self.KioskUI.assignPresenter(self.KioskPresenter)
        self.KioskUI.initStartUI()

    def StartKioskSystem(self):
        self.KioskUI.show()
        sys.exit(self.app.exec_())

# ₩
if __name__ == '__main__':
    kiosk = KioskSystem()
    kiosk.StartKioskSystem()