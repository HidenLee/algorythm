# #https://www.acmicpc.net/problem/15653
# from collections import deque
from copy import deepcopy


# def pprint(lst):
#     for slst in lst:
#         print(slst)
#     print()




# def gravity(table, d):
#     # -1:fail, 0:keep, 1:success
#     table, Bflag, Bmoved = move(table, d,'B')
#     if Bflag:
#         return table, -1, False
#     else:
#         table, Rflag, Rmoved = move(table, d,'R')
#         table, Bflag, buffer = move(table, d,'B')
#         Bmoved = any([Bmoved,buffer])
#         if Bflag:
#             return table, -1, False
#         elif Rflag:
#             return table, 1, True
#         else:
#             if any([Bmoved, Rmoved]):
#                 return table, 0, True
#             else:
#                 return table, 0, False


# def move(table, diridx, color): #-> table, isgoaled, ismoved
#     global O
#     if color == 'R':
#         x, y = table[-2][0], table[-2][1]
#     else: # B
#         x, y = table[-1][0], table[-1][1]

#     #[R,D,L,U]
#     dirdict = [(1,0),(0,1),(-1,0),(0,-1)]
    
#     table[y][x] = '.'

#     nx, ny = x , y 
#     while table[ny + dirdict[diridx][1]][nx + dirdict[diridx][0]] in ['.','O'] :
#         nx += dirdict[diridx][0]
#         ny += dirdict[diridx][1]
#         if nx == O[0] and ny == O[1]:
#             if color == 'R':
#                 table[-2][0], table[-2][1] = nx, ny
#             else: # B
#                 table[-1][0], table[-1][1] = nx, ny
#             return table, True, True
#     table[ny][nx] = color

#     if color == 'R':
#         table[-2][0], table[-2][1] = nx, ny
#     else: # B
#         table[-1][0], table[-1][1] = nx, ny
    
#     if (x, y) == (nx, ny):
#         return table, False, False
#     return table, False, True



# N, M = map(int,input().split())
# table = [list(input()) for _ in range(N)]
# for y in range(1,N-1):
#     for x in range(1,M-1):
#         if table[y][x] == 'R':
#             R = [x,y]
#         elif table[y][x] == 'B':
#             B = [x,y]
#         elif table[y][x] == 'O':
#             O = [x,y]
# table.append(R)
# table.append(B)



# dirkeyword = ['R','D','L','U']

# isvisited = set([])
# dq = deque([(table,0,'0'),(table,1,'1'),(table,2,'2'),(table,3,'3')])
# ispass = False
# while dq:
#     maze, diridx, route = dq.popleft()
#     # print(route)
#     isvisited.add(route)
#     # if len(route) > 10:
#     #     continue
#     nxt = deepcopy(maze)
#     nxt, status, ismoved = gravity(nxt,diridx)
#     # print("route: ",route)
#     # pprint(nxt)
#     if status == 1:
#         ispass = True
#         print(len(route))
#         # print(''.join([dirkeyword[int(X)] for X in route]))
#         # print('congraturation!!!!!!',route)
#         break
#     elif status == -1:
#         continue
#         # print('faillll',route)
#     else:
#         for d in range(4):
#             if ismoved and d not in [diridx, (diridx+2)%4] and route+str(d) not in isvisited:
#                 dq.append((nxt,d,route+str(d)))

# if not ispass:
#     print(-1)

from collections import deque

def gravity(table, d):
    table, Bflag, Bmoved = move(table, d, 'B')
    if Bflag:  # Blue reaches the hole (fail)
        return table, -1, False
    table, Rflag, Rmoved = move(table, d, 'R')
    table, Bflag, buffer = move(table, d, 'B')
    Bmoved = any([Bmoved, buffer])
    if Bflag:
        return table, -1, False
    elif Rflag:
        return table, 1, True  # Red reaches the hole (success)
    return table, 0, Bmoved or Rmoved

def move(table, diridx, color):
    global O
    if color == 'R':
        x, y = table[-2][0], table[-2][1]
    else:  # B
        x, y = table[-1][0], table[-1][1]

    dirdict = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    table[y][x] = '.'

    nx, ny = x, y
    while table[ny + dirdict[diridx][1]][nx + dirdict[diridx][0]] in ['.', 'O']:
        nx += dirdict[diridx][0]
        ny += dirdict[diridx][1]
        if nx == O[0] and ny == O[1]:
            if color == 'R':
                table[-2][0], table[-2][1] = nx, ny
            else:
                table[-1][0], table[-1][1] = nx, ny
            return table, True, True
    table[ny][nx] = color

    if color == 'R':
        table[-2][0], table[-2][1] = nx, ny
    else:
        table[-1][0], table[-1][1] = nx, ny

    return table, False, (x != nx or y != ny)

N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]
for y in range(1, N-1):
    for x in range(1, M-1):
        if table[y][x] == 'R':
            R = [x, y]
        elif table[y][x] == 'B':
            B = [x, y]
        elif table[y][x] == 'O':
            O = [x, y]
table.append(R)
table.append(B)

visited = set()
dq = deque([(table, 0, '0'), (table, 1, '1'), (table, 2, '2'), (table, 3, '3')])
found_solution = False

while dq:
    maze, diridx, route = dq.popleft()
    # if len(route) > 10:  # Limit moves to 10
    #     continue
    state_key = (tuple(maze[-2]), tuple(maze[-1]), diridx)
    if state_key in visited:
        continue
    visited.add(state_key)

    nxt, status, moved = gravity(deepcopy(maze), diridx)
    if status == 1:  # Success
        print(len(route))
        found_solution = True
        break
    if status == -1:  # Failure (Blue marble in hole)
        continue
    if moved:  # Only move further if something moved
        for d in range(4):
            if d != diridx and d != (diridx + 2) % 4:
                dq.append((nxt, d, route + str(d)))

if not found_solution:
    print(-1)
