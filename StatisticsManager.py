from Singleton import SingletonInstance
from DBManager import DBManager

class StatisticsManager(SingletonInstance):
    def __init__(self):
        self.DBManager = DBManager.instance()
        
        self.daily_income_dict = dict()
        self.bestselling_menu_dict = dict()
        self.sorted_orderhistory = dict()
        self.oldest_date = str()
        self.latest_date = str()

    # rawdata로부터 통계 생성
    def GenerateOrderStatistics(self):
        raworderhistory = self.DBManager.getOrderHistoryDB()

        sorted_dates = sorted(raworderhistory.keys())
        self.oldest_date = sorted_dates[0]
        self.latest_date = sorted_dates[-1]

        for date, menu_items in raworderhistory.items(): # 메뉴별로 판매량 기록 후 판매량을 기준으로 내림차순 정렬
            for menu, details in menu_items.items():
                quantity = details['quantity']
                if menu in self.bestselling_menu_dict:
                    self.bestselling_menu_dict[menu] += quantity
                else:
                    self.bestselling_menu_dict[menu] = quantity

        self.bestselling_menu_dict = dict(sorted(self.bestselling_menu_dict.items(), key=lambda x: x[1], reverse=True))

        self.sorted_orderhistory = sorted(raworderhistory.items(), # 날짜별로 가장 많이 팔린 메뉴 기준으로 정렬
        key=lambda x: max(x[1].values(), key=lambda y: y['quantity']), 
        reverse=True)

        for date, menu in raworderhistory.items(): # 날짜별 총 수익 계산
            total_income = sum(menu_item['quantity'] * menu_item['price'] for menu_item in menu.values())
            self.daily_income_dict[date] = total_income
    
    def DisplayBestSellingMenu(self):
        for menu, quantity in self.bestselling_menu_dict.items():
            print(f"{menu}: {quantity}")

    def DisplayDailyIncome(self):
        for date, income in self.daily_income_dict.items():
            print(f"{date}: {income}")

# 딕셔너리 형식을 임시로 표시
# raworderhistory = {
#     '2023-05-29':{
#         '떡볶이':{
#             'quantity': 2,
#             'price': 3500
#         },
#         '라면': {
#             'quantity': 3,
#             'price': 3000,
#         }
#     },
#     '2023-05-30':{
#         '떡볶이':{
#             'quantity': 2,
#             'price': 3500
#         }
#     }
# }