T = 10
for test_case in range(1,T+1):
    size = int(input())
    treedict = {}
    visited = [False for _ in range(size+1)]
    for _ in range(size):
        progeny = []
        parent, alp, *progeny = (f(s) for f,s in zip([int,str,int,int],input().split()))
        treedict[parent] = (alp,progeny)
    rst =''
    N = 1
    while len(rst) != size:
        now = treedict[N][0]
        print(rst,now)
        temp = [x for x in treedict[N][1] if not visited[x]] # 자식노드중 출력되지 않은 것
        if (len(temp) == 0 or (len(temp)==1 and len(treedict[N][1])==2)) and not visited[N]: #자식이없거나 왼쪽은 처리했거나
            rst += now
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
    print(f'#{test_case} {rst}')