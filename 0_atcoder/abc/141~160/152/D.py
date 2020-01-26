def main():
    N = int(input())
    ls = [[0 for _ in range(10)] for _ in range(10)]
    ans = 0
    for i in range(1,N+1):
        b,a = int(str(i)[0]),int(str(i)[-1])

        if a==b:
            ans += 2*ls[a][b]+1
            
        else:
            ans += 2*ls[a][b]

        ls[b][a] += 1

    print(ans)

        
if __name__ == '__main__':
    main()