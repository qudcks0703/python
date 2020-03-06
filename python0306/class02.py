class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def showInfo(self):        
        print("!!부모")

class baby(Person):
    def showInfo(self):
        print("난 애기")


aa=Person("33",33)
bb=baby("33",33)
aa.showInfo()
bb.showInfo()

# 두개 상속시 super(상속클래스,self).hello()
class Character:
    def __init__(self,hp,attack,defence):
        self.hp=hp
        self.attack=attack
        self.defence=defence
        print("캐릭터 생성함")

    def showInfo(self):
        pass
    def __del__(self):
        print("캐릭터 죽음")
    def __call__(self, *args, **kwargs):
        print("hp:", self.hp, "attack:", self.attack)
    def __getitem__(self, item):
        if item=="hp":
            print(self.hp)
bc=Character(10,20,30)
bc()
bc["z"]