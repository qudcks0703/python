import random
# #범위지정 randint
# num=random.randint(1,5)
# num1=random.random
# print(num)
# #random() 그냥랜덤 0~1 우리가아는 랜덤
# print(random.random())
# #random.randrange(범위)
# list=[10,20,30,40,50]
# #리스트 골라줌
# num2=random.choice(list)
# print(num2)
# #갯수만큼 빼기
# num3=random.sample(list,3)
# print(num3)
# #셔플 하기
# random.shuffle(list)
# print(list)

num=random.randint(0,1)
print(num)
if num==1:
    print("뒷면")
else:
    print("앞면")

num1=random.randint(0,2)
my=int(input("가위(0) 바위(1) 보(2) "))# 2 0한테 지고 1한테 이기고 2에 비김
print("컴퓨터는? %d" %num1)
if my==0:
    if num1==1:
        print("이김")
    elif num1==2:
        print("짐")
    else:
        print("비김")
elif my==1:
    if num1==0:
        print("이김")
    elif num1==2:
        print("짐")
    else:
    print("비김")
else
    if num1==1:
        print("이김")
    elif num==0:
        print("짐")
    else:
     print("비김")
