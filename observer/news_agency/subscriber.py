from abc import ABCMeta, abstractmethod


class Subscriber(metaclass=ABCMeta):
    """
    Observer Interface
    모든 ConcreteObserver의 추상 기본클래스가 된다.
    """

    @abstractmethod
    def update(self):
        """
        ConcreateObserver(구현체)는 update() 메소드를 통해 Subject(NewsPublisher)로 부터 새로운 뉴스 알림을 받는다.
        :return:
        """
        pass
