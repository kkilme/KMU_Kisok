import time
from Singleton import SingletonInstance
from DBManager import DBManager
from MenuManager import MenuManager
from StatisticsManager import StatisticsManager

class AdminManager(SingletonInstance):
    def __init__(self):
        self.DBManager = DBManager.instance()
        self.MenuManager = MenuManager.instance()
        self.StatisticsManager = StatisticsManager.instance()

    def Authenticate(self, password):
        dbpassword = self.DBManager.getAdminDB()
        if password == dbpassword:
            return True
        else:
            print(f'테스트용 출력 - 현재 비밀번호는 {dbpassword}입니다.') 
            return False

    def DisplayAvailableFunctions(self):
        # 관리자 모드: 다국어 필요 없음
        print('''
        *****************************************
        *              관리자 모드               *
        *             1. 메뉴 관리               *
        *             2. 통계 확인               *
        *            3. 비밀번호 변경            *
        *              4. 뒤로가기               *
        *****************************************
        ''')
        n = input()
        try:
            n = int(n)
        except:
            print("잘못된 값을 입력했습니다.")
            self.DisplayAvailableFunctions()
        if n<0 or n>4:
            print("잘못된 값을 입력했습니다.")
            self.DisplayAvailableFunctions()
        return n
    
    def ManageMenu(self):
        while True:
            print('''
            **************************************
            *             메뉴 관리               *
            *                                    *
            *            1. 메뉴 추가             *
            *            2. 메뉴 수정             *
            *            3. 메뉴 제거             *
            *            4. 메인 화면으로         *
            *                                    *
            **************************************
            ''')
            n = input()
            try:
                n = int(n)
            except:
                print("잘못된 값을 입력했습니다.")
                time.sleep(1)
                continue
            if n<0 or n>4:
                print("잘못된 값을 입력했습니다.")
                time.sleep(1)
                continue

            if n==1: #메뉴 추가
                print("메뉴를 추가합니다.")
                menutype = input("메뉴 타입을 입력하세요(Drink 또는 Food): ")
                if menutype.lower() != 'drink' and menutype.lower() != 'food':
                    print("잘못된 메뉴 타입입니다.")
                    time.sleep(1)
                    continue
                menuname = input("메뉴 이름을 입력하세요: ")
                menuprice = input("메뉴 가격을 입력하세요: ")
                try:
                    menuprice = int(menuprice)
                except:
                    print("가격은 숫자여야 합니다.")
                    time.sleep(1)
                    continue
                menudesc = input("메뉴 설명을 입력하세요: ")

                self.MenuManager.CreateMenu(menuname, menuprice, menudesc, menutype)

                print("성공적으로 메뉴를 추가했습니다.")
                time.sleep(1)
            
            elif n==2: #메뉴 수정
                print("현재 메뉴 리스트")
                self.MenuManager.DisplayMenu()
                idx = int(input("수정할 메뉴의 번호를 입력하세요: ")) - 1
                if idx<0 or idx>self.MenuManager.getMenuListLength()-1:
                    print("잘못된 값을 입력했습니다.")
                else:
                    print("수정할 메뉴: ")
                    self.MenuManager.DisplayMenu(idx=idx)
                    newmenutype = input("새로운 메뉴 타입을 입력하세요(Drink 또는 Food) (유지 원할 시 공백입력): ")
                    if menutype.lower() != 'drink' and menutype.lower() != 'food':
                        print("잘못된 메뉴 타입입니다.")
                        time.sleep(1)
                        continue
                    newname = input("새로운 이름을 입력하세요. (유지 원할 시 공백입력): ")
                    newprice = int(input("새로운 가격을 입력하세요. (유지 원할 시 공백입력): "))
                    newdesc = input("새로운 설명을 입력하세요. (유지 원할 시 공백입력): ")
                    self.MenuManager.EditMenu(idx, newname, newprice, newdesc, newmenutype)
                    print("성공적으로 메뉴를 수정했습니다.")
                    time.sleep(1)



            elif n==3: # 메뉴 제거
                print("현재 메뉴 리스트")
                self.MenuManager.DisplayMenu()
                idx = int(input("제거할 메뉴의 번호를 입력하세요: ")) - 1
                if idx<0 or idx>self.MenuManager.getMenuListLength()-1:
                    print("잘못된 값을 입력했습니다.")
                else:
                    self.MenuManager.RemoveMenu(idx)
                    print("성공적으로 메뉴를 제거했습니다.")
                time.sleep(1)

            elif n==4:
                print("잠시 후 메인 화면으로 돌아갑니다...")
                time.sleep(1.5)
                break

    def ViewStatistics(self):
        self.StatisticsManager.GenerateOrderStatistics()
        while True:
            print('''
            *************************************
            *                                   *
            *             통계 확인              *
            *                                   *
            *      1. 총 수익 확인               *
            *      2. 가장 많이 팔린 메뉴 확인    *
            *      3. 메인 화면으로              *
            *                                   *
            *************************************
            ''',)
            n = input()
            try:
                n = int(n)
            except:
                print("잘못된 값을 입력했습니다.")
                continue
            if n<0 or n>3:
                print("잘못된 값을 입력했습니다.")
                continue
            if n==1:
                print()
                self.StatisticsManager.DisplayDailyIncome()
                input("\n아무 텍스트를 입력하면 메인화면으로 돌아갑니다...")
                break

            elif n==2:
                print()
                self.StatisticsManager.DisplayBestSellingMenu()
                input("\n아무 텍스트를 입력하면 메인화면으로 돌아갑니다...")
                break
            
            else:
                break
        

    def UpdateAccount(self):
        newpass = input('새 비밀번호를 입력하세요: ')
        self.DBManager.UpdateAdminDB(newpass)
        print("비밀번호 변경에 성공했습니다! 잠시 후 메인 화면으로 돌아갑니다...")