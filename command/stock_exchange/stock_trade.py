
class StockTrade:
    """
    Receiver 객체를 나타낸다.
    ConcreteCommand 객체가 생성한 주문을 처리하는 여러 메소드를 정의한다.
    Receiver에 정의된 buy()와 sell() 메소드는 BuyStockOrder와 SellStockOrder 클래스가 주식을 매수 또는 매도할 때 호출된다.
    """
    def buy(self):
        """
        주식을 매수할 때 호출되는 함수
        :return:
        """
        print("You will buy stocks")
    def sell(self):
        """
        주식을 매도할 때 호출되는 함수
        :return:
        """
        print("You will sell stocks")