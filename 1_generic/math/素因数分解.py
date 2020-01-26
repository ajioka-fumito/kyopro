# 素因数分解 (list)
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

# 素因数分解 (taple)
def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

def prime_list(n,ls):
    i = 0
    table = []
    while ls[i]**2<=n:
        while n%ls[i]==0:
            n //= ls[i]
            table.append(ls[i])
        i += 1
    if n>1:
        table.append(n)
    return table
    
if __name__ == __name__:
    print(prime_decomposition(25))
    