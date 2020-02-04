def jikan(lenth,v):
    return lenth/v
def kyori(v,time):
    return v*time

def solve(lenth,va,vb):
    time = jikan(lenth,va)
    sub = kyori(vb,time)
    return sub


def main():
    N,va,vb,L = map(int,input().split())

    for _ in range(N):
        L = solve(L,va,vb)
    
    L = float(L)
    print("{:.7f}".format(L))


if __name__ == "__main__":
    main()