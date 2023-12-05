from MenuManager import MenuManager
from AdminUI import AdminUI
from AdminPresenter import AdminPresenter

class KioskPresenter():
    def __init__(self, ui) -> None:
        self.ui = ui
        self.MenuManager = MenuManager.instance()

    def openAdminWindow(self):
        adminUI = AdminUI()
        adminPresenter = AdminPresenter(adminUI)
        adminUI.assignPresenter(adminPresenter)
        adminUI.initStartUI()
        adminUI.show()