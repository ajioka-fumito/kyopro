def main():
    N = int(input())
    H = int(input())
    W = int(input())
    ans = (N+1-H)*(N+1-W)
    print(ans)
if __name__ == '__main__':
    main()