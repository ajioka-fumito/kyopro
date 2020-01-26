# スタック
"""
最後に追加された要素を最初に(O(1)で)取り出すことができるデータ構造
LIFO : last in first out
python では標準Listが対応しているが後述するcollections.dequeで実装することも可能
"""
def sample_stack():
    stack = [1,2,3]
    print("stack:",stack)
    stack.append(4)
    print("stack:",stack)
    stack.append(5)
    print("stack:",stack)
    stack.pop()
    print("stack:",stack)

# キュー
"""
要素を最後尾に追加し,先頭の要素を取り出すことができるデータ構造
FIFO : first in first out
python ではcollections.dequeで実装
"""
from collections import deque
def sample_queue():
    queue = deque([1,2,3])
    print("queue:",queue)
    queue.append(4)
    print("queue:",queue)
    queue.append(5)
    print("queue:",queue)
    queue.popleft()
    print("queue:",queue)

if __name__ == "__main__":
    sample_stack()
    print()
    sample_queue()