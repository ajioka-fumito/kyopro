import math
def distance(x1,y1,x2,y2):
    x = pow(abs(x1-x2),2)
    y = pow(abs(y1-y2),2)
    return math.sqrt(x+y)

import itertools
# 順列生成
def permutation(list_):
    return list(itertools.permutations(list_))

def main():
    n = int(input())
    x,y = [0 for _ in range(n)],[0 for _ in range(n)]
    for i in range(n):
        x[i],y[i] = map(int,input().split())
    
    can = permutation(list(range(n)))

    all_path = 0
    for ls in can:
        path = 0
        for i in range(1,len(ls)):
            path += distance(x[ls[i-1]],y[ls[i-1]],x[ls[i]],y[ls[i]])
        all_path += path
    print(all_path/len(can))

if __name__=='__main__':
    main()