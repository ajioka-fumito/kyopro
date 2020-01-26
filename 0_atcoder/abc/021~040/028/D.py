def main():
    n,k = map(int,input().split())
    ans1 = -2-3*n+6*k*n+6*k-6*k**2
    ans2 = n**3
    print(ans1/ans2)
if __name__ == "__main__":
    main()