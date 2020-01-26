# nまでの自然数が素数かどうかを表すリストを返す
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
    n = int(input())
    prime_ls = makePrimeChecker(55555)
    ans = []
    i = 2
    while 1:
        if len(ans)==n:
            break
            
        if prime_ls[i] and i%5==1:
            ans.append(i)
        else:
            pass
        i += 1
    

    for ans_ in ans:
        print(ans_,end=" ")
    print("\n")



if __name__ == "__main__":
    main()