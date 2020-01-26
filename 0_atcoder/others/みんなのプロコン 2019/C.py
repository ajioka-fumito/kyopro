def main():
    K,A,B = map(int,input().split())
    if B-A<=2:
        print(1+K)
        exit()
    now = 1
    K -= (A-1)
    now = A
    if K%2==0:
        now += (B-A)*(K//2)
    else:
        now += (B-A)*((K-1)//2)
        now += 1
    print(now)  
if __name__ == '__main__':
    main()