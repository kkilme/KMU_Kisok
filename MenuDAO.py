from DAOTemplate import DAOTemplate

class MenuDAO(DAOTemplate):
    def __init__(self) -> None:
        super().__init__()
    
    def getMenuDB(self):
        self.connectDB()

        sql = "SELECT * FROM kookminkiosk.menu;" 

        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        
        self.disconnectDB()
        return res

    def editMenu(self, id, name, price, menutype):
        self.connectDB()

        sql = "UPDATE kookminkiosk.menu SET `name` = %s, `price` = %s, `type` = %s WHERE (`id` = %s);"

        self.cursor.execute(sql, (name, price, menutype, id))
        
        self.disconnectDB()
        
    def deleteMenu(self, id):
        self.connectDB()
        
        sql = "UPDATE kookminkiosk.menu SET `islegacy` = 1 WHERE (`id` = %s);"
        self.cursor.execute(sql, (id))
        
        self.disconnectDB()
    
    def createMenu(self, name, price, menutype):
        self.connectDB()
        
        sql = "INSERT INTO kookminkiosk.menu (name, price, type, islegacy) VALUES (%s, %s, %s, 0)"
        self.cursor.execute(sql, (name, price, menutype))

        self.disconnectDB()

    

if __name__ == '__main__':
    dao = MenuDAO()
    dao.getMenuDB()
