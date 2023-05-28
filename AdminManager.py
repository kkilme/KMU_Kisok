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

    def Login():
        pass

    def Logout():
        pass

    def Authenticate(self, password):
        dbpassword = self.DBManager.getAdminDB()
        if password == dbpassword:
            return True
        else:
            print(f'테스트용 프린트! 현재 비밀번호는 {dbpassword}입니다.') 
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
        print('''
        **************************************
        *             메뉴 관리               *
        *                                    *
        *            1. 메뉴 추가             *
        *            2. 메뉴 수정             *
        *            3. 메뉴 제거             *
        *                                    *
        **************************************
        ''')

    def ViewStatistics(self):
        print('''
        *************************************
        *                                   *
        *             통계 확인              *
        *                                   *
        *      1. 총 수익 확인               *
        *      2. 가장 많이 팔린 메뉴 확인    *
        *                                   *
        *************************************
        ''',)

    def UpdateAccount(self):
        newpass = input('새 비밀번호를 입력하세요: ')
        self.DBManager.UpdateAdminDB(newpass)
        print("비밀번호 변경에 성공했습니다! 잠시 후 메인 화면으로 돌아갑니다...")