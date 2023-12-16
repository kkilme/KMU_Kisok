import time
from Singleton import SingletonInstance
from AdminDAO import AdminDAO

class AdminManager(SingletonInstance):
    def __init__(self):
        self.AdminDAO = AdminDAO.instance()

    def authenticate(self, password):
        return password == self.AdminDAO.getPassword()

    