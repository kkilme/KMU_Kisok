from uitexts import *
import time
from MenuManager import MenuManager
from OrderManager import OrderManager
from KioskHelper import KioskHelper
from AdminManager import AdminManager
from StatisticsManager import StatisticsManager
from Singleton import SingletonInstance

class UIManager(SingletonInstance):
    def __init__(self):
        self.language = 'KR'
        self.UIDict = UI_KR
        self.MenuManager = MenuManager.instance()
        self.KioskHelper = KioskHelper.instance()
        self.AdminManager = AdminManager.instance()
        self.OrderManager = OrderManager.instance()
        self.StatisticsManager = StatisticsManager.instance()

    def MainScreen(self):
        while True:
            print(self.UIDict['mainscreen'])
            selectNum = int(input())
            print()

            if selectNum == 1:  #메뉴 보기
                self.MenuScreen()

            elif selectNum == 2:  #언어 설정
                print(self.UIDict['languageselect'])
                language = self.KioskHelper.SetKioskLanguage()
                if language == 'KR':
                    self.language ='KR'
                    self.UIDict = UI_KR
                else :
                    self.language ='EN'
                    self.UIDict = UI_EN
                continue
                
            elif selectNum == 3:  #직원 호출
                self.KioskHelper.CallEmployee()
                continue

            elif selectNum == 4:  #관리자 모드
                self.AdminLoginScreen()

            else :
                print("Wrong input, please enter valid number")
                time.sleep(2)
                continue

    def MenuScreen(self):
        while True:
            print(self.UIDict['menuscreen'], end='')
            self.MenuManager.DisplayMenu()
            print("*****************************")
            print(self.UIDict['cartscreen'], end="")
            self.OrderManager.DisplayCart()
            print("*****************************************")

            itemNum = int(input("메뉴 선택: "))
            if itemNum == 0 :  #결제하기
                if len(self.OrderManager.cartDict) == 0:
                    print("장바구니가 비어있습니다.")
                    time.sleep(1)
                    continue
                self.OrderManager.MakeOrder()
                self.OrderManager.ProcessPayment()
                self.ReceiptScreen()
                self.OrderManager.MakeReceipt()
                self.NumberTicketScreen()
                self.OrderManager.MakeNumberTicket()
                print("잠시 후 메인 화면으로 돌아갑니다...")
                time.sleep(3)
                break
            elif itemNum == -1 :  #장바구니 비우기
                self.OrderManager.ClearCart()
                continue
            elif itemNum == -2 :  # 메뉴 장바구니에서 제거
                idx = int(input("제거할 메뉴 번호 입력: ")) - 1
                if idx < 0 or idx >= len(self.OrderManager.cartDict.items()):
                    print("잘못된 번호입니다.")
                    time.sleep(2)
                    continue
                self.OrderManager.RemoveFromCart(idx)
                continue
            if itemNum < 0 or itemNum >len(self.MenuManager.menuList) :
                print("Wrong input! Please try again!")
                time.sleep(2)
            else:
                selectedMenu = self.MenuManager.getMenu(itemNum-1)
                quantity = int(input("수량: "))
                self.OrderManager.AddToCart(selectedMenu, quantity)

    def ReceiptScreen(self):
        print(self.UIDict['receiptscreen'])

    def NumberTicketScreen(self):
        print(self.UIDict['numberticket'])

    def AdminLoginScreen(self):
        # 현재 비밀번호 1234!!
        while True:
            print('***관리자 모드***')
            password = input('비밀번호를 입력하세요: ')
            
            if not self.AdminManager.Authenticate(password):
                print("잘못된 비밀번호를 입력했습니다.")
                time.sleep(1)
                break
            
            n = self.AdminManager.DisplayAvailableFunctions()
            if n == 1:
                self.AdminManager.ManageMenu()
            elif n == 2:
                self.AdminManager.ViewStatistics()
            elif n == 3:
                self.AdminManager.UpdateAccount()
            break

    def StatisticsScreen(self):
        print(self.UIDict['statisticsmain'])