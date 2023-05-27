import time
from Singleton import SingletonInstance

class KioskHelper(SingletonInstance):
    def __init__(self) -> None:
        pass

    def getInstance():
        pass

    def SetKioskLanguage(self):
        print("Select : ( Korean / English )")
        language = input()

        if language == 'EN' or language.upper() == 'ENGLISH':
            return 'EN'
        elif language == 'KR' or language.upper() == 'KOREAN':
            return 'KR'

    def CallEmployee(self):
        print("Do you need help from staff? (yes/no)")
        ans = input()
        if ans.upper() == 'YES' :
            print("\n...Calling Manager.....waiting please...\n")
            time.sleep(2)
        else :
            print("Back")

    def DisplayAvailableHelp():
        pass