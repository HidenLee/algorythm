def func2(cost,depth):
    global maximum
    if cost > maximum:
        return
    if depth >= 12: 
        if maximum > cost:
            maximum = cost
        return
    func2(cost+min(daily*arr[depth],monthly),depth+1)
    func2(cost+tri,depth+3)


for test_case in range(1, int(input())+1):
    daily, monthly, tri, maximum = map(int, input().split())
    arr = list(map(int, input().split()))
    func2(0,0)
    print(f'#{test_case} {maximum}')