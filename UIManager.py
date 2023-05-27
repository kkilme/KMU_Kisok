from uitexts import *
import time
from MenuManager import MenuManager
from OrderManager import OrderManager
from KioskHelper import KioskHelper
from AdminManager import AdminManager
from Singleton import SingletonInstance

class UIManager(SingletonInstance):
    def __init__(self):
        self.language = 'KR'
        self.UIDict = UI_KR
        self.MenuManager = MenuManager.instance()
        self.KioskHelper = KioskHelper.instance()
        self.AdminManager = AdminManager.instance()
        self.OrderManager = OrderManager.instance()

    def MainScreen(self):
        print(self.UIDict['mainscreen'])
        selectNum = int(input())
        print()

        if selectNum == 1:  #메뉴 보기
            self.MenuScreen()

        elif selectNum == 2:  #언어 설정
            print(self.UIDict['languageselect'])
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
            print("Wrong input, please enter valid number")
            time.sleep(2)
            self.MainScreen()

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
                self.MainScreen()
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