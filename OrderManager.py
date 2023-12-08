import time
import copy
from OrderDAO import OrderDAO
from MenuDAO import MenuDAO
from datetime import datetime
from Order import Order
from Singleton import SingletonInstance


class OrderManager(SingletonInstance):

    def __init__(self) -> None:
        self.OrderDAO = OrderDAO.instance()
        self.MenuDAO = MenuDAO.instance()
        self.cartDict = {}       
  
    def addToCart(self, menu, quantity):
        if menu.name in self.cartDict.keys():  #기존에 메뉴가 이미 추가되어있으면 수량 추가
            self.cartDict[menu.name]['quantity'] += quantity
        else :
            self.cartDict[menu.name] = {}
            self.cartDict[menu.name]['menu'] = menu
            self.cartDict[menu.name]['quantity'] = quantity
            
    def increaseCartItem(self, menuname):
        self.cartDict[menuname]['quantity'] += 1

    def decreaseCartItem(self, menuname):
        if self.cartDict[menuname]['quantity'] == 1:
            del self.cartDict[menuname]
        else:
            self.cartDict[menuname]['quantity'] -= 1
        
    def clearCart(self):
        self.cartDict.clear()
        
    def calculateTotalPrice(self):
        tprice = 0
        for data in self.cartDict.values():
            tprice += data['menu'].price * data['quantity']
        return tprice
    
    def calculateTotalQuantity(self):
        quantity = 0
        for data in self.cartDict.values():
            quantity += data['quantity']
            
        return quantity
    
    def processOrder(self):
        price = self.calculateTotalPrice()
        quantity = self.calculateTotalQuantity()
        
        orderid = self.OrderDAO.insertOrderData((price, quantity))
        self.OrderDAO.insertOrderDetailData(orderid, self.cartDict)
        
    def getCart(self):
        return self.cartDict
    
    def getTodayOrderCount(self):
        return self.OrderDAO.getTodayOrderCount()
    
    # def ProcessPayment(self):
    #     time.sleep(1)
    #     print("...Waiting for a payment...")
    #     time.sleep(1.5)
    #     print("Payment Success!")
    #     time.sleep(1)
        

    # def MakeReceipt(self):
    #     order = self.currentOrder
    #     print("주문날짜:", order.orderDate)
    #     print("주문내역:")
    #     for i in order.orderItems:
    #         print(f" - {i.name} {i.price}원 x{order.orderItems[i]}")
    #     print("포장유무: ", order.isTakeOut)
    #     print("\n합계금액: ", order.totalPrice)
    #     print("*****************************")

    # def MakeNumberTicket(self):
    #     print(f'\t     {self.numticketnum}\n')
    #     print("주문날짜:", self.currentOrder.orderDate)
    #     print("*****************************")
    #     self.numticketnum+=1

    # def ResetNumberTicketNum(self):
    #     self.numticketnum = 0

