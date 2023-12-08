from Singleton import SingletonInstance
import pymysql
from password import password
from datetime import datetime
class OrderDAO(SingletonInstance):
    def __init__(self) -> None:
        self.conn = None
        self.cursor = None
    
    def connectDB(self):
        if self.conn and self.cursor: return
        self.conn = pymysql.connect(host='localhost', user='root', password=password, charset='utf8')
        self.cursor = self.conn.cursor()
    
    def disconnectDB(self):
        self.conn.commit()
        self.conn.close()
        self.conn = None
        self.cursor = None
    
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