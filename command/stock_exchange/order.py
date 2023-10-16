from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    """
    고객의 주문을 나타내는 Order Interface
    Command 객체를 나타낸다.
    ConcreteCommand가 구현할 세부 로직을 정의한다.
    """
    @abstractmethod
    def execute(self):
        """
        ConcreteCommand 클래스가 Order 클래스를 실행하는 추상 메소드
        :return:
        """
        pass
