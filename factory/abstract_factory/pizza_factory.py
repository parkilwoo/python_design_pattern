from abc import ABCMeta, abstractmethod
class PizzaFactory(metaclass=ABCMeta):
    """
        추상 메소드를 선언할 추상 클래스(피자 공장)
    """
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass
