from abc import ABCMeta, abstractclassmethod
# ABCMeta는 파이썬에서 특정 클래스를 Abstract로 선언하는 특수 메타 클래스

class Animal(metaclass = ABCMeta):

    @abstractclassmethod
    def do_say(self): pass

class Dog(Animal):

    def do_say(self):
        print("멍!멍!")

class Cat(Animal):

    def do_say(self):
        print("야옹~야옹~")

# forest factory 정의
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()
    
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)