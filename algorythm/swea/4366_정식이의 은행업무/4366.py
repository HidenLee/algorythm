def func1(): # 3진법 최대 40자리나옴 3**40 ->메모리 펑
    for _ in range(1,int(input())+1):
        binnum=ternum=0
        binary = input()
        ternary = input()

        for idx, num in enumerate(binary[::-1]): # 2진변환
            binnum += (2**idx)*int(num)
        for idx, num in enumerate(ternary[::-1]): # 3진변환
            ternum += (3**idx)*int(num)

        bindiff = [2**x*y for x in range(len(binary)) for y in [-1,0,1]] 
        bindiff = list(set(bindiff))
        terdiff = [3**x*y for x in range(len(ternary)) for y in [-2,-1,0,1,2]]
        terdiff = list(set(terdiff))
        print(bindiff,terdiff)
        for num in [x for x in range(2**(len(binary)-1),2**len(binary)+1) if 3**(len(ternary)-1)<=x<3**len(ternary)]: # 같은 자릿수임
            if abs(num-binnum) in bindiff and abs(num-ternum) in terdiff:
                print(f'#{_} {num}')   
                break
        else:
            print(-1)



def func3(n,string,decnum):
    arr = []
    for idx, elm in enumerate(string):
        for delta in [x for x in range(n) if x != int(elm)]:
            temp = decnum + (delta-int(elm))*n**(len(string)-idx-1)
            if idx == 0 and delta == 0:
                continue
            arr.append(temp)
    print(arr)
    return arr

def func2():
    for _ in range(1,int(input())+1):
        binnum=ternum=0
        binary = input()
        ternary = input()
        for idx, num in enumerate(binary[::-1]): # 2진변환
            binnum += (2**idx)*int(num)
        for idx, num in enumerate(ternary[::-1]): # 3진변환
            ternum += (3**idx)*int(num)

        bindiff =func3(2,binary,binnum)
        terdiff =func3(3,ternary,ternum)
        ans = list(set(bindiff)&set(terdiff))
        if ans:
            print(f'#{_} {ans[0]}')
        else:
            print(f'#{_} {-1}')   



func2()