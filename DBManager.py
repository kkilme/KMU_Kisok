import pickle
class DBManager:
    def __init__(self):
        self.menufilename = 'menu.dat'
        pass

    def UpdateMenuList(mlist):
        pass

    def LoadMenuList(self):
        menuData = open(self.menufilename, 'rb')
        menulist = pickle.load(menuData)
        menuData.close()
        return menulist

    def SaveOrder(order):
        pass

    def getInstance():
        pass

    def getOrderHistory():
        pass


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