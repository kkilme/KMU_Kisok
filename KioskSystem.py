from UIManager import UIManager
from Singleton import SingletonInstance

class KioskSystem(SingletonInstance):
    def __init__(self) -> None:
        self.UIManager = UIManager()
        pass

    def StartKioskSystem(self):
        UIManager.MainScreen()
        pass

    def EndKioskSystem():
        pass

    def DisplayMenuScreen():
        pass

    def EnterMenuScreen():
        pass


if __name__ == '__main__':
    kiosk = KioskSystem.instance()
    kiosk.StartKioskSystem()