def main():
    w = int(input())
    n,K = map(int,input().split())
    ls = [[int(x) for x in input().split()] for _ in range(n)]
    dp = [[[0 for _ in range(w+1)] for _ in range(n+1)] for _ in range(n)]

    for k in range(w+1):
        if ls[0][0]<=k:
            dp[0][1][k]=ls[0][1]

    for i in range(1,n):
        for j in range(1,n+1):
            for k in range(w+1):
                if k<ls[i][0]:
                    dp[i][j][k] = dp[i-1][j][k]
                else:
                    dp[i][j][k] = max(dp[i-1][j][k],
                                      dp[i-1][j-1][k-ls[i][0]]+ls[i][1])
    print(dp[n-1][K][w])


if __name__ == "__main__":
    main()