import sys
sys.stdout = open('input.txt','w')



print(100, 100, 100)

for _ in range(10000):
    a = [0 for _ in range(100)]
    print(*a)
