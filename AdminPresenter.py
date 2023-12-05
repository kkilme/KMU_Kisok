from MenuManager import MenuManager
from StatisticsManager import StatisticsManager
from AdminManager import AdminManager

class AdminPresenter():
    def __init__(self, ui) -> None:
        self.ui = ui
        self.MenuManager = MenuManager.instance()
        self.StatisticsManager = StatisticsManager.instance()
        self.AdminManager = AdminManager.instance()