def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A = sorted(A)

    now = N
    A_cumsum = [A[0]]
    for i in range(1,N):
        A_cumsum.append(A_cumsum[-1]+A[i])
    ans = 0
    for i in range(1,N):
        if A_cumsum[i-1]*2>=A[i]:
            pass
        else:
            ans = i
    print(N-ans)

if __name__ == "__main__":
    main()

