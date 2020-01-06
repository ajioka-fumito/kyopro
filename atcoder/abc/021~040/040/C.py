def main():
    n = int(input())
    ls = [int(x) for x in input().split()]
    ans = [0 for _ in range(n)]
    # 1本目,2本目
    ans[1] = abs(ls[1]-ls[0])
    for i in range(2,n):
        p1 = ans[i-2]+abs(ls[i]-ls[i-2])
        p2 = ans[i-1]+abs(ls[i]-ls[i-1])
        if p1<=p2:
            ans[i] = p1
        else:
            ans[i] = p2
    print(ans[-1])
if __name__=='__main__':
    main()