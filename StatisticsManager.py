from Singleton import SingletonInstance
from DBManager import DBManager

class StatisticsManager(SingletonInstance):
    def __init__(self):
        self.DBManager = DBManager.instance()
        
        self.daily_income_dict = dict()
        self.sorted_orderhistory = dict()
        self.oldest_date = str()
        self.latest_date = str()

    # rawdata로부터 통계 생성
    def GenerateOrderStatistics(self):
        raworderhistory = DBManager.getOrderHistoryDB()

        sorted_dates = sorted(raworderhistory.keys())
        self.oldest_date = sorted_dates[0]
        self.latest_date = sorted_dates[-1]

        self.sorted_orderhistory = sorted(raworderhistory.items(), # 가장 많이 팔린 메뉴 기준으로 정렬
        key=lambda x: max(x[1].values(), key=lambda y: y['quantity']), 
        reverse=True)

        for date, menu in raworderhistory.items(): # 날짜별 총 수익 계산
            total_income = sum(menu_item['quantity'] * menu_item['price'] for menu_item in menu.values())
            self.daily_income_dict[date] = total_income

    def DisplayAvailableStatistics(self):
        print(f' 가능한 날짜 범위: {self.oldest_date} ~ {self.latest_date}')

    def DisplayBestSellingMenu(self):
        pass

    def DisplayDailyIncome(self):
        pass

raworderhistory = {
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