class Agent:
    """
    Invoker를 나타내는 클래스다.
    고객과 중개소 사이의 중개자이며 클라이언트의 주문을 처리한다.
    큐를 나타내는 리스트형 데이터 멤버가 있고, 모든 주문의 우선 이 큐에 추가한다.
    """
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        """
        주문을 큐에 적재하고 처리까지 담당하는 함수
        :param order: 주문 객체
        :return:
        """
        self.__orderQueue.append(order)
        order.execute()
