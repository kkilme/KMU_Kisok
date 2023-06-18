from Menu import DrinkMenu, FoodMenu

class MenuFactory():
    def CreateMenu(name, id, price, desc, menutype):
        if menutype == 'Drink':
            return DrinkMenu(name, id, price, desc)
        elif menutype == 'Food':
            return FoodMenu(name, id, price, desc)
