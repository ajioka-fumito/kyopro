import fractions
def main():
    mod = 10**9 + 7
    N = int(input())
    A = [int(x) for x in input().split()]
    sub = A[0]
    for i in A:
        sub = sub * i // fractions.gcd(sub, i)
    ans = 0
    for i in range(N):
        ans += sub//A[i]
        ans %= mod
    print(ans%mod)
if __name__ == '__main__':
    main()