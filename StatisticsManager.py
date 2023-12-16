from Singleton import SingletonInstance
from OrderDAO import OrderDAO
class StatisticsManager(SingletonInstance):
    def __init__(self):
        self.orderDAO = OrderDAO().instance()

    def calcDailyIncome(self):
        res = self.orderDAO.getOrderHistory()
        dailyincome = {}
        for order in res:
            date_key = order[3].date()  # datetime 객체에서 날짜만 추출
            dailyincome[date_key] = dailyincome.get(date_key, 0) + order[2]
            
        return dailyincome
    
    def calcTotalSalesPerMenu(self):
        res = self.orderDAO.getTotalSalesPerMenu()
        menuincome = {}
        for id, name, income in res:
            menuincome[name] = menuincome.get(name, 0) + income
            
        return menuincome