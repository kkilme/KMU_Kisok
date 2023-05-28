import pickle
from Singleton import SingletonInstance

class DBManager(SingletonInstance):


    def __init__(self):
        self.menufilename = 'menu.dat'
        self.orderhistoryfilename = 'orderhistory.dat'
        self.adminfilename = 'admin.dat'

        self.menuDB = self.LoadMenuDB()
        self.orderhistoryDB = self.LoadOrderHistory()
        self.adminPass = self.LoadAdminDB() #현재는 비밀번호를 의미하는 하나의 스트링
    

    def SaveMenuDB(self, mlist):
        menudata = open(self.menufilename, 'wb')
        pickle.dump(mlist, menudata) # mlist를 menudata에 덮어쓰기
        menudata.close()

    def LoadMenuDB(self):
        try:
            menudata = open(self.menufilename, 'rb')
        except FileNotFoundError as e: # 데이터 파일이 없음
            print('Menufile Not Found')
            return {}
        menulist = pickle.load(menudata)
        menudata.close()
        return menulist

    def UpdateOrderHistory(order):
        pass

    def SaveOrderHistory(self, orderlist):
        orderdata = open(self.orderhistoryfilename, 'wb')
        pickle.dump(orderlist, orderdata)
        orderdata.close()

    def LoadOrderHistory(self):
        try:
            orderdata = open(self.orderhistoryfilename, 'rb')
        except FileNotFoundError as e:
            print('Orderfile Not Found')
            return {}
        orderhistory = pickle.load(orderdata)
        orderdata.close()
        return orderhistory
    
    def SaveAdminDB(self):
        admindata = open(self.adminfilename, 'wb')
        pickle.dump(self.adminPass, admindata)
        admindata.close()

    def LoadAdminDB(self):
        try:
            admindata = open(self.adminfilename, 'rb')
        except FileNotFoundError as e:
            print('Adminfile Not Found')
            return '0000'
        admindb = pickle.load(admindata)
        admindata.close()
        return admindb
    
    def UpdateAdminDB(self, new):
        self.adminPass = new
        self.SaveAdminDB()

    def getMenuDB(self):
        return self.menuDB
    
    def getAdminDB(self):
        return self.adminPass
    
    def getOrderHistoryDB(self):
        return self.orderhistoryDB
    
    def getNextOrderID(self):
        return len(self.orderhistoryDB) + 1
    
    def getNextMenuID(self):
        return len(self.menuDB) + 1


orderhistory = {
    '2023-05-29':{
        '떡볶이':{
            'quantity': 2,
            'price': 3500
        },
        '라면': {
            'quantity': 3,
            'price': 3000,
        }
    },
    '2023-05-30':{
        '떡볶이':{
            'quantity': 2,
            'price': 3500
        }
    }
}

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

admin = '0000' #비밀번호

# if __name__ == '__main__':
#     db = DBManager.instance()
#     db.SaveMenuDB(menulist)