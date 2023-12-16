from Singleton import SingletonInstance

class StatisticsManager(SingletonInstance):
    def __init__(self):
        
        self.daily_income_dict = dict()
        self.bestselling_menu_dict = dict()
        self.sorted_orderhistory = dict()
        self.oldest_date = str()
        self.latest_date = str()
