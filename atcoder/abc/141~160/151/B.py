def main():
    N,K,M = map(int,input().split())
    A = [int(x) for x in input().split()]
    sub = N*M - sum(A)
    if sub>K:
        print(-1)
    else:
        print(max(sub,0))

if __name__ == '__main__':
    main()