for tc in range(10):
    N = int(input()) # test 번호
    queue = list(map(int, input().split()))
    end = True
    while end:
        for i in range(1, 6):
            a = queue[0] - i
            if a <= 0:
                queue.pop(0)
                queue.append(0)
                end = False
                break
            queue.pop(0)
            queue.append(a)

    print(queue)