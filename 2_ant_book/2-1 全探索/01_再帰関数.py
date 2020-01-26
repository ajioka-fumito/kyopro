import time
# 再帰関数
"""
順列計算
"""
def fact(N):
    if N==0: # 呼び出しを止める条件式
        return 1
    return N*fact(N-1)
"""
フィボナッチ数列
"""
def fib1(N):
    if N<=1:
        return N
    return fib1(N-2)+fib1(N-1)
"""
ここで呼び出し回数を削減するためにメモ化のテクニックを導入する
"""
class fib2:
    def __init__(self,N):
        self.memo = [0 for i in range(N+1)]

    def main(self,N):
        if N<=1:
            return N
        if self.memo[N]!=0:
            return self.memo[N]
        else:
            self.memo[N] = self.main(N-1) + self.main(N-2)
            return self.memo[N]

if __name__ == "__main__":
    print()
    print("5! = 120")
    print("5! =",fact(5))
    print()
    print("fib(30) = 832040" )
    s = time.time()
    print("fib(30) =",fib1(30)) 
    print("処理にかかった時間:",time.time()-s) 
    print()
    s = time.time()
    print("fib(30) =",fib2(30).main(30))
    print("処理にかかった時間:",time.time()-s)
