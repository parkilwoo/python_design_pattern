"""
    옵저버 패턴
    * 객체 간 일대다 (1:N) 관계를 형성하고 객체의 상태를 다른 종속 객체에 자동으로 알린다.
    * 서브젝트의 핵심 부분을 캡슐화 한다.
    eg)
        - 분산 시스템의 이벤트 서비스를 구현할 때
        - 뉴스 에이전시 프레임워크
        - 주식 시장 모델
"""
from abc import ABCMeta, abstractmethod, ABC


class Subject:
    """
        Observer를 관리하는 클래스
        register 메소드를 통해 observer들을 등록하고, notifyAll 메소드를 통해 모든 observer들에게 알림을 준다.
    """
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer(metaclass=ABCMeta):
    """
        Subject를 감시하는 객체를 위한 인터페이스
        Subject의 상태를 알 수 있도록 ConcreteObserver가 구현해야 하는 메소드를 정의한다.
    """
    @abstractmethod
    def notify(self, subject: Subject, *args):
        pass



class Observer1(Observer):
    """
        Subject의 상태를 저장한다.
        서브젝트에 대한 정보와 실제 상태를 일관되게 유지하기 위해 Observer 인터페이스를 구현한다.
    """
    def __init__(self, subject: Subject):
        subject.register(self)

    def notify(self, subject: Subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


class Observer2(Observer):
    def __init__(self, subject: Subject):
        subject.register(self)

    def notify(self, subject: Subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


subject = Subject()

observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notifyAll('notification')