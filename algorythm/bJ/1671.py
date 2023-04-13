def dfs(k, visited):
    for i in range(N):
        if eatable[k][i]:
            if visited[i] == -1:
                visited[i] = k
                visited[k] = i
                return True
            else:
                visited[i], temp = -1, visited[i]
                if dfs(i, visited):
                    visited[i] = k
                    visited[k] = i
                    return True
                visited[i] = temp
    return False

    

N = int(input())
eatable = [[False]*N for _ in range(N)]
sharks = []
for i in range(N):
    Str, Dex, Int = map(int,input().split()) # import new shark
    for idx, (oS, oD, oI) in enumerate(sharks):
        if Str == oS and Dex == oD and Int == oI: # if new shark is totally same with old one
            eatable[idx][i] = True
        else:
            if Str >= oS and Dex >= oD and Int >= oI: # if new shark is stroger than old one
                eatable[i][idx] = True
            if Str <= oS and Dex <= oD and Int <= oI: #if new shar is weaker than old one
                eatable[idx][i] = True
    sharks.append((Str,Dex,Int))

cnt = 0
for i in range(N):
    visited = [-1]*N
    if dfs(i,visited):
        cnt += 1
    print(visited)
print(cnt)
