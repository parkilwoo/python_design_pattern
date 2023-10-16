from command.stock_exchange.order import Order


class BuyStockOrder(Order):
    """
    Order 인터페이스를 구현한 구상 클래스(Concrete class)이다.
    증권 거래 시스템 객체를 사용해 주식을 매수한다.
    """

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        """
        주식 객체를 통해 주식을 매수하는 함수
        :return:
        """
        self.stock.buy()
