import sys
input = sys.stdin.readline
#str 注意
def main():
    n,k = map(int,input().split())
    d = [x for x in input().split()]
    d = set(d)

    while 1:
        if len(set(list(str(n))) & d)==0:
            print(n)
            exit()
        else:
            n +=1

if __name__=='__main__':
    main()