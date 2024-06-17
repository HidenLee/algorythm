# https://www.acmicpc.net/problem/14916

def NumberTheory(x):
    a, b = divmod(x,5)
    if b % 2:
        a = a - 1
        b = (b // 2) + 3
        if a < 0:
            return(-1)
        else:
            return(a+b)
    else:
        return(a+b//2)

def Greedy(x):
    cnt = 0
    while(x>0):
        if not x % 5 :
            return cnt + x // 5
        x -= 2
        cnt += 1
    if x == 0:
        return cnt
    else:
        return -1

def dp(x):
    arr = [100000 for _ in range(max(6,x+1))]
    arr[2] = 1
    arr[4] = 2
    arr[5] = 1 
    for i in range(6,x+1):
        arr[i] = min(arr[i-2],arr[i-5])+1
    if arr[x] == 100000:
        return -1
    return arr[x]


x = int(input())
print(1,NumberTheory(x))
print(2,Greedy(x))
print(3,dp(x))