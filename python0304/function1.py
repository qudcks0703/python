'''
def 함수명(매개변수1,매개변수2)
    실행문...
    return 값
'''
import random
print(random.randint(0, 1))
def showInfo():
    print("함수 호출")

showInfo()

def getNum():
    print("리턴있듬")
    return "hello"
#
# def plus(num1,num2):
#     return num1+num2
# def minus(num1,num2):
#     return num1-num2
# def multi(num1,num2):
#     return num1*num2
# def div(num1,num2):
#     return num1*num2
#
# print(plus(1,2))
# print(minus(1,2))
# print(multi(1,2))
# print(div(1,2))
#
# def func(num):
#     num=num+1
#     print(num)
# num=10
# #전역 변수를 사용하려면 global 변수명 을앞에붙여줘야함
# print(num)
