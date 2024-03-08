def pprint(lst):
    for slst in lst:
        print(slst)


def solution(m, n, puddles):
    table = [[0]*m for _ in range(n)]
    for x in range(m):
        if [x+1,1] in puddles:
            break
        table[0][x] = 1
    for y in range(n):
        if [1,y+1] in puddles:
            break
        table[y][0] = 1
    for y in range(1,n):
        for x in range(1,m):
            if [x+1,y+1] in puddles:
                continue
            table[y][x] = table[y-1][x] + table[y][x-1]
            
    answer = table

    return answer

# pprint(solution(5,4,[[1,2],[2,1]]))

