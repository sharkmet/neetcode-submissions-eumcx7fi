class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for x, y in points:
            # x = point[0]
            # y = point[1]
            heapq.heappush(heap, (math.sqrt((x)**2 + (y)**2), x, y))
        
        for _ in range(k):
            p = heapq.heappop(heap)
            result.append([p[1], p[2]])

        return result
        