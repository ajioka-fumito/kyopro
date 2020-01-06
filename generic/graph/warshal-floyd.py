def Warshall_Floyd(edges,N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                edges[i][j]=min(edges[i][j],edges[i][k]+edges[k][j])
    return edges