import pickle
from datetime import datetime
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
        menu_dict = {}
        for menu in mlist:
            menu_dict[menu.name] = {
                'id': menu.id,
                'price': menu.price,
                'description': menu.description
            }
        
        menudata = open(self.menufilename, 'wb')
        pickle.dump(menu_dict, menudata) # menudata에 덮어쓰기
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

    def UpdateOrderHistory(self, order):
        orderhistory = self.orderhistoryDB
        order_date = datetime.strptime(order.orderDate, '%Y-%m-%d %H:%M:%S')
        order_date = order_date.strftime("%Y-%m-%d")  # 주문 날짜를 문자열 형식으로 변환
        if order_date in orderhistory:  # 이미 해당 날짜의 주문이 존재하는 경우
            for menu, quantity in order.orderItems.items():
                menu_name = menu.name
                if menu_name in orderhistory[order_date]:  # 이미 해당 메뉴의 주문이 존재하는 경우
                    orderhistory[order_date][menu_name]['quantity'] += quantity
                else:  # 해당 메뉴의 주문이 처음인 경우
                    menu_price = menu.price
                    orderhistory[order_date][menu_name] = {
                        'quantity': quantity,
                        'price': menu_price
                    }
        else:  # 해당 날짜의 주문이 처음인 경우
            orderhistory[order_date] = {}
            for menu, quantity in order.orderItems.items():
                menu_name = menu.name
                menu_price = menu.price
                orderhistory[order_date][menu_name] = {
                    'quantity': quantity,
                    'price': menu_price
                }
        self.orderhistoryDB = orderhistory
        self.SaveOrderHistory(orderhistory)

        print()
        print("테스트용 출력: 현재 orderhistory")
        print(orderhistory)
        print()

    def SaveOrderHistory(self, orderhistory):
        orderdata = open(self.orderhistoryfilename, 'wb')
        pickle.dump(orderhistory, orderdata)
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