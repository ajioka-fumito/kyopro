n = 4
a = [1,2,4,7]
k = 13

def dfs(i,add):
    if i==n:
        return add==k
    if dfs(i+1,add):
        return True
    if dfs(i+1,add+a[i]):
        return True
    return False

print(dfs(0,0))
    