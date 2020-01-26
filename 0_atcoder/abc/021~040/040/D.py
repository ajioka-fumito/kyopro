class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
import sys
input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    path = [[int(x) for x in input().split()] for _ in range(m)]
    path = sorted(path,key=lambda x:-x[2])
    q = int(input())
    ls = [[int(i),0,0] for i in range(q)]

    for i in range(q):
        ls[i][1],ls[i][2] = map(int,input().split())
    
    ls = sorted(ls,key=lambda x:-x[2])
    ans = [0 for _ in range(q)]
    tree = UnionFind(n)
    key = 0

    for now in ls:
        while 1:
            if key==m:
                break
            if now[2]<path[key][2]:
                tree.union(path[key][0]-1,path[key][1]-1)
                key += 1
            else:
                break
        ans[now[0]] = tree.size(now[1]-1)

    for i in range(q):
        print(ans[i])

if __name__=='__main__':
    main()