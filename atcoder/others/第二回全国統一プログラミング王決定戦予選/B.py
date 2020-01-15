from collections import defaultdict
def main():
    N = int(input())
    D = [int(x) for x in input().split()]
    dic = defaultdict(int)
    for i in D:
        dic[i] += 1

    if dic[0]!=1:
        print(0)
        exit()
    ans = 1
    for i in range(1,max(dic.keys())+1):
        ans *= dic[i-1]**dic[i]
    print(ans)    
if __name__ == '__main__':
    main()