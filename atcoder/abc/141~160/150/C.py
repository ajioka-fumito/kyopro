import itertools
from collections import defaultdict
# 順列生成
def permutation(list_):
    return list(itertools.permutations(list_))

def main():
    N = int(input())
    P = "".join([str(x) for x in input().split()])
    Q = "".join([str(x) for x in input().split()])
    
    ls = [ "".join(i) for i in permutation([str(i+1) for i in range(N)])]
    dic = defaultdict(int)
    for num,i in enumerate(ls):
        dic[i] = (num+1)
    print(abs(dic[P]-dic[Q]))
    
if __name__ == '__main__':
    main()