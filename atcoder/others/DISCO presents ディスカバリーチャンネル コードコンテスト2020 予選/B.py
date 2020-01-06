import bisect
import math
def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A_sum = sum(A)
    A_cumsum_l = [0 for _ in range(N)]
    A_cumsum_l[0] = A[0]
    for i in range(1,N):
        A_cumsum_l[i] = A_cumsum_l[i-1] + A[i]
    A_cumsum_r = [0 for _ in range(N)]
    for i in range(N):
        A_cumsum_r[i] = A_sum - A_cumsum_l[i]
    
    index = 0
    sub = 10**12
    for i in range(N):
        if abs(A_cumsum_l[i]-A_cumsum_r[i])<sub:
            index = i
            sub = abs(A_cumsum_l[i]-A_cumsum_r[i])


    print(sub)


if __name__ == "__main__":
    main()