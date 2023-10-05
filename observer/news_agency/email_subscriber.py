from subscriber import Subscriber
from news_publisher import NewsPublisher


class EmailSubscriber(Subscriber):
    """
    Subscriber(Observer) 인터페이스를 구현한 구현체(ConcreteObserver)
    """

    def __init__(self, publisher: NewsPublisher):
        """
        생성자를 통해 자신을 Subject(NewsPublisher)에 등록한다.(구독)
        :param publisher:
        """
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        """
        update() 메소드를 통해 새로운 뉴스의 알림을 받는다.
        eamil로 뉴스를 전달하는 구현을 하면된다.
        :return:
        """
        print(type(self).__name__, self.publisher.getNews())
