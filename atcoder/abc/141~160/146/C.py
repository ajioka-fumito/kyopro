def main():
    a,b,x = map(int,input().split())
    if a*(10**9)+b*10 <= x:
        print(10**9)
        exit()
    ans = 0

    right = 10**9
    left = 1
    while 1:
        if left==right:
            if a*right+b*(len(str(right))) <= x:
                print(right)
                exit()
            else:
                print(left-1)
                exit()
        elif left+1 == right:
            if a*right+b*(len(str(right))) <= x:
                print(right)
                exit()
            elif a*left+b*(len(str(left))) <= x:
                print(left)
                exit()
        mid = int((right+left)/2)
        if x == a*(mid)+b*(len(str(mid))):
            print(mid)
            exit()
        elif x<= a*(mid)+b*(len(str(mid))):
            right = mid
        else:
            left = mid
if __name__=='__main__':
    main()