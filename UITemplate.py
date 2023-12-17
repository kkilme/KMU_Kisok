from PySide2.QtWidgets import QMainWindow

class UITemplate(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.presenter = None

    def assignPresenter(self, presenter):
        self.presenter = presenter

    def initUI(self):
        pass