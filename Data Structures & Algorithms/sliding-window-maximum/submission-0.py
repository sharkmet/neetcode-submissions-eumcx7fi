class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque() # stores indices, decreasing by value

        for r in range(len(nums)):
            # pop from back anything smaller than current
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            # pop from front if it's outside the window
            if dq[0] < r - k + 1:
                dq.popleft()

            # only record once first window is complete
            if r >= k - 1:
                result.append(nums[dq[0]])

        return result