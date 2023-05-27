from Singleton import SingletonInstance
from DBManager import DBManager
from UIManager import UIManager

class StatisticsManager(SingletonInstance):
    def __init__(self):
        self.DBManager = DBManager.instance()
        self.UIManager = UIManager.instance()

    def GenerateOrderStatistics():
        pass

    def DisplayOrderStatistics():
        pass

    def DisplayBestSellingMenu():
        pass

    def DisplayDailyIncome():
        pass