class NewsPublisher:
    """
    Subject 클래스
    서브젝트의 행동(메소드)를 구현한다.
    구독자(Observer)가 구현할 인터페이스를 제공한다.
    """

    def __init__(self):
        self.__subscribers = []
        self.__lastNews = None

    def attach(self, subscriber):
        """
        Subscriber(observer)는 attach()를 통해 NewsPublisher에 등록한다.(구독)
        :param subscriber: 구독자(observer) 객체
        :return:
        """
        self.__subscribers.append(subscriber)

    def detach(self):
        """
        Subscriber(observer)는 attach()를 통해 NewsPublisher에 등록을 취소한다.(구독 해지)
        현재 구현은 간단하게 pop을 통해 가장 최근에 구독한 Subscriber를 구독 취소
        :return:
        """
        self.__subscribers.pop()

    def subscribers(self):
        """
        현재 Subject에 구독중인 구독자 목록을 반환
        :return:
        """
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        """
        Subject에 구독중인 모든 구독자(Subscriber)에게 알림을 보낸다.
        :return:
        """
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        """
        Subject는 addNews() 메서드로 새로운 뉴스를 등록한다.
        :param news: 뉴스
        :return:
        """
        self.__lastNews = news

    def getNews(self):
        """
        Subject는 getNews() 메서드로 현재 최신 뉴스를 Observer에게 전달한다.
        :return:
        """
        return "Got News:", self.__lastNews
