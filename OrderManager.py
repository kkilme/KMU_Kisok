from Order import Order
from Singleton import SingletonInstance
from MenuManager import MenuManager

class OrderManager(SingletonInstance):
    def __init__(self) -> None:
        self.MenuManager = MenuManager()
        self.cartList = []
        pass

    def getInstance():
        pass

    def OrderMenu(self, UIDict):
        self.MenuManager.DisplayMenu(UIDict)
        while(1):
            itemNum = int(input("메뉴 선택 : "))
            if itemNum == 0 :
                print("clear cart")
                continue
            elif itemNum == -1 :
                print("go to purchase")
                break
            if itemNum < 0 or itemNum >len(self.MenuManager.menuList) :
                print("wrong input! again please!")
                continue
            self.AddToCart(itemNum)
            self.PrintCart(UIDict)
        
        # date = "20230527"
        # istakeout = input("포장유무(O/X)")
        # tmp = Order(id, date, id, items, tprice, istakeout)
                
        
    def AddToCart(self, itemNum):
        menu = self.MenuManager.menuList[itemNum-1]  #메뉴리스트에 있는 메뉴 객체 가져옴.
        # 떡볶이 올테고, 수량 입력
        quantity = int(input("수량: "))
        OrderItem = [menu, quantity]
        self.cartList.append(OrderItem)

    def PrintCart(self, UIDict):
        print(UIDict['cartscreen'], end="")
        for i in self.cartList:
            print("- {}({})".format(i[0].name, i[1]))
        print("\n\n")



    def RemoveFromCart(item):
        pass

    def ClearCart():
        pass

    def MakeOrder():
        pass

    def MakeReceipt():
        pass

    def MakeNumberTicket():
        pass

    def ResetNumberTicketNum():
        pass

    def CheckTakeOut():
        pass

    def CalculateTotalPrice():
        pass

    def RequestPayment():
        pass