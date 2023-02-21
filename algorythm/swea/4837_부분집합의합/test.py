arr = [3,6,7]
n = len(arr)
temp = []
rst = []
for i in range(1<<n): # 1<<n == 2**n
    for j in range(n):
        if i & (1<<j):
            temp.append(arr[j])
    rst.append(temp)
    temp=[]
print(rst)              