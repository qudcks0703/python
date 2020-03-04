from builtins import float
#import하면 함과동시에 거기있는게 실행되버림
#위에를 안하려면 if __name__ == "__main__"
#import bc03
#from bc01 import add,sub *
class Cal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdata(self,first,second):
        self.first=first
        self.second=second #a.second
    def add(self):
        result=self.first+self.second
        return result
a=Cal(3,4)
print(a.add())

class Cal2(Cal):
    pass
b=Cal2(3,6)
print(b.add())

