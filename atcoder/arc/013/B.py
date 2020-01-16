def main():
    C = int(input())
    N,M,L = [],[],[]
    for _ in range(C):
        ls = [int(x) for x in input().split()]
        n,m,l = sorted(ls)
        N.append(n)
        M.append(m)
        L.append(l)
    print(max(N)*max(M)*max(L))
    
if __name__ == '__main__':
    main()