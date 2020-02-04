import sys
input = sys.stdin.readline
#str 注意
def main():
    n,t = map(int,input().split())
    
    index = [0,0,0]
    ls_a,ls_b = [],[]
    aap,bap = ls_a.append,ls_b.append
    for i in range(n):
        a,b = map(int,input().split())
        aap(a)
        bap(b)
        if index[2]<b:
            index = [i,a,b]
        elif index[2]==b:
            if index[1]>a:
                index = [i,a,b]
            else:
                pass
        else:
            pass
    ls_a.pop(index[0])
    add = ls_b.pop(index[0])
    print(ls_a,ls_b)
    dp = [[0 for _ in range(t)] for _ in range(n-1)]

    for i in range(t):
        if ls_a[0]<= i:
            dp[0][i] = ls_b[0]
        else:
            pass
    


    for i in range(1,n-1):
        for j in range(t):
            if j>=ls_b[i]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-ls_b[i]]+ls_a[i])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n-2][-1]+add)

if __name__=='__main__':
    main()

