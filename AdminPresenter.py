from MenuManager import MenuManager
from StatisticsManager import StatisticsManager
from AdminManager import AdminManager
from CustomWidgetCreator import CustomWidgetCreator
from AdminUI import AdminUI
from functools import partial

class AdminPresenter():
    def __init__(self, kioskpresenter) -> None:
        self.kioskpresenter = kioskpresenter
        self.ui = AdminUI()
        self.ui.assignPresenter(self)
        self.ui.initUI()
        self.MenuManager = MenuManager.instance()
        self.StatisticsManager = StatisticsManager.instance()
        self.AdminManager = AdminManager.instance()
        self.WidgetCreator = CustomWidgetCreator()
        self.menutypelist = self.MenuManager.getMenutypeList()
        self.loadMenu()
    
    # 관리자 도구 창 염
    def openUI(self):
        if not self.ui.isVisible():
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.wrongpasswordlabel.setText("")
            self.ui.show()
    
    # 비밀번호 인증
    def authenticate(self, password):
        success = self.AdminManager.authenticate(password)
        if success:
            self.ui.passwordlineedit.setText("")
            self.ui.changeUI(1)
        else:
            self.ui.wrongpasswordlabel.setText("잘못된 비밀번호입니다.")
    
    # 주문 대기목록에 주문 추가        
    def addOrderQueueItem(self, orderlist, ordernum, tprice):
        table = self.ui.orderqueuetable
        
        current_row_count = table.rowCount()
        table.setRowCount(current_row_count + 1)
        orderstr = ''
        for i, data in enumerate(orderlist.values()):
            orderstr += f'{data["menu"].name} x {data["quantity"]}'
            if i != len(orderlist) - 1:
                orderstr += '\n'
                
        table.setItem(current_row_count, 0, self.WidgetCreator.tableWidgetItem(str(ordernum)))
        table.setItem(current_row_count, 1, self.WidgetCreator.tableWidgetItem(orderstr))
        table.setItem(current_row_count, 2, self.WidgetCreator.tableWidgetItem(str(tprice)))
        removeButton = self.WidgetCreator.cartItemManageButton(managetype="remove")
        table.resizeRowToContents(current_row_count)
        removeButton.clicked.connect(lambda: self.removeOrderQueueItem(table, removeButton))
        table.setCellWidget(current_row_count, 3, removeButton)
    
    # 주문 대기목록에서 주문 삭제
    def removeOrderQueueItem(self, table, button):
        row = self.getWidgetRow(table, 3, button)
        table.removeRow(row)
    
    # 메뉴 관리 창에 현재 메뉴 목록 표시
    def loadMenu(self):
        table = self.ui.curmenutable
        menus = self.MenuManager.getMenuList()
        table.setRowCount(len(menus))
        
        for i, menu in enumerate(menus):
            table.setItem(i, 0, self.WidgetCreator.tableWidgetItem(str(menu.id)))
            table.setItem(i, 1, self.WidgetCreator.tableWidgetItem(menu.name))
            table.setItem(i, 2, self.WidgetCreator.tableWidgetItem(str(menu.price)))
            table.setItem(i, 3, self.WidgetCreator.tableWidgetItem(str(menu.menutype)[9:]))
            
            editButton = self.WidgetCreator.cartItemManageButton(managetype="edit")
            editButton.clicked.connect(partial(self.editMenu, menu.id, menu.name, str(menu.price), str(menu.menutype)[9:]))
            table.setCellWidget(i, 4, editButton)
            
            removeButton = self.WidgetCreator.cartItemManageButton(managetype="remove")
            removeButton.clicked.connect(lambda: self.deleteMenu(menu.id))
            table.setCellWidget(i, 5, removeButton)
               
    # 메뉴 수정
    def editMenu(self, id, name, price, menutype):
        original_values = [name, price, menutype]
        window = self.WidgetCreator.menuEditor(name, price, menutype, self.menutypelist)
        def sendsignal():
            newvalues = [window.menunameline.text(), window.menupriceline.text(), window.menutypecombobox.currentText()]
            for i in range(len(newvalues)):
                if newvalues[i] == '': newvalues[i] = original_values[i]
            self.MenuManager.editMenu(id, newvalues[0], newvalues[1], newvalues[2])
            window.close()
        window.okButton.clicked.connect(lambda: sendsignal())
        window.exec_()
        self.refresh()
    
    # 메뉴 삭제
    def deleteMenu(self, id):
        self.MenuManager.deleteMenu(id)
        self.refresh()
    
    # 메뉴 생성
    def createMenu(self):
        window = self.WidgetCreator.menuCreator(self.menutypelist)
        def sendsignal():
            newvalues = [window.menunameline.text(), window.menupriceline.text(), window.menutypecombobox.currentText()]
            for i in range(len(newvalues)):
                if newvalues[i] == '':
                    window.errormessage.setText("입력하지 않은 정보가 있습니다.")
                    return
            self.MenuManager.createMenu(newvalues[0], newvalues[1], newvalues[2])
            window.errormessage.setText("")
            window.close()
        window.okButton.clicked.connect(lambda: sendsignal())
        window.exec_()
        self.refresh()

    # ui 새로고침
    def refresh(self):
        self.loadMenu()
        self.menutypelist = self.MenuManager.getMenutypeList()
        self.kioskpresenter.loadMenu()
        
    # 위젯이 들어있는 행 찾음 
    def getWidgetRow(self, table, column, widget):
        row = -1
        for i in range(table.rowCount()):
            if table.cellWidget(i, column) == widget:
                row = i
        if row == -1:
            print("Could not find row")
            return -1
        return row
    