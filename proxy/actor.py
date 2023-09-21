class Actor(object):
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, "is occupied with current movie")  # 다른영화 촬영중

    def available(self):
        self.isBusy = False
        print(type(self).__name__, "is free for the movie")  # 출연 가능

    def getStatus(self):
        return self.isBusy
