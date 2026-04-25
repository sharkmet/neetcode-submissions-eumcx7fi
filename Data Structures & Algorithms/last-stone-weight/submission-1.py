class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while True:
            if len(stones) == 0:
                return 0
            elif len(stones) == 1:
                return -stones[0]

            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)

            if s1 < s2:
                heapq.heappush(stones, -(s2 - s1))
            elif s1 > s2:
                heapq.heappush(stones, -(s1 - s2))


        