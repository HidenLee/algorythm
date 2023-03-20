def findparent(a,k):
    temp = a % k
    if temp <= 1: # 1, 0
        return a // k
    else:
        return (a + (k-temp)) // k
["" if True  else "" for _ in range()]
N, K, Q = map(int,input().split())
for _ in range(Q):
    x, y = map(int,input().split())
    xparents = [x]
    yparents = [y]
    while xparents[-1] != 1:
        xparents.append(findparent(xparents[-1],K))
    while yparents[-1] != 1:
        temp = findparent(yparents[-1],K)
        yparents.append(temp)
        if temp in xparents:
            print(xparents.index(temp)+len(yparents)-1)
            break
    if y == 1:
        print(len(xparents)-1)
