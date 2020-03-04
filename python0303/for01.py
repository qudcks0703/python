# for i in range(10):
#     print(i)
# lst={1,2,3,4,5}
# for i in lst:
#     print(i)
# lst1=(1,2,3,4,5)
# print("--------------")
#     #한칸식 1~ 11
# for i in range(1,11):
#     print(i)
#     #두칸식 1~11
# for i in range(1,11,2):
#     print(i)
#
scores = [90,45,66,10,49]
for i in scores:
    if i>60:
        print("합격")
    else:
        print("불합격")
for i in range(11):
    if i%2==1:
        print(i)
        sum=0
for i in range(10,100,2):
    sum+=i
    if i==100:
        print(sum)
for i in range(10,100,10):
    print(i)
input1=int(input("몇단 ?"))
for i in range(1,9):
    print("2 X %d=2*%d" %(i,i))
for i in range(1,9):
    print("%d X %d=%d" %(i,input1,i*input1))
for i in range(2, 10):
    for j in range(1, 9):
        print("%d X %d=%d" %(i,j,i*j))
lst =[-1,-20,45,70,-40]
plusCnt=0
minusCnt=0
for i in lst:
    if i>0:
        plusCnt+=1
    else:
        minusCnt+=1
print(plusCnt)
print(minusCnt)