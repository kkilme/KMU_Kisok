from abc import ABCMeta,abstractmethod

class Menu(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, id, price, desc) -> None:
        self.name = name
        self.id = id
        self.price = price
        self.description = desc

    def UpdateMenu(self, name, price, desc, menutype):
        if name!='': self.name = name
        if price!='': self.price = price
        if desc!='': self.description = desc
        if menutype!='': self.menutype = menutype
    
    def __hash__(self): # 딕셔너리 키로 Menu객체를 사용하기 위해 구현
        return hash(self.name)

    def __eq__(self, other): # 딕셔너리 키로 Menu객체를 사용하기 위해 구현
        return isinstance(other, Menu) and self.name == other.name
    
class DrinkMenu(Menu):
    def __init__(self, name, id, price, desc) -> None:
        super().__init__(name, id, price, desc) 
        self.menutype = 'Drink'

class FoodMenu(Menu):
    def __init__(self, name, id, price, desc) -> None:
        super().__init__(name, id, price, desc)
        self.menutype = 'Food'       