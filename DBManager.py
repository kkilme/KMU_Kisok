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
        return self.menuDB
    
    def getAdminDB(self):
        return self.adminDB
    
    def getOrderHistory(self):
        return self.orderhistoryDB


### DB example

menulist = {
    'rice': {
        'price': 1000,
        'description': 'rr'
    } ,
    'rice2': {
        'price': 1000,
        'description': 'rr'
    }
}

print(menulist['rice']['price'])

#dbfile name
self.menufile = 'menu.dat'
self.orderfile = 'order.dat'
self.adminfile = 'admin.dat'

# write
menuData = open(self.menufile, 'wb')
pickle.dump(menulist, menuData) # menulist를 menudata에 덮어쓰기
menuData.close()

#read

menuData = open(self.menufile, 'rb')
menulist2 = pickle.load(menuData)
menuData.close()