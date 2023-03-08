T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    C = [0] * 31
    rst = float('inf')

    for num in list(map(int, input().split())):
        C[num] += 1
    carrots = [C[num] for num in range(31) if C[num]]

    for top in range(1, len(carrots)-1):
        for bottom in range(top+1, len(carrots)):
            box1 = box2 = box3 = 0
            for idx in range(len(carrots)):
                if idx < top:
                    box1 += carrots[idx]
                elif top <= idx < bottom:
                    box2 += carrots[idx]
                else:
                    box3 += carrots[idx]
            if box1 * box2 * box3 == 0 or box1 > N//2 or box2 > N//2 or box3 > N//2:
                continue
            else:
                temp = max(box1, box2, box3) - min(box1, box2, box3)
                if rst > temp:
                    rst = temp
    if rst == float('inf'):
        rst = -1
    print(f'#{test_case} {rst}')