from MenuManager import MenuManager
from AdminUI import AdminUI
from AdminPresenter import AdminPresenter
from MenuButton import MenuButton

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
        
    def loadMenu(self):
        menulist = self.MenuManager.getMenuList()
        x = 0; y = 0;
        for menu in menulist:
            if str(getattr(menu, "menutype")) == "Menutype.Food":
                button = MenuButton(f'{menu.name}\n\n₩{menu.price}')
                self.ui.replaceWidget(self.ui.FoodGrid, button, y, x)
            elif str(getattr(menu, "menutype")) == "Menutype.Drink":
                button = MenuButton(f'{menu.name}\n\n₩{menu.price}')
                self.ui.replaceWidget(self.ui.DrinkGrid, button, y, x)
            elif str(getattr(menu, "menutype")) == "Menutype.Set":
                button = MenuButton(f'{menu.name}\n\n₩{menu.price}')
                self.ui.replaceWidget(self.ui.SetGrid, button, y, x)
            y = y + 1 if x == self.ui.menugridSize - 1 else y
            x = x + 1 if x < 4 else 0
        