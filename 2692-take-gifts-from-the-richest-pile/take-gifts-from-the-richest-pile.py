import math
import heapq

class Solution:
    def pickGifts(self, gifts, k):
        pq = [-gift for gift in gifts]  
        heapq.heapify(pq)
        for _ in range(k):
            gift = -heapq.heappop(pq)
            left = int(math.floor(math.sqrt(gift)))
            heapq.heappush(pq, -left)
        return -sum(pq) 