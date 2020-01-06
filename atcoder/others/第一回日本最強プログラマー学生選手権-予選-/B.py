from collections import defaultdict
from bisect import bisect_left
def bubble_sort(A):
    cnt = 0
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                cnt += 1
    return cnt

def main():
    N,K = map(int,input().split())
    A = [int(x) for x in input().split()]
    mod = 10**9 + 7
    
    falls = bubble_sort(A)
    rank = 0
    for i in A:
        rank += bisect_left(A,i)

    falls_all = (falls*K)%mod
    rank_all  = ((K*(K-1))//2)%mod
    rank_all  = (rank_all*rank)%mod

    print((falls_all+rank_all)%mod) 
    
if __name__ == "__main__":
    main()