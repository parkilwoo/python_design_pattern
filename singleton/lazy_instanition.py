class Singleton:
    __instance = None
    def __init__(self) -> None:
        if not Singleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance alreay created:", self.getInstance())
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
    



s = Singleton()
print("Object Created", Singleton.getInstance())
s1 = Singleton()