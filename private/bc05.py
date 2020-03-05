# Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#
# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status2))
#
# words=['cat','window','me']
# del words[1]
# print(words)
# print(tuple(range(2,2)))
# for n in range(2,10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')
# #/ float #int
# for i in range(2,5):
#     for j in range(2,4):
#         print("안눙")
#     else:
#         print("하이")
#
# print()
#
# a=1
# b=2
# print(a,b)
# a,b=b,a
# print(a,b)

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        print(retries)
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
def foo(name, **kwds):
    return 'name' in kwds

kwd={"aa":3,"bb":4}

print(foo('name'))