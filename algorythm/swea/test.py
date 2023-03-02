answer = 0
# visited = [False for _ in range(100)]
def func(n,lst):
    global answer
    N = len(lst)
    if N == 1: # bottom of recursion
        if n % lst[0] or n < lst[0]: # 불가능한 조합
            return 
        else:
            answer = answer + 1
            print(n,lst,answer)
            return  
    else:
        if n >= lst[-1]:
            if not n % lst[-1]:
            # if not n % lst[-1] and visited[N] == False:
                answer += 1
                # visited[N-1] = True
                # print(n,lst,answer)
            for i in range((n+lst[-1])//lst[-1]):
                func(n-i*lst[-1],lst[:-1])
    return answer
def solution(n, money):
    answer = 0
    money.sort()
    answer = func(n,money)
    
    
    # right = len(money) - 1
#     while True:
#         now = right
#         if money[right] > n:
#             right -= 1
#             continue
#         elif money[right] == n:
#             answer += 1
#             right -= 1
#             continue
#         else:
#             temp = n
#             for i in range(n // money[now] + 1):         
    return answer

print(solution(5,[1,2,4]))