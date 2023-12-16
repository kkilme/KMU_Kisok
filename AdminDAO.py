from DAOTemplate import DAOTemplate

class AdminDAO(DAOTemplate):
    def __init__(self) -> None:
        super().__init__()
    
    def getPassword(self):
        self.connectDB()
        
        sql = "SELECT password FROM kookminkiosk.admin;" 

        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        
        self.disconnectDB()
        return res[0][0]
    
if __name__ == "__main__":
    dao = AdminDAO()
    print(dao.authenticate())
    