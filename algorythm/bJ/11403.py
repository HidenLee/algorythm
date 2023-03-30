def func1(mat1): #product itself and merge with original // 새로운 매트릭스를 만들어야해서 효율적이지 못한듯
    mat2 = [[int(any([mat1[y][x]]+[(mat1[y][n]*mat1[n][x]) for n in range(N)]))for x in range(N)] for y in range(N)]
    return mat2


def func2(mat1):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if mat1[i][k]*mat1[k][j]: 
                    mat1[i][j] = 1
                    break
    return mat1

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
for _ in range(N):
    lst = func1(lst)
for _ in range(N):
    print(*lst[_])