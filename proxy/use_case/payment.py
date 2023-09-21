from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    """
        Subject 클래스
        Subject 클래스는 Proxy와 RealSubject가 구현하는 인터페이스이다.
    """

    @abstractmethod
    def do_pay(self):
        """
            Proxy와 RealSubject가 구현해야 할 do_pay메소드를 포함한다.
        :return:
        """
        pass
