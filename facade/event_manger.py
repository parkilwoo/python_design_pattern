
from caterer import Caterer
from florist import Florist
from hotelier import Hotelier
from musician import Musician
class EventManager(object):
    """
        결혼식에서 음식과 꽃 장식 등을 준비하는 업체와 조율하는 웨딩플래너(Facade)
    """
    def __init__(self):
        self.musician = None
        self.caterer = None
        self.florist = None
        self.hotelier = None
        print("Event Manager:: Let me talk to the folks\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()