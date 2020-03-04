# try:
#     4/0
# except ZeroDivisionError as z:
#     print(z)
# finally:
#     print("빠이")
#pass 오류회피
#raise Error이름 에러 발생시키기
#dir 자체함수 보기
# #divmod 나머지와 몫을 구함
# # result1,result2=divmod(2,1)
# # print(result1,result2)
# # #eval 동적 으로 클래스 실행하기 위해사용
# # def positive(x):
# #     return x > 0
# # list1=[1,2,-3,-5,4]
# # print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
# # print(list(filter(positive,list1)))
# # #isinstance(object,class) instanceof
# # #map(함수,배열 및 반복가능자료형)
# # #sorted()
# # print(sorted([3,1,2]))
# import pickle
# f = open("test.txt", 'wb')
# data = {1: 'python', 2: 'you need'}
# pickle.dump(data, f)
# f.close()
# import pickle
# f = open("test.txt", 'rb')
# data1 = pickle.load(f)
# data2 = f.read()
# print(data1)
# print(data2)
# f.close()
#
# import webbrowser
# webbrowser.open("http://google.com")
#time
# import time
# print(time.localtime())
# print(time.time())
# print(time.ctime())
import calendar
print(calendar.calendar(2020))
# print(calendar.prcal(2015)) 둘다같음
#
# print(calendar.prmonth(2020,12))