import sys
input = sys.stdin.readline
#str 注意
def main():
    n = int(input())
    ls = []
    lsa = ls.append
    for _ in range(n-1):
        a,b = map(int,input().split())
        lsa([a-1,b-1])


    ans_1 = [0 for _ in range(n)]
    for ls_ in ls:
        ans_1[ls_[0]] +=1
        ans_1[ls_[1]] +=1
    print(max(ans_1))
    
    for ls_ in ls:

        

    
if __name__=='__main__':
    main()