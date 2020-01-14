import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        A_cumsum =[0]
        for i in range(N):
            A_cumsum.append(A_cumsum[-1]+A[i])
        target = sum(A)
        
    if A[0]<0 or A[1]<0:
        print("No")
    else:
        
        
if __name__ == '__main__':
    main()