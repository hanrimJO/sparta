# a = 'spartacodingclub@gmail.com'
#
#
# def check_mail(s):
#     if a.find('@') > 1:
#         return True
#     return False
#
# def check_mail2(s):
#     b = s.split('@')
#     if len(b) == 2:
#         return True
#     return False


# 결과값
# print(check_mail(a))


# s = 'spartacodingclub@gmail.com'
#
#
# # 채워야하는 함수
# def get_mail(s):
#     ## 여기에 코딩을 해주세요
#     b = s.split('@')
#     print(b)
#     a = b[1].split('.')
#     print(a)
#     if len(a) == 2:
#         return a[0]
#     return False
#
#     # return s.split('@')[1].split('.')[0]
#
# # 결과값
# print(get_mail(s))


# a = ['사과', '감', '감', '배', '포도', '포도', '딸기', '포도', '감', '수박', '딸기']
#
#
# # 채워야하는 함수
# def count_list(fruits):
#     # 여기에 코딩을 해주세요
#     result = {}
#
#     for element in fruits:
#         if element in result:
#             result[element] += 1
#         else:
#             result[element] = 1
#     return result
#
#
#
#
# # 결과값
# print(count_list(a))

import random

def get_lotto():
    # lotto_list = {}
    # for i in range(1, 47):
    #     lotto_list.append(i)

    a = range(1, 47)
    b = random.sample(a, 6)

    b.sort()

    return b




print(get_lotto())

#아래와 같이 출력됩니다
