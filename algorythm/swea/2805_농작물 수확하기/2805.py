T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    garden = [list(input()) for _ in range(N)]
    rst = 0
    print(garden)
    middle = N // 2
    for i in range(-middle,middle+1):
        for j in range(-abs(middle-abs(i)),(abs(middle-abs(i))+1)):
            rst += int(garden[middle+i][middle+j])
    print(f'#{test_case} {rst}')