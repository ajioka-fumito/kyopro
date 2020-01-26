# 深さ優先探索
"""
深さ優先探索:
探索手法の一つ.ある状態からはじめ、遷移できなくなるまで状態を変化させていき,遷移できなくなったら直前の状態に戻るということを繰り返す.
"""
# ex. 部分和問題 
# 2**N の状態数を考える
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

