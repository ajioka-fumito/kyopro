from collections import defaultdict

def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
    
def prime_list(n,ls):
    i = 0
    table = defaultdict(int)
    while ls[i]**2<=n:
        while n%ls[i]==0:
            n //= ls[i]
            table[ls[i]] += 1
        i += 1
    if n>1:
        table[n] += 1
    return table
    

def main():
    mod = 10**9 + 7
    N = int(input())
    A = [int(x) for x in input().split()]
    dic = defaultdict(int)
    eranes = eratosthenes(10**6)
    
    for i in A:
        prime = prime_list(i,eranes)
        for j,k in prime.items():
            if dic[j]<=k:
                dic[j] = k
            else:
                pass
    sub = 1
    for i,j in dic.items():
        sub *= i**j
    ans = 0
    for i in A:
        ans += sub//i
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()