N, K = map(int,input().split())
arr = input()
isHam =[False]*(N)
ans = 0
for idx, elm in enumerate(arr):
    if elm == "H":
        isHam[idx] = True
    else:
        for jdx in [x for x in range(idx-K,idx+K+1) if x != idx and 0<= x <N]:
            if isHam[jdx]:
                isHam[jdx] = False
                ans += 1
print(ans)