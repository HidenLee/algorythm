for roop in range(10):
    T = int(input())
    array = []
    for _ in range(100):
        array.append(list(map(int,input().split())))
    x = array[-1].index(2)
    y = 100 - 1
    while y != 0:
        if x+1 < 100 and array[y][x+1] == 1:
            array[y][x] = 0
            x = x + 1
        elif x-1 > 0 and array[y][x-1] == 1:
            array[y][x] = 0
            x = x - 1
        elif y-1 > 0:
            y = y - 1
        else:
            print(f'#{T} {x}')
            break
