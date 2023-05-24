from uitexts import *

class UIManager:
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
        print(self.UIDict['mainscreen'])