import sys
input = sys.stdin.readline

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    ls = [0 for _ in range(N)]
    ans = 0
    mins = 10**10
    for i in range(N):
        mins = min(mins,P[i])
        if mins==P[i]:
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()