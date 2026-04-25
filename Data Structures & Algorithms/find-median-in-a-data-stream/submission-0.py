class MedianFinder:

    def __init__(self):
        self.lmax_heap = []  # max-heap (stores negatives), holds smaller half
        self.rmin_heap = []  # min-heap, holds larger half
        
    def addNum(self, num: int) -> None:
        if not self.lmax_heap and not self.rmin_heap:
            heapq.heappush(self.rmin_heap, num)
            return

        if num > self.rmin_heap[0]:
            heapq.heappush(self.rmin_heap, num)
        else:
            heapq.heappush(self.lmax_heap, -num)

        if abs(len(self.lmax_heap) - len(self.rmin_heap)) > 1:
            if len(self.lmax_heap) > len(self.rmin_heap):
                heapq.heappush(self.rmin_heap, (-heapq.heappop(self.lmax_heap)))
            else:
                heapq.heappush(self.lmax_heap, (-heapq.heappop(self.rmin_heap)))
        
    def findMedian(self) -> float:
        if (len(self.lmax_heap) + len(self.rmin_heap)) % 2 == 0:
            return (-self.lmax_heap[0] + self.rmin_heap[0]) / 2
        elif len(self.lmax_heap) > len(self.rmin_heap):
            return -self.lmax_heap[0]
        else:
            return self.rmin_heap[0]