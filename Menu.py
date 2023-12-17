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
    
    def __hash__(self): # 딕셔너리 키로 Menu객체를 사용하기 위해 구현
        return hash(self.name)

    def __eq__(self, other): # 딕셔너리 키로 Menu객체를 사용하기 위해 구현
        return isinstance(other, Menu) and self.name == other.name
    