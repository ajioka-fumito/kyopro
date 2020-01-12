def Warshall_Floyd(edges,N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                edges[i][j]=min(edges[i][j],edges[i][k]+edges[k][j])
    return edges


def main():
    H,W = map(int,input().split())
    ls = [list(input()) for _ in range(H)]
    for i in range(H):
        ls[i].insert(0,"#")
        ls[i].append("#")
    ls.append(["#" for _ in range(W+2)])
    ls.insert(0,["#" for _ in range(W+2)])
    graph = [[float("inf") for _ in range(H*W)] for _ in range(H*W)]

    for i in range(1,H+1):
        for j in range(1,W+1):
            if ls[i][j]==".":
                # ue
                if ls[i-1][j]==".":
                    graph[(i-1)*W+(j-1)][(i-2)*W+(j-1)] = 1
                    graph[(i-2)*W+(j-1)][(i-1)*W+(j-1)] = 1
                # migi
                if ls[i][j+1]==".":
                    graph[(i-1)*W+(j-1)][(i-1)*W+j] = 1
                    graph[(i-1)*W+j][(i-1)*W+(j-1)] = 1
                # sita
                if ls[i+1][j]==".":
                    graph[(i-1)*W+(j-1)][i*W+(j-1)] = 1
                    graph[i*W+(j-1)][(i-1)*W+(j-1)] = 1
                # hidari
                if ls[i][j-1]==".":
                    graph[(i-1)*W+(j-1)][(i-1)*W+(j-2)] = 1
                    graph[(i-1)*W+(j-2)][(i-1)*W+(j-1)] = 1
                else:
                    pass
    for i in range(H*W):
        
    a = Warshall_Floyd(graph,H*W)
    for i in range(H*W):
        for j in range(H*W):
            if a[i][j]==float("inf"):
                a[i][j]=0
    for i in range(H*W):
        a[i][i] = 0

    mx = 0
    for i in a:
        mx = max(mx,max(i))
    print(mx)
if __name__ == '__main__':
    main()