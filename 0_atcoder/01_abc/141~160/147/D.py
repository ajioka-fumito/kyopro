import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ls_now = [0 for i in range(61)]
    ans = [0 for i in range(61)]
    for i in range(n):
        now = a[(n-1)-i]
        now = str(bin(now))[2:]
        now = now.zfill(61)
        roop = i+1
        for digit,j in enumerate(reversed(now)):
            ls_now[digit] += int(j)
        
        
    
        for digit,j in enumerate(reversed(now)):
            if j=="1":
                ans[digit] += (roop-ls_now[digit])
            else:
                ans[digit] += ls_now[digit]
    A = 0
    for i in range(1,61):
        A += i*ans[i]
    sub = ans[0]
    ans = 1
    
    print(A)
    for _ in range(A):
        ans = (ans*2)%(10**9+7)
    ans += sub
    print(ans)            

if __name__ == "__main__":
    main()