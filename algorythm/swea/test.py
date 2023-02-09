import math
import time

start1 = time.time()


for N in [26,27,28,29]:
    # 여기서부터 실행시간이 궁금한 작업 실시
    a = [0] * 2**N
    for i in range(2**N):
        a[i] = i


    end1 = time.time()
    print(f"{N} {end1 - start1:.5f} sec")
    a = []
    start2 = time.time()


    # 여기서부터 실행시간이 궁금한 작업 실시
    a = []
    for i in range(2**N):
        a.append(i)


    end2 = time.time()
    print(f"{N} {end2 - start2:.5f} sec")
    a = []