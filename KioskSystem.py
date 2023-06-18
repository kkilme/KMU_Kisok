from UIManager import UIManager

class KioskSystem():
    def __init__(self) -> None:
        self.UIManager = UIManager.instance()

    def StartKioskSystem(self):
        self.UIManager.MainScreen()

    def EndKioskSystem(self):
        exit()



if __name__ == '__main__':
    kiosk = KioskSystem()
    kiosk.StartKioskSystem()
    kiosk.EndKioskSystem()