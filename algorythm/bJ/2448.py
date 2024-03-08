#  https://www.acmicpc.net/problem/2448 stars11
N = int(input()) # N = 3x2^k
K = len(bin(N//3)) - 3

def pprint(lst,reversed=False):
    if reversed:
        for _ in range(-1,-len(lst)-1,-1):
            print(lst[_])
        return
    for _ in range(len(lst)):
        print(lst[_])

def stars(lst):
    length = len(lst)
    for i in range(length):
        temp = ' ' * length + lst[i] + ' ' * length
        lst[i] = lst[i] + ' ' + lst[i]
        lst.append(temp)
    return lst

ans = ['','','']
ans[0] = '*****' 
ans[1] = ' * * ' 
ans[2] = '  *  ' 


for _ in range(K):
    ans = stars(ans)

pprint(ans, reversed=True)
