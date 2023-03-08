def pprint(table):
    '''
    디버깅을 위해 만든 array출력 함수
    '''
    for row in table:
        print(row)
    print()



n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

r = n-1
c = n-1
arr[r][c] = 1

num = 2
while num <= n ** 2:
    if c % 2 == 1:
        r -= 1
        arr[r][c] = num
        num += 1
        if r == 0:
            c -= 1
            arr[r][c] = num
            num += 1
    else:
        r += 1
        arr[r][c] = num
        num += 1
        if r == n-1:
            c -= 1
            arr[r][c] = num
            num += 1


pprint(arr)