def mergesort(arr,cnt): # time out
    length = len(arr)
    if length == 1:
        return arr, cnt
    middle = length // 2
    left, cnt = mergesort(arr[:middle],cnt)
    right, cnt = mergesort(arr[middle:],cnt)
    if left[-1] <= right[0]:
        left.extend(right)
        return left, cnt
    if left[-1] > right[-1]:
        cnt += 1
    for relm in right:
        for idx , lelm in enumerate(left):
            if lelm < relm and (idx + 1 == len(left) or relm < left[idx+1] ):
                left.insert(idx+1,relm)
                break
        else:
            left.insert(0,relm)
    return left, cnt
    
def mergesort2(arr,cnt): # 채택
    length = len(arr)
    if length == 1:
        return arr, cnt
    middle = length // 2
    left, cnt = mergesort2(arr[:middle],cnt)
    right, cnt = mergesort2(arr[middle:],cnt)
    if left[-1] <= right[0]:
        left.extend(right)
        return left, cnt
    if left[-1] > right[-1]:    
        cnt += 1
    left.extend(right)
    left.sort()
    return left, cnt


def mergesort3(lst,cnt): # 과정에 문제가 있음, 2개씩묶으면 길이=(홀수*2)의 꼴에서 문제가 생김
    temp = lst
    middle = sorted(lst)[N//2]
    while True:
        arr = temp
        temp = []
        if len(arr) == 1:
            break
        for L,R in [(arr[2*i],arr[2*i+1]) for i in range(len(arr)//2)]:
            if L > R:
                cnt+=1
                temp.append(L)
            else:
                temp.append(R)
    return middle, cnt





def is_power_of_two(n):
    return (n != 0) and (n & (n-1) == 0)

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    rst, cnt = mergesort(lst,N)
    print(f'#{test_case} {rst} {cnt}')
    # print(f'#{test_case} {rst[N//2]} {cnt}')