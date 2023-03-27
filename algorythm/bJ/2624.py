def solution(n,money):
    money = sorted(money,reverse=True)
    lst = [0]*(n+1)
    lst[0] = 1
    for mon in money:    
        for i in range(n,-1,-1):
            for h in range(1,mon[1]+1):
                if 0 <=i-mon[0]*h:
                    lst[i] += lst[i-mon[0]*h]
    answer = lst[n]
    return answer   

T = int(input())
k = int(input())
money = [list(map(int,input().split()))for _ in range(k)]
print(solution(T,money))