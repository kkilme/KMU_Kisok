import datetime
import matplotlib.pyplot as plt

class GraphDrawer():
    def __init__(self) -> None:
        plt.rc('font', family='Malgun Gothic')

    def drawDailyIncome(self, data):
        dates = list(data.keys())
        incomes = list(data.values())

        plt.figure(figsize=(10, 5))
        plt.plot(dates, incomes, marker='o', linestyle='-')
        plt.title('날짜별 수익')
        plt.xlabel('날짜')
        plt.ylabel('총 수익')
        plt.xticks(rotation=45) 
        plt.tight_layout()

        # 각 데이터 포인트에 수익 표시
        for date, income in zip(dates, incomes):
            plt.text(date, income, str(income), ha='center', va='bottom')

        plt.show()
        
    def drawSalesPerMenu(self, data):
        menu_names = list(data.keys())
        total_incomes = list(data.values())

        plt.figure(figsize=(10, 5))
        bars = plt.bar(menu_names, total_incomes, color='skyblue')
        plt.title('메뉴별 매출')
        plt.xlabel('메뉴 이름')
        plt.ylabel('총 수입')
        plt.xticks(rotation=45)
        plt.tight_layout()
        for bar, income in zip(bars, total_incomes):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(income), ha='center', va='bottom')

        plt.show()