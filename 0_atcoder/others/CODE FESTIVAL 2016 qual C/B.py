import heapq
def main():
    K,T = map(int,input().split())
    A = [-int(x) for x in input().split()]
    if T == 1:
        print(K-1)
        exit()

    heapq.heapify(A)
    first = heapq.heappop(A)
    while 1:
        second = heapq.heappop(A)
        if second==0:
            break
        else:
            heapq.heappush(A,first+1)
            first = second
    print(-first-1)
    
if __name__ == '__main__':
    main()