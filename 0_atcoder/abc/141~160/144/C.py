import sys
import math
input = sys.stdin.readline
#str 注意
def main():
    n = int(input())
    root = int(math.sqrt(n))
    ans = 10**100
    for i in range(1,root+1):
        if n%i==0:
            ans = min(ans,i+n//i)
        else:
            pass
    print(ans-2)

if __name__=='__main__':
    main()