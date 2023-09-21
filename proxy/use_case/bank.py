from payment import Payment


class Bank(Payment):
    """
        RealSubject 클래스
        구매자의 계좌에서 판매자의 계좌로 돈을 인출한다.
    """

    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card  # 카드 번호와 계좌 번호는 같다고 가정
        return self.account

    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return True

    def setCard(self, card):
        """
            Proxy는 setCard() 메소드를 사용해서 카드 정보를 은행에 전달한다.
        :param card:
        :return:
        """
        self.card = card

    def do_pay(self):
        """
            자금 상황에 따라 판매자에게 지불하는 역할을 하는 do_pay() 메소드를 구현하였다.
        :return:
        """
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False
