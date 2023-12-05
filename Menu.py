from abc import ABCMeta,abstractmethod

class Menu(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, id, price) -> None:
        self.name = name
        self.id = id
        self.price = price

    def UpdateMenu(self, name, price, menutype):
        if name!='': self.name = name
        if price!='': self.price = price
        if menutype!='': self.menutype = menutype
    
    def __hash__(self): # 딕셔너리 키로 Menu객체를 사용하기 위해 구현
        return hash(self.name)

    def __eq__(self, other): # 딕셔너리 키로 Menu객체를 사용하기 위해 구현
        return isinstance(other, Menu) and self.name == other.name