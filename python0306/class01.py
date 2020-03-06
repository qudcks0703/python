class Person:
    name=""
    age=0
    gender=""
    blood=""
    jumin=""

    def showInfo(self):
        print("이름:%s" %self.name)

class Tv:
    power=False
    color="white"
    channel=1
    num1=1
    def __init__(self,num):
        self.num=num
    def onOff(self,num):
        self.num=num
        if self.power:
            self.power=not self.power
        else:
            self.power=not self.power

# tv=Tv()
# tv.onOff(4)
# print(tv.num)
# print(tv.num1)
class Game:

    def __init__(self,name,level):
        self.name=name
        self.level=level

    def die(self):
        print("으억")

    @staticmethod
    def message():
        print("ㅎㅇ")

    @classmethod
    def update(cls,value):
        cls.discount=value
class Test:
    num=0
    @staticmethod
    def add(x,y):
        return x+y
    @classmethod
    def test(cls,value):
        cls.value=value
        cls.num=value


bc=Game("qudcks",45)
so=Game("tmddh",20)
print(bc.name,bc.level)
so.message()
t=Test()
print(t.test(3))
print(t.value)
print(t.num)
