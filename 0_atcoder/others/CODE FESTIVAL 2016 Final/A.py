from collections import defaultdict
def main():
    H,W = map(int,input().split())
    ls = [[str(x) for x in input().split()] for _ in range(H)]
    dic = defaultdict(str)
    for i,now in enumerate([chr(i) for i in range(65, 65+26)]):
        dic[i] = now

    for i in range(H):
        for j in range(W):
            if ls[i][j]=="snuke":
                ans = dic[j]+str(i+1)
                print(ans)
                exit()
if __name__ == '__main__':
    main()