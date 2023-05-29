from UIManager import UIManager
from Singleton import SingletonInstance

class KioskSystem(SingletonInstance):
    def __init__(self) -> None:
        self.UIManager = UIManager.instance()

    def StartKioskSystem(self):
        self.UIManager.MainScreen()

    def EndKioskSystem():
        exit()



if __name__ == '__main__':
    kiosk = KioskSystem.instance()
    kiosk.StartKioskSystem()