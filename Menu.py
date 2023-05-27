class Menu:
    def __init__(self, name, id, price, desc) -> None:
        self.name = name
        self.id = id
        self.price = price
        self.description = desc
    
    def __hash__(self): # 딕셔너리 키로 Menu객체를 사용하기 위해 구현
        return hash(self.name)

    def __eq__(self, other): # 딕셔너리 키로 Menu객체를 사용하기 위해 구현
        return isinstance(other, Menu) and self.name == other.name