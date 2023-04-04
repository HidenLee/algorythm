from collections import deque

def func2(queue):
    if queue[0] == queue[1] and queue[1] == queue[2]:
        return 10000 + queue[0]*1000
    
    if queue[0] == queue[1]:
        return 1000 + queue[0]*100
    if queue[1] == queue[2]:
        return 1000 + queue[1]*100
    if queue[2] == queue[0]:
        return 1000 + queue[2]*100
    
    return max(queue)*100



def func1(queue,depth):
    if depth == N:
        print(func2(queue))
        return func2(queue) / 6
    for i in range(1,7):
        queue[0], queue[1], queue[2], temp = queue[1], queue[2], i, queue[0]
        value = max(func1(queue,depth+1)/6,func2(queue))
        queue[0], queue[1], queue[2] = temp, queue[0], queue[1]

    return value / 6





N = int(input())
queue = deque([0,0,0])
print(func1(queue,0))