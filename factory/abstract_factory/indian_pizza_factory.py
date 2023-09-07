from pizza_factory import PizzaFactory
from pizza import *


class IndianPizzaFactory(PizzaFactory):
    """
        PizzaFactory를 상속받아 각각의 추상 메소드를 구현한다.
        인도식에 맞는 야채피자와 일반피자를 만든다.
    """

    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()
