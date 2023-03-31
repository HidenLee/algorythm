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

        for num in [x for x in range(2**(len(binary)-1),2**len(binary)+1) if 3**(len(ternary)-1)<=x<3**len(ternary)]: # 같은 자릿수임
            if abs(num-binnum) in bindiff and abs(num-ternum) in terdiff:
                print(f'#{_} {num}')
                break
        else:
            print(-1)   