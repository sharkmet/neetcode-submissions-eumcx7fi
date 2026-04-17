class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A) - 1

        while True: #A valid partition is guaranteed to exist, so the loop will always hit the return statement. No need for a termination condition.
            i = (l + r) // 2              # partition point in A
            j = half - i - 2              # partition point in B (-2 because i,j are 0-indexed) -> (i + 1) + (j + 1) = half -> i + j + 2 = half -> j = half - i - 2

            A_left  = A[i]   if i >= 0 else float('-inf')       #A:  ... A[i-1]  A[i]  |  A[i+1]  A[i+2] ...
            A_right = A[i+1] if i+1 < len(A) else float('inf')  #              A_left  |  A_right
            B_left  = B[j]   if j >= 0 else float('-inf')
            B_right = B[j+1] if j+1 < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right: # valid partition
                if total % 2:
                    return min(A_right, B_right)
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right: #If A_left_max > B_right_min → took too much from A → search left (r = mid - 1)
                r = i - 1
            else: #If B_left_max > A_right_min → took too little from A → search right (l = mid + 1)
                l = i + 1
                
