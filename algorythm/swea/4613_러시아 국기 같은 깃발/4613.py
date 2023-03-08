T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())
    Entire = [input() for _ in range(N)]
    rst = float('inf')
    for Bottom in range(2, N):
        for Top in range(1, Bottom):
            Head = Entire[:Top]
            Tail = Entire[Bottom:]
            Body = Entire[Top:Bottom]
            cnt = 0
            for row in Head:
                for elm in row:
                    if elm != 'W':
                        cnt += 1
            for row in Tail:
                for elm in row:
                    if elm != 'R':
                        cnt += 1
            for row in Body:
                for elm in row:
                    if elm != 'B':
                        cnt += 1
            if rst > cnt:
                rst = cnt
    print(f'#{test_case} {rst}')
