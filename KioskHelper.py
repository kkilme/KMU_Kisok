import time
from Singleton import SingletonInstance
class KioskHelper(SingletonInstance):
    def __init__(self) -> None:
        pass

    def SetKioskLanguage(self):
        num = int(input())

        if num == 2:
            return 'EN'
        else:
            return 'KR'

    def CallEmployee(self):
        print("Do you need help from staff? 1: yes 2:no")
        
        if input() == '1' :
            print("\n...Calling Manager...please wait...\n")
            time.sleep(2)
        else :
            print("Back")