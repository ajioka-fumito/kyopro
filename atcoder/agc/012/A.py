def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A = sorted(A,reverse=True)
    ans = 0
    for i in range(N):
        ans += A[2*i+1]
    print(ans)

if __name__ == "__main__":
    main()