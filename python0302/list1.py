#list
#변수명 =[요소,1,요소2,요소3]

# nums=[1,2,3,4,5]
# print(nums)

# num3=[1,2,3,[4,5,6],7]
#
# print(num3[3][0])
# print(num3[2])
# print(num3[4])
num4=[1,2,3,["a","b","c"],4,5]

print(num4[2:5])
print(num4[3][0:2])
print([num4[2],num4[3],num4[4]])
print([num4[3][0],num4[3][1]])

lst=[1,2,3]
lst[1]=['a','b','c']
print(lst)
lst=[1,2,3]
lst[1:2]=['a','b','c']
print(lst)
lst=[1,2,3]
lst[1]='a','b','c'
print(lst)
print(lst[1][1])
lst=[1,2,3]
lst1=[4,5,6]
#맨뒤에 추가
lst.append([1,2])
#확장시킴
lst1.extend(lst)
print(lst1)
lst=[1,2,3]
#자리추가하기
lst.insert(1,10)
print(lst)
#자리지우기 인덱스아니ㅏㅁ값임
lst.remove(10)
print(lst)