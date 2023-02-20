while True:
    try:
        tc = int(input())
        lst = list(map(int,input().split()))
        i = 1
        while True:
            temp = lst.pop(0)
            lst.append(temp - i)
            i %= 5
            i += 1
            if lst[-1] <= 0:
                lst[-1] = 0
                break
        print('#', end= '')
        print(tc, end= ' ')
        print(*lst) 
    except:
        break