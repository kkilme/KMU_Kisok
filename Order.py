class Order:
    def __init__(self, id, date, items, tprice, istakeout) -> None:
        self.orderDate = date
        self.orderId = id
        self.orderItems = items # 주문한 메뉴 내역, 형식: {'menu1': 2}, 2=구매 수량(quantity)
        self.totalPrice = tprice
        self.isTakeOut = istakeout
        