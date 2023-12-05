from abc import ABCMeta,abstractmethod 
from enum import Enum

class Menutype(Enum):
    Food = 1
    Drink = 2
    Set = 3
    
# 문자열을 Menutype Enum으로 변환하는 함수  
def stringToMenutype(value):
    for member in Menutype.__members__:
        if member.lower() == value.lower():
            return Menutype[member]
    raise ValueError(f"No such Menutype: {value}")

class Menu():
    def __init__(self, id: int, name: str, price:int , menutype: Menutype) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.menutype = menutype

    def UpdateMenu(self, name, price, menutype):
        if name!='': self.name = name
        if price!='': self.price = price
        if menutype!='': self.menutype = menutype
    
    def __hash__(self): # 딕셔너리 키로 Menu객체를 사용하기 위해 구현
        return hash(self.name)

    def __eq__(self, other): # 딕셔너리 키로 Menu객체를 사용하기 위해 구현
        return isinstance(other, Menu) and self.name == other.name
    
if __name__ == "__main__":
    test1 = Menu(1,"test",1000,Menutype.Drink)
    a = str(getattr(test1, "menutype"))
    print(a == "Menutype.Drink")
    