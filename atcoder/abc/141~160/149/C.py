def makePrimeChecker(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    return isPrime

def main():
    N = int(input())
    ls = makePrimeChecker(10**6)
    for i in range(N,10**6+1):
        if ls[i]:
            print(i)
            exit()
        

if __name__ == '__main__':
    main()