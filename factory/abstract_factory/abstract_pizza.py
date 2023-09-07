from abc import ABCMeta, abstractmethod


class VegPizza(metaclass=ABCMeta):
    """
        채식피자를 만들기 위한 추상 클래스 prepare라는 추상 메소드를 가지고 있다.
    """
    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(metaclass=ABCMeta):
    """
        일반피자를 만들기 위한 추상 클래스. 채식피자의 베이스 위에 토핑을 더하는 관계로 채식피자를 arg로 받는 추상 메소드를 가지고 있다.
    """
    @abstractmethod
    def serve(self, VegPizza):
        pass
