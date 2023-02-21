'''
책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.
'''

# def binsearch(P,target):
#     cnt, left, right, page = 0, 1 , P, -1
#     while page + 1 < target:
#         if page < 0:
#             page = int(P/2)
#         else:
#             if P == target:
#                 if -1 <= page-P <= 1:
#                     break
#             cnt += 1
#             page = int((left+right)/2)
#             if page < target:
#                 left = page
#             elif page > target:
#                 right = page
#             else:
#                 break
#     return cnt

# 이진탐색


def binsearch2(P,target):
    cnt, left, right = 0, 1 , P 
    page = int((left+right)/2)
    temp = 0
    while True: 
        if temp == int((left+right)/2):
            break
        page = int((left+right)/2)
        temp = page
        if page <= target:
            left = page
        elif page >= target:
            right = page
        if page == target:
            break
        cnt += 1
    return cnt       

T = int(input())
for test_case in range(1,T+1):
    P, Pa, Pb = map(int,input().split())
    result = []
    result.append(binsearch2(P,Pa)) 
    result.append(binsearch2(P,Pb)) 
    if result[0] < result[1]:
        print(f'#{test_case} A')
    elif result[0] > result[1]:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')