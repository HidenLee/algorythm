#https://www.acmicpc.net/problem/5430
for _ in range(int(input())):
    cmd = input()
    M = int(input())

    # arr = [int(x) for x in list(input()) if x !="[" and x !="]" and x !=","]
    arr_input = input()[1:-1]
    if arr_input:
        arr = list(map(int, arr_input.split(',')))
    else:
        arr = []

    isReverse = False
    left = 0
    right = M-1
    error_flag = False
    for elm in cmd:
        if elm == "R":
            isReverse = not isReverse
        else: # elm == "D"
            if left <= right:
                if isReverse:
                    right -= 1
                else:
                    left += 1
            else:
                print("error")
                
                break
    else:
        result = arr[left:right+1]
        if isReverse:
            print("[" + ",".join(map(str, result[::-1])) + "]")
            # print(arr[left:right+1].reverse())
        else:
            print("[" + ",".join(map(str, result)) + "]")
            # print(arr[left:right+1])
        
    