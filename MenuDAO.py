from Singleton import SingletonInstance
from password import password
import pymysql

class MenuDAO(SingletonInstance):
    def __init__(self) -> None:
        self.menudbcache = None
        pass
    
    def connectDB(self):
        conn = pymysql.connect(host='localhost', user='root', password=password, charset='utf8')
        cursor = conn.cursor()
        return conn, cursor
    
    def getMenuDB(self):
        conn, cursor = self.connectDB()

        sql = "SELECT * FROM kookminkiosk.menu;" 

        cursor.execute(sql)
        res = cursor.fetchall()
        
        conn.commit() 
        conn.close() 

# 응답 예시
#((1, '라면', 5000, 'Food'),  (2, '김밥', 1500, 'Food'), (3, '떡볶이', 2000, 'Food'), 
# (4, '순대', 2000, 'Food'), (5, '사이다', 1000, 'Drink'), (6, '콜라', 1000, 'Drink'), 
# (7, '환타', 1000, 'Drink'), (8, '라면+김밥', 6000, 'Set'), (9, '라면+순대', 6500, 'Set'), 
# (10, '김밥+떡볶이', 2500, 'Set'))
if __name__ == '__main__':
    dao = MenuDAO()
    dao.getMenuDB()
