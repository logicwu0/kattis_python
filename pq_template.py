# 堆
from heapq import heappush, heappop, heapify

k = 100
# 堆
pq = []

# 将数组转成堆
heapify(pq)

# 默认小顶堆
for i in range(k):
    heappush(pq, i)

# 删除堆顶元素
for i in range(k):
    heappop(pq)

# 常见堆题目基本够用
