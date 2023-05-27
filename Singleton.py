class SingletonInstance: # 이 클래스를 상속받으면 싱글톤으로 구현가능
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = cls(*args, **kwargs)
        cls.instance = cls.__getInstance
        return cls.__instance