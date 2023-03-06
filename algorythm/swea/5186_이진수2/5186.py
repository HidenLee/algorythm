bindict = {X:2**(-X) for X in range(1,13)}
bindict[13] = 10

T = int(input())
for test_case in range(1,T+1):
    rst = ''
    idx = 1
    N = float(input())
    while idx < 13:
        if N == 0:
            break
        if N >= bindict[idx]:
            rst += '1'
            N -= bindict[idx]
        else:
            rst +='0'
        idx += 1
    if N != 0:
        rst = 'overflow'
    print(f'#{test_case} {rst}')