from stock_exchange.order import Order
class Wizard:
    """
    인스톨러를 구현한 클래스
    preferences() 메소드를 통해 각 단계에서 사용자가 선택한 정보를 저장한다.
    execute() 메소드를 통해 저장된 설정을 불러오고 설치를 시작한다.
    """

    def __init__(self, src, rootdir):
        self.choices: list[dict] = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.rootdir)
            else:
                print("No Operation")

if __name__ == '__main__':
    ## 클라이언트 코드
    wizard = Wizard('python3.10.gzip', '/usr/bin')
    ## 사용자는 파이썬을 선택
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()