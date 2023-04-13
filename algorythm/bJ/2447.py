def pprint(lst):
    for _ in range(len(lst)):
        print(lst[_])
        
def stars(lst):
    length = len(lst)
    temp = []
    #Head
    for i in range(length):
        temp.append(lst[i]*3)
    
    #Body
    for i in range(length):
        piecelen = len(lst[i])
        temp2 = lst[i] + " " * piecelen + lst[i]
        temp.append(temp2)
    #Tail
    for i in range(length):
        temp.append(lst[i]*3)
    lst = temp
    return lst

N = int(input())
ans= ['*']

K = 0
while N != 1:
    N = N // 3
    K += 1
for _ in range(K):
    ans = stars(ans)
pprint(ans)