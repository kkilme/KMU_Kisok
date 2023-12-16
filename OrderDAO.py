from DAOTemplate import DAOTemplate
from datetime import datetime

class OrderDAO(DAOTemplate):
    def __init__(self) -> None:
        super().__init__()
        
    
    def insertOrderData(self, data):
        self.connectDB()
        price, quantity = data
        date = datetime.now()
        sql = "INSERT INTO kookminkiosk.order (quantity, totalprice, orderdate) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (quantity, price, date))

        self.disconnectDB()
        return self.getLatestOrdernum()

    def insertOrderDetailData(self, orderid, data):
        self.connectDB()
        
        for key in data.keys():
            menuid = data[key]['menu'].id
            quantity = data[key]['quantity']
            sql = "INSERT INTO kookminkiosk.orderdetail (menuid, orderid, quantity) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (menuid, orderid, quantity))
            
        self.disconnectDB()
    
    def getLatestOrdernum(self):
        self.connectDB()
        
        sql = "SELECT id FROM kookminkiosk.order ORDER BY id DESC LIMIT 1"
        self.cursor.execute(sql)
        
        id = self.cursor.fetchall()
        
        return id
    
    def getTodayOrderCount(self):
        self.connectDB()
        
        sql = "SELECT COUNT(*) FROM kookminkiosk.order WHERE DATE(orderdate) = CURDATE()"
        self.cursor.execute(sql)
        
        cnt = self.cursor.fetchall()

        self.disconnectDB()
        return cnt[0][0]