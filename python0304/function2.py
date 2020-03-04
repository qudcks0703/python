
#

# # login(id,pw)
# # def login(a,d):
# #     global id
# #     print(id)
# #     id=id+1
# #     print(id)
# # id=3
# # login(1,1)
# # print(id)
# # print(id,"zzz")
#
# def sum(*num):
#     tot=0
#     for i in num:
#         tot +=i
#     return tot
#일반 파라미터 *파미터 초기값파라미터
#초기값있는 파라미터는 값=이렇게보내줘야함함print(sum(10,20))
# def calc(op, *num, age=0):
#     if op == "sum":
#         tot = 0
#         for i in num:
#             tot += i
#     elif op == "mul":
#         tot = 1
#         for i in num:
#             tot *= i
#     elif op == "sub":
#         tot = num[0]
#         for i in num:
#             tot -= i
#     print(age)
#     return tot
#
# print(calc('sum', 1,2,3,4,5))
#print("a","b","c",sep="-",end="")
def login(id,pw):
    if(id=="python"):
        if(pw=="1234"):
            print("합격")
            return 1
        else:
            print("존재하지 않는 비밀번호입니다.",end="")
            return 0
    else:
        print("존재 하지않는 아이디입니다.")
        return 0

def start():
    print("로그인 해라 임마야 ㅋㅋ")
    id=input("아이디 입력하세요")
    pw=input("패스워드 입력하세요")
    result=login(id,pw)
    money=0;
    while True:
        if result==1:
            print("--------------")
            print("1.입금")
            print("2.출금")
            print("3.잔액 조회")
            print("4.계좌이체")
            print("5.종료")
            print("--------------")
            select=int(input("몇번 할꺼냐"))
        if select==1:
            money+=float(input("얼마 넣을건데 ㅋㅋ 십년아"))
        elif select==2:
            money-=float(input("얼마 뺄건데 ㅋㅋ 십년아"))
        elif select==3:
            print("너 지금 %d원 있다" %money)
        elif select==4:
            print("너 지금 %d원 있다" %money)
        elif select==5:
            print("끄지라")
            return
start()
db_id = "java"
db_pw = "1111"

menu = ["1.입금","2.출금","3.잔액 조회","4.계좌 이체","5.종료"]
my_money = 100000

print("*** 글로벌 은행 ATM ***")
i = 0
while True:
    if i == 3:
        print("아이디와 패스워드 3회 오류. 프로그램이 종료됩니다.")
        break
    if i == 5:
        print("이용해주셔서 감사합니다.")
        break

    id = input("아이디를 입력하세요")
    pw = input("비밀번호를 입력하세요")

    if db_id != id or db_pw != pw:
        print("아이디와 비밀번호를 확인하세요")
        i += 1
    elif db_id == id and db_pw == pw:
        while True:
            print(menu[0])
            print(menu[1])
            print(menu[2])
            print(menu[3])
            print(menu[4])
            print()
            menuNum = input("번호를 선택하세요.")
            if menuNum == "1": #입금
                print(menu[0])
                put = int(input("입금하실 금액을 입력하세요."))
                my_money += put
                print("총 잔액 :", my_money)
                print()
            elif menuNum == "2": #출금
                print(menu[1])
                put = int(input("출금하실 금액을 입력하세요."))
                if put > my_money:
                    print("잔액이 부족합니다.")
                    print()
                else:
                    my_money -= put
                    print("총 잔액 :", my_money)
                    print()
            elif menuNum == "3":  # 잔액조회
                print(menu[2])
                print("총 잔액 :", my_money)
                print()
            elif menuNum == "4":  # 계좌이체
                print(menu[3])
                print(input("이체할 계좌번호를 입력하세요."))
                send = int(input("이체할 금액을 입력하세요"))
                if send > my_money:
                    print("잔액이 부족합니다.")
                    print()
                else:
                    my_money -= send
                    print("총 잔액 :", my_money)
                    print()
            elif menuNum == "5":  # 종료
                print(menu[4])
                print("프로그램이 종료됩니다.")
                print()
                i = 5
                break