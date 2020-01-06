import sys
input = sys.stdin.readline
def main():
    n = int(input())
    ls = [[int(i+1),int(j)] for i,j in enumerate(input().split())]
    ls = sorted(ls,key=lambda x:-x[1])
    for i in range(n):
        print(ls[i][0])
if __name__=='__main__':
    main()