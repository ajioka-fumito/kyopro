def main():
    n,x  = map(int,input().split())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(1,n):
        if a[i]+a[i-1]<=x:
            pass
        else:
            if (a[i]+a[i-1])-x<=a[i]:
                ans += (a[i]+a[i-1])-x
                a[i] -= (a[i]+a[i-1])-x
            else:
                ans += (a[i]+a[i-1])-x 
                a[i] = 0
    print(ans)
if __name__ == "__main__":
    main()