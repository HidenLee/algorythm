T = int(input())
for test_case in range(1,T+1):
    E , N = map(int,input().split())
    lst = list(map(int,input().split()))
    lst = [(lst[idx*2],lst[idx*2+1]) for idx in range(E)]
    treedict = {X:[0,0] for X in range(1,E+2)}
    for parent, progeny in lst:
        if not treedict[parent][0]:
            treedict[parent][0] = progeny
        else:
            treedict[parent][1] = progeny
    rst = []
    stack = [N]
    while stack:
        N = stack.pop()
        if not N in rst:
            rst.append(N)
            for nxt in treedict[N]:
                if nxt:
                    stack.append(nxt)
                    
    print(f'#{test_case} {len(rst)}')