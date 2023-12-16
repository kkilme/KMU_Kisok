from Singleton import SingletonInstance
import pymysql
from password import password

class DAOTemplate(SingletonInstance):
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