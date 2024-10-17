D, N = map(int,input().split())
arr = list(map(int,input().split()))

pre = arr[0]
for idx in range(1,D):
    arr[idx] = min(pre,arr[idx])
right = D
left = 0

for pizza in list(map(int,input().split())):
    while left < right:
        mid = (left+right) // 2
        if arr[mid] < pizza:
            left = mid + 1
        else:
            right = mid 
    right = left - 1
    print(right)
    

    # while idx < D and pizza <= arr[idx] :
    #     idx += 1
    # right = idx
if right < 0 :
    print(0)
else:
    print(right + 1)
