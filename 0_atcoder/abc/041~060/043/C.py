import sys
input = sys.stdin.readline
#str 注意
def main():
    n = int(input())
    ls = [int(x) for x in input().split()]
    ans = 10**10
    for i in range(-100,101):
        can = 0
        for j in range(n):
            can += (ls[j]-i)**2
        if can<=ans:
            ans = can
    print(ans)
if __name__=='__main__':
    main()
