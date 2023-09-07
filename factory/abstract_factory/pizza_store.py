from indian_pizza_factory import IndianPizzaFactory
from us_pizza_factory import USPizzaFactory
class PizzaStore:
    def __init__(self):
        self.VegPizza = None
        self.NonVegPizza = None
        self.factory = None
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)

pizza_store = PizzaStore()
pizza_store.makePizzas()