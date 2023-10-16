from stock_trade import StockTrade
from order_impl.buy_stock_order import BuyStockOrder
from order_impl.sell_stock_order import SellStockOrder
from agent import Agent

if __name__ == '__main__':
    """
    클라이언트는 우선 StockTrade 클래스를 Receiver로 지정한다.
    BuyStockOrder와 SellStockOrder(ConcreteCommand)는 StockTrade 객체에 대해 거래를 요청해 주문을 생성한다.
    Invoker 객체는 Agent 클래스를 인스턴스화할 때 생성된다.
    Agent 클래스의 placeOrder() 메소드는 클라이언트의 요청을 주문한다.
    """
    #Client
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    # #Invoker
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)