def Warshall_Floyd(edges,N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                edges[i][j]=min(edges[i][j],edges[i][k]+edges[k][j])
    return edges

def main():
    N,M = map(int,input().split())
    edges = [[float("inf") for _ in range(N)] for _ in range(N)]
    for i in range(N):
        edges[i][i] = 0
    for _ in range(M):
        a,b,t = map(int,input().split())
        edges[a-1][b-1],edges[b-1][a-1] = t,t
    edges = Warshall_Floyd(edges,N)
    ans = float("inf")
    for i in range(N):
        ans = min(ans,max(edges[i]))
    print(ans)

if __name__ == "__main__":
    main()