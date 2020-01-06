from collections import defaultdict
def main():
    ls = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic_str = defaultdict(int)
    dic_num = defaultdict(str)
    for i,st in enumerate(ls):
        dic_str[i] = st
        dic_num[st] = i
    n = int(input())
    s = input()
    ans = ""
    for i in s:
        num = dic_num[i]
        if num+n>25:
            num -= 26
        ans = ans + str(dic_str[int(num)+n])
    print(ans)

if __name__=='__main__':
    main()