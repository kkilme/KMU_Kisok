import time
from Order import Order
from Singleton import SingletonInstance
from MenuManager import MenuManager

class OrderManager(SingletonInstance):
    def __init__(self) -> None:
        self.MenuManager = MenuManager()
        self.cartDict = {}
        pass

    def getInstance():
        pass

    def MakeOrder(self, UIDict):
        self.MenuManager.GenerateMenu()
        self.MenuManager.DisplayMenu(UIDict)
        while(1):
            itemNum = int(input("메뉴 선택 : "))
            if itemNum == 0 :  #장바구니 비우기
                self.ClearCart()
                self.MenuManager.DisplayMenu(UIDict)
                continue
            elif itemNum == -1 :  #결제하기
                self.Purchase(UIDict)
                break
            if itemNum < 0 or itemNum >len(self.MenuManager.menuList) :
                print("wrong input! again please!")
                continue
            self.AddToCart(itemNum)
            self.PrintCart(UIDict)
                
        
    def AddToCart(self, itemNum):
        menu = self.MenuManager.menuList[itemNum-1]  #메뉴리스트에 있는 메뉴 객체 가져옴.
        quantity = int(input("수량: "))

        if menu in self.cartDict.keys():  #기존에 메뉴가 이미 추가되어있으면 수량 추가
            self.cartDict[menu] = self.cartDict[menu]+quantity
        else :
            self.cartDict[menu] = quantity

    def PrintCart(self, UIDict):
        print(UIDict['cartscreen'], end="")
        for i in self.cartDict:
            print("- {}({})".format(i.name, self.cartDict[i]))
        print("\n\n")



    def RemoveFromCart(item):
        pass

    def ClearCart(self):
        print("Clear Cart!\n")
        self.cartDict.clear()
        
    def Purchase(self, UIDict):
        date = "20230527"  #임시날짜
        tprice = 0
        for i in self.cartDict:
            price = i.price * self.cartDict[i]
            tprice = tprice + price
        istakeout = input("포장유무(O/X) : ")
        time.sleep(2)
        print("...Waiting for a payment...")
        time.sleep(3)
        tmp = Order(date, id, self.cartDict, tprice, istakeout.upper())
        self.MakeReceipt(tmp, UIDict)
        

    def MakeReceipt(self, order, UIDict):
        print(UIDict['receiptscreen'], end="")
        print("주문날짜 : ", order.orderDate)
        print("주문내역:")
        for i in order.orderItems:
            print(" - {} {}원 ({})".format(i.name, i.price, order.orderItems[i]))
        print("포장유무: ", order.isTakeOut)
        print("\n합계금액: ", order.totalPrice)
        print("*****************************")

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