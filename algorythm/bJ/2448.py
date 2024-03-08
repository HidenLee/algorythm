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

N = int(input())
# blank = [' '*((i//3)*3) for i in range(N)]
# ans = ['' for _ in range(N)]
ans = ['','','']
ans[0] = '*****' 
ans[1] = ' * * ' 
ans[2] = '  *  ' 

K = 0
L = N // 3
while L != 1:
    L = L // 2
    K += 1

for _ in range(K):
    ans = stars(ans)



# for i in range(N):
#     if i >= N // 2:
#         ans[i] += blank[i]+ ans[i-N//2]
#     else:
        # ans[i] += (blank[i] + ans[i] + ' ' + blank[i])
pprint(ans, reversed=True)
