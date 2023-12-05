import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 800, 300)       

        self.ta1 = QTableWidget(self)
        self.ta1.resize(400, 500)
        self.ta1.setColumnCount(3)       

        table_column=["첫번째 열" , "두번째 열" , "Third 열"]
        self.ta1.setHorizontalHeaderLabels(table_column)      
        
        #행 2개 추가
        self.ta1.setRowCount(2)
        
        #추가된 행에 데이터 채워넣음
        self.ta1.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.ta1.setItem(0, 1, QTableWidgetItem("(0,1)"))
        self.ta1.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.ta1.setItem(1, 1, QTableWidgetItem("(1,1)"))

        self.btn1 = QPushButton("버튼")
        self.btn2 = QPushButton("버튼")

        self.btn1.clicked.connect(self.btn_fun)
        self.btn2.clicked.connect(self.btn_fun)

        self.ta1.setCellWidget(0,2,self.btn1)
        self.ta1.setCellWidget(1,2,self.btn2)
    
    def btn_fun(self):
        button = self.sender()

        item = self.ta1.indexAt(button.pos())        
        print( self.ta1.item( item.row(),0 ).text()  )

                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()