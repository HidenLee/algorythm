
def solv():
    N, M = map(int,input().split())
    Num = [int(x) for x in str(N)]

    if len(Num) < 2 or not M:
        return N

    rst = set()
    target = sorted(Num,reverse=True)
    stack = [(Num,M)]
    while stack:
        K, depth = stack.pop()
        if K == target: 
            break
        if depth < 1:
            continue
        
        for i,j in [(i,j) for i in range(len(K)-1) for j in range(i+1,len(K))]:
            temp = K[:]
            temp[i], temp[j] = temp[j], temp[i]
            temp2 = int(''.join([str(x) for x in temp]))
            if temp2 not in rst:
                stack.append((temp,depth-1))
                rst.add(temp2)
    
    

    if stack or not rst:
        if depth%2 and len(Num)==len(set(Num)):
            target[-1], target[-2] = target[-2], target[-1]
        ans = int(''.join([str(x) for x in target]))
    else:
        ans = max(rst)
    return ans




T = int(input())
for test_case in range(1,T+1):
    print(f'#{test_case} {solv()}') 