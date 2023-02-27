codedict = {'0001101':0, '0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    lst = [list(input()) for _ in range(N)]
    code = []
    for row in lst:
        if '1' in row:
            invertrow = row[::-1]
            ridx = invertrow.index('1')
            barcord = row[-56-ridx:-ridx] 
            break
    
    for idx in range(0,56,7):
        code.append(codedict[''.join(barcord[idx:idx+7])])
    rst = 0
    for idx in range(8):
        if idx%2:
            rst += code[idx]
        else:
            rst += code[idx]*3
    sumnum = 0
    if not rst % 10:
        sumnum = sum(code)
    print(f'#{test_case} {sumnum}')