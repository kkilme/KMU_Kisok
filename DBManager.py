import pickle
from Singleton import SingletonInstance

class DBManager(SingletonInstance):


    def __init__(self):
        self.menufilename = 'menu.dat'
        self.orderhistoryfilename = 'orderhistory.dat'
        self.adminfilename = 'admin.dat'

        self.menuDB = self.LoadMenuDB()
        self.orderhistoryDB = self.LoadOrderHistory()
        self.adminDB = self.LoadAdminDB()
    

    def SaveMenuDB(self, mlist):
        menudata = open(self.menufile, 'wb')
        pickle.dump(mlist, menudata) # mlist를 menudata에 덮어쓰기
        menudata.close()

    def LoadMenuDB(self):
        try:
            menudata = open(self.menufilename, 'rb')
        except FileNotFoundError as e: # 데이터 파일이 없음
            print('File Not Found')
            return {}
        menulist = pickle.load(menudata)
        menudata.close()
        return menulist

    def UpdateOrderHistory(order):
        pass

    def LoadOrderHistory(self):
        try:
            orderdata = open(self.orderhistoryfilename, 'rb')
        except FileNotFoundError as e: # 데이터 파일이 없음
            print('File Not Found')
            return {}
        orderhistory = pickle.load(orderdata)
        orderdata.close()
        return orderhistory
    
    def SaveOrderHistory(self):
        pass

    def LoadAdminDB(self):
        try:
            admindata = open(self.adminfilename, 'rb')
        except FileNotFoundError as e: # 데이터 파일이 없음
            print('File Not Found')
            return {}
        admindb = pickle.load(admindata)
        admindata.close()
        return admindb
    
    def SaveAdminDB(self):
        pass
    
    def getMenuDB(self):
        menulist = {
            '떡볶이': {
                'id' : 1,
                'price': 3500,
                'description': '매콤달콤 추억의 간식!'
            } ,
            '라면': {
                'id' : 2,
                'price': 3000,
                'description': '꼬들꼬들 면발!'
            }
        }
        return menulist
    
    def getAdminDB(self):
        return self.adminDB
    
    def getOrderHistory(self):
        return self.orderhistoryDB
    
    def getNextOrderID(self):
        return len(self.orderhistoryDB) + 1
    
    def getNextMenuID(self):
        return len(self.menuDB) + 1


