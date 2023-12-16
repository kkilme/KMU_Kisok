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
    
    def getOrderHistory(self):
        self.connectDB()
        
        sql = "SELECT * FROM kookminkiosk.order"
        self.cursor.execute(sql)
        
        res = self.cursor.fetchall()
        self.disconnectDB()
        return res
    
    def getTotalSalesPerMenu(self):
        self.connectDB()
        
        sql = """
            SELECT
                menu.id AS menu_id,
                menu.name AS menu_name,
                SUM(orderdetail.quantity * menu.price) AS total_sales
            FROM
                kookminkiosk.orderdetail
            JOIN
                kookminkiosk.menu ON orderdetail.menuid = menu.id
            GROUP BY
                menu.id, menu.price;
            """
        self.cursor.execute(sql)
        
        res = self.cursor.fetchall()
        self.disconnectDB()
        return res
    
if __name__ == "__main__":
    db = OrderDAO()
    print(db.getOrderDetailHistory())