T= int(input())
for test_case in range(1,T+1):
    size = int(input())
    visited = [False for _ in range(size+1)]
    treedict = {}
    for i in range(1,size+1):
        treedict[i] = [0,[0,0]]
        if 2*i <= size:
            treedict[i][1][0] = 2*i
        if 2*i+1 <= size:
            treedict[i][1][1] = 2*i+1
    
    cnt = 1
    N = 1
    visited[0] = True
    while cnt < size + 1:
        if N and visited[treedict[N][1][0]] and not visited[N]: #자식이없거나 왼쪽은 처리했거나
            treedict[N][0] = cnt
            cnt += 1
            visited[N] = True
        else:
            for progeny in treedict[N][1]:
                if not visited[progeny]:
                    N = progeny
                    break
            else:
                for key, value in treedict.items(): 
                    if N in value[1]:
                        N = key
                        break
    print(f'#{test_case} {treedict[1][0]} {treedict[size//2][0]}')