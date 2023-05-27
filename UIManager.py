from uitexts import *
from MenuManager import MenuManager
from KioskHelper import *
from AdminManager import *
from Singleton import SingletonInstance

class UIManager(SingletonInstance):
    def __init__(self) -> None:
        self.language = 'KR'
        self.UIDict = UI_KR
        pass


    def setLanguage(language, self):
        self.language = language;
        if language == 'EN':
            self.UIDict = UI_EN
        else:
            self.UIDict = UI_KR

    def MainScreen(self):
        print(self.UIDict['mainscreen'])   #왜 오류나지

        selectNum = input()
        if selectNum == 1:  #메뉴 보기
            MenuManager()
        elif selectNum == 2:  #언어 설정
            KioskHelper.SetKioskLanguage()
        elif selectNum == 3:  #직원 호출
            KioskHelper.CallEmployee()
        elif selectNum == 4:  #관리자 모드
            AdminManager()
        else :
            print("Error! Again Please")