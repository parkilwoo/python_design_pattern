from event_manger import EventManager


class You(object):
    """
        실제 결혼을 진행하는 사람, 모든 준비를 웨딩플래너에게 맡긴다.(Client)
    """
    def __init__(self):
        print("YOU:: Whoa! Marriage Arrangements??!!!")

    def askEventManager(self):
        print("YOU:: Let's Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("YOU:: Thanks to Event Manager, all preparations done! Phew!")


you = You()
you.askEventManager()
