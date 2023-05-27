class Order:
    def __init__(self, id, date, items, tprice, istakeout) -> None:
        self.orderDate = date
        self.orderId = id
        self.orderItems = items
        self.totalPrice = tprice
        self.isTakeOut = istakeout
        