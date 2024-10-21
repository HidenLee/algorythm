_ = input()
dic = {x : True for x in list(map(int,input().split()))}
_ = input()
for i in list(map(int,input().split())):
    if i in dic:
        print(1)
    else:
        print(0)
    