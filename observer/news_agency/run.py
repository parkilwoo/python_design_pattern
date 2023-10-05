from news_publisher import NewsPublisher
from email_subscriber import EmailSubscriber
from sms_subscriber import SMSSubscriber
from any_other_subscriber import AnyOtherSubscriber

if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for Subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscriber(news_publisher)

    print("\nSubscribers:", news_publisher.subscribers())

    news_publisher.addNews('Hello World!')
    news_publisher.notifySubscribers()

    print("\nDetached:", type(news_publisher.detach()).__name__)
    print("\nSubscribers:", news_publisher.subscribers())

    news_publisher.addNews('My Second News!')
    news_publisher.notifySubscribers()