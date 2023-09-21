from payment import Payment
from bank import Bank


class DebitCard(Payment):
    """
        Proxy 클래스
        RealSubject 클래스인 Bank 클래스의 대리 객체이다.
    """
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()
