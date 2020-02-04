def main():
    N = int(input())
    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            ans += i*j
    
    sub = ans-N
    for i in range(1,10):
        for j in range(1,10):
            if sub == i*j:
                print("{0} x {1}".format(i,j))
    
if __name__ == "__main__":
    main()