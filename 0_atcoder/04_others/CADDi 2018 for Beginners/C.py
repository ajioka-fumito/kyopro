from collections import defaultdict
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

def main():
    N,P = map(int,input().split())
    ls = prime_decomposition(P)
    dic = defaultdict(int)
    for i in ls:
        dic[i] += 1
    ans = 1
    for i,j in dic.items():
        if N<=j:
            ans *= i
    print(ans)
if __name__ == '__main__':
    main()