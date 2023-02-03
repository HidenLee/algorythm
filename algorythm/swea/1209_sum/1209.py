import sys
sys.stdin = open('input.txt','r')

for test_case in range(10):
    T = int(input())
    sumlist = []
    array = []
    temptoleftup = 0
    temptorigntdown = 0
    for roop in range(100):
        array.append(list(map(int,input().split())))
        sumlist.append(sum(array[-1]))   
    for idx1 in range(100):
        temp = 0
        temptorigntdown += array[idx1][idx1]
        temptoleftup += array[99-idx1][idx1]
        for idx2 in range(100):
            temp += array[idx2][idx1]
        sumlist.append(temp)
    sumlist.append(temptorigntdown)
    sumlist.append(temptoleftup)
    print(f'#{T} {max(sumlist)}')        