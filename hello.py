def oddeven(num):  # oddeven이라는 이름의 함수를 정의한다. num을 변수로 받는다.
    if num % 2 == 0:  # num을 2로 나눈 나머지가 0이면
        return True  # True (참)을 반환한다.
    else:  # 아니면,
        return False  # False (거짓)을 반환한다.


def checkbob(name):
    if name == 'bob':  # name이 'bob'이면 True를, 아니면 False를 반환해라
        return True
    else:
        return False


print(oddeven(11))


# if 1 == 1:
#     return
#
# if True:
#     return
#
# if not None:
#     return

def allsum(mylist):  # allsum이라는 이름의 함수를 정의한다. mylist를 변수로 받는다.
    sum = 0  # sum이라는 변수를 0으로 일단 정의한다.
    for i in mylist:  # mylist의 원소들을 처음부터 돌면서, i에 넣어 아래 식을 수행한다.
        sum = sum + i  # sum에다 직전 sum에다 원소를 더한 값을 넣는다.
    return sum  # 최종 sum을 반환한다.


sth_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(allsum(sth_list))  # 45

# 또는, 자동으로 리스트를 생성해주는 파이썬 자체함수 range(숫자)를 사용하면,

sth_list_2 = range(10)  # [0,1,2,3,4,5,6,7,8,9] 와 같음
print(allsum(sth_list_2))  # 45


