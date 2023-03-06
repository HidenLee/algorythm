T = int(input())
for test_case in range(1,T+1):
    N, num = input().split()
    rst = ''
    for elm in num:
        binelm = str(bin(int(elm,base=16)))[2:]
        while len(binelm) != 4:
            binelm = '0' + binelm
        rst += binelm
    print(f'#{test_case} {rst}')