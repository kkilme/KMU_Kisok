import time
import copy
from datetime import datetime
from Order import Order
from Singleton import SingletonInstance
from MenuManager import MenuManager
from DBManager import DBManager

class OrderManager(SingletonInstance):

    def __init__(self) -> None:
        self.MenuManager = MenuManager.instance()
        self.DBManager = DBManager.instance()
        self.cartDict = {}
        self.numticketnum = 1
        self.currentOrder = None
        self.nextorderid = self.DBManager.getNextOrderID()

    def MakeOrder(self):
        orderdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        totalprice = self.CalculateTotalPrice()
        orderid = self.nextorderid
        orderitems = copy.deepcopy(self.cartDict) # 깊은복사 해주어야 clearcart해도 내용이 사라지지 않음
        self.nextorderid+=1
        while True :
            istakeout = input("포장유무(O/X) : ").upper()
            if istakeout == 'O' or istakeout == 'X':
                break
            else:
                print("wrong input! again please")
        neworder = Order(orderid, orderdate, orderitems, totalprice, istakeout)
        self.currentOrder = neworder
        self.DBManager.UpdateOrderHistory(neworder)
        self.ClearCart()
        
  
    def AddToCart(self, menu, quantity):
        if menu in self.cartDict.keys():  #기존에 메뉴가 이미 추가되어있으면 수량 추가
            self.cartDict[menu] = self.cartDict[menu]+quantity
        else :
            self.cartDict[menu] = quantity

    def DisplayCart(self):
        if len(self.cartDict.items()) == 0:
            print("                  Empty")
            return
        for index, (key, value) in enumerate(self.cartDict.items(), start=1):
            print(f"            -  {index}. {key.name}({value})")

    def RemoveFromCart(self, idx):
        cartitems = list(self.cartDict.items())
        del cartitems[idx]
        self.cartDict = dict(cartitems)
        
    def ClearCart(self):
        self.cartDict.clear()
        
    def ProcessPayment(self):
        time.sleep(1)
        print("...Waiting for a payment...")
        time.sleep(1.5)
        print("Payment Success!")
        time.sleep(1)
        

    def MakeReceipt(self):
        order = self.currentOrder
        print("주문날짜:", order.orderDate)
        print("주문내역:")
        for i in order.orderItems:
            print(f" - {i.name} {i.price}원 x{order.orderItems[i]}")
        print("포장유무: ", order.isTakeOut)
        print("\n합계금액: ", order.totalPrice)
        print("*****************************")

    def MakeNumberTicket(self):
        print(f'\t     {self.numticketnum}\n')
        print("주문날짜:", self.currentOrder.orderDate)
        print("*****************************")
        self.numticketnum+=1

    def ResetNumberTicketNum(self):
        self.numticketnum = 0

    def CalculateTotalPrice(self):
        tprice = 0
        for i in self.cartDict:
            tprice += i.price * self.cartDict[i]
        return tprice
