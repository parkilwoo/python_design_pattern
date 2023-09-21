from debit_card import DebitCard


class You:
    """
        Client 클래스
    """

    def __init__(self):
        """
            프록시(DebitCard)를 호출하고 생성하는 메소드
        """
        print("YOU:: Lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        """
            내부적으로 프록시의 메소드를 호출해 금액을 지불한다.
        :return:
        """
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        """
            결제가 성공하면 매직메소드를 호출해 Print한다.
        :return:
        """
        if self.isPurchased:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You:: I should earn more :(")


you = You()
you.make_payment()
