import sys
input = sys.stdin.readline
def main():
    # input
    N,W = map(int,input().split())
    w,v = [0]*N,[0]*N
    for i in range(N):
        w[i],v[i] = map(int,input().split())

    # init dp
    v_max = sum(v)
    dp = [[float("inf") for i in range(v_max+1)] for _ in range(N)]
    dp[0][v[0]] = w[0]
    for i in range(N):
        dp[i][0] = 0

    for i in range(1,N):
        for j in range(v_max+1):
            if j<v[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-v[i]]+w[i])
    ans = 0
    for i in range(v_max+1):
        if dp[-1][i]<=W:
            ans = i
        else:
            pass
    print(ans)
if __name__ == "__main__":
    main()
