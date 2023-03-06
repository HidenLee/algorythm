import sys

sys.stdin = open('algorythm\\swea\\1242_암호코드 스캔\\sample_input (15).txt','r')
sys.stdout = open('output.txt','w')

#reference
codedict = {'0001101':0, '0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}

#input
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    lst = [input().strip() for _ in range(N)]
    
    #initializing
    sumnum = 0
    codelist = set()

#preprocessing
    lst = sorted(set(lst))[1:]    
    for case in lst:
        binrow = ''
        for elm in case:
            if elm:
                binnum = bin(int(elm,16))[2:] #0x1234... => 1234...
                while len(binnum) % 4: # 100 => 0100
                    binnum = '0' + binnum
                binrow += binnum         
        binrow = binrow.rstrip('0')
        while len(binrow) % 56:
            binrow = '0' + binrow

        #solution roop
        while len(binrow) > 0:
        #find thickness
            ratio = [1,1,1,1] 
            previous = binrow[-1]  # 우측 암호부터 탐색
            diffcount = 0
            idx = -2
            while diffcount <= 3: 
                if binrow[idx] == previous: # N:M:K:L 비율을 세웠을때 가장 작은 숫자가 두께 (각 코드의 기본비율에서 가장 작은갯수는 항상 1이기 때문)
                    ratio[diffcount] += 1
                else: 
                    diffcount += 1
                previous = binrow[idx]
                idx -= 1
            
            thickness = min(ratio)
                    
            targetcode = binrow[len(binrow)-thickness*56:]
            binrow = binrow[:len(binrow)-thickness*56].rstrip('0')
            eigencode = [targetcode[x] for x in range(len(targetcode)) if not x % thickness]
            codelist.add(''.join(eigencode))
            
            
#decode
    for code in codelist:
        temp = []
        for idx in range(0,56,7):
            if ''.join(code[idx:idx+7]) in codedict.keys(): 
                temp.append(codedict[''.join(code[idx:idx+7])])
        # code validation
        if len(temp) == 8:
            valid = sum([temp[x] for x in range(8) if x % 2]) + sum([temp[x] for x in range(8) if not x % 2]) * 3
            if not valid % 10:
                sumnum += sum(temp)            
    print(f'#{test_case} {sumnum}')
    
    
    
    
