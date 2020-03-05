# 성적처리 프로그램
menu = """
*** 글로벌 학원 ***
1.학생정보 출력
2.학생정보 입력
3.학생정보 수정
4.학생정보 삭제
5.학생정보 검색
6.총점,평균
7.종료
"""

scores = {"이형우": 100, "이근동": 99, "조소연": 98, "이근호": 97, "허웅": 96}


def view():
    #items 쓰면 딕셔너리 키벨류값받을수잇음
    for i, j in scores.items():
        print("이름 :%s 성적 %d" % (i, j))


def input1():
    name = input("학생이름 입력:")
    score = int(input("학생성적 입력:"))
    #추가하는방법
    #update 에 키형식으로넣기
    scores.update({name:score})
def modify():
    name = input("학생이름 입력")
    scores = input("수정할 점수 입력")
    scores[name] = scores

def delete():
    name = input("학생이름 입력")
    scores.__delitem__(name)
    print("삭제완료")

def search():
    name = input("학생이름 입력")
    score = scores.get(name)
    print(name)
    print(scores)
def avg():
    total = sum(scores.values())
    avg = total / scores.__len__()
    print(total)
    print(avg)

while True:
    print(menu)
    choose = int(input("메뉴선택:"))
    if choose == 1:
        view()
    elif choose == 2:
        input1()
    elif choose == 3:
        modify()
    elif choose == 4:
        delete()
    elif choose == 5:
        search()
    elif choose == 6:
        avg()
    elif choose == 7:
        print("종료")
        break
    else:
        print("다시선택")