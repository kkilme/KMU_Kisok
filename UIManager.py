from uitexts import *
from MenuManager import MenuManager
from OrderManager import OrderManager
from KioskHelper import *
from AdminManager import *
from Singleton import SingletonInstance

class UIManager(SingletonInstance):
    def __init__(self) -> None:
        self.language = 'KR'
        self.UIDict = UI_KR
        self.MenuManager = MenuManager()
        self.KioskHelper = KioskHelper()
        self.AdminManager = AdminManager()
        self.OrderManager = OrderManager()

    def MainScreen(self):
        print(self.UIDict['mainscreen'])
        selectNum = int(input())
        print()

        if selectNum == 1:  #메뉴 보기
            self.OrderManager.MakeOrder(self.UIDict)

        elif selectNum == 2:  #언어 설정
            self.language = self.KioskHelper.SetKioskLanguage()
            if self.language == 'KR':
                self.UIDict = UI_KR
            else :
                self.UIDict = UI_EN
            self.MainScreen()
            
        elif selectNum == 3:  #직원 호출
            self.KioskHelper.CallEmployee()
            self.MainScreen()

        elif selectNum == 4:  #관리자 모드
            self.AdminManager.Login()

        else :
            print("Error! Again Please")
            time.sleep(2)
            self.MainScreen()