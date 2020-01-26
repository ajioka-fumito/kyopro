import sys
input = sys.stdin.readline
import heapq
def main():
    N = int(input())
    a = [int(x) for x in input().split()]
    left = [0]*(N+1)
    left_a = a[:N]
    left[0] = sum(left_a)

    heapq.heapify(left_a)
    for i in range(1,N+1):
        now = heapq.heappop(left_a)

        if now<a[N-1+i]:
            heapq.heappush(left_a,a[N-1+i])
            left[i] = left[i-1]+a[N-1+i]-now
        else:
            heapq.heappush(left_a,now)
            left[i] = left[i-1]
    
    right = [0]*(N+1)
    right_a = [-int(x) for x in a[2*N:]]
    right[-1] = -sum(right_a)
    
    heapq.heapify(right_a)
    for i in range(N):
        now = -1 * heapq.heappop(right_a)
        if now>a[2*N-1-i]:
            heapq.heappush(right_a,-a[2*N-1-i])
            right[N-i-1] = right[N-i]-now+a[2*N-1-i]
        else:
            heapq.heappush(right_a,-now)
            right[N-i-1] = right[N-i]

    ans = -1 * float("inf")
    for i in range(len(left)):
        ans = max(ans,left[i]-right[i])
    print(ans)



if __name__ == "__main__":
    main()