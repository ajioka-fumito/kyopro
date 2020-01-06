import heapq
a = [3,0,2,6]
#listのheap化
#heapはsortではないので順番は割とあべこべになる。最小値は先頭
heapq.heapify(a)
print(a)

#挿入
heapq.heappush(a,3)
print(a)

#最小値を削除&出力
print(heapq.heappop(a))
print(a)