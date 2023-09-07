from pizza_factory import PizzaFactory
from pizza import *
class USPizzaFactory(PizzaFactory):
    """
        PizzaFactory를 상속받아 각각의 추상 메소드를 구현한다.
        미국식에 맞는 야채피자와 일반피자를 만든다.
    """
    def createVegPizza(self):
        return MexicanPizza()

    def createNonVegPizza(self):
        return HamPizza()