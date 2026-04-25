class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = {}

        for task in tasks:
            if task not in task_freq:
                task_freq[task] = 1
            else:
                task_freq[task] += 1


        max_heap = [-cnt for cnt in task_freq.values()]
        heapq.heapify(max_heap)
        
        time = 0
        q = deque()  # (ready_time, remaining_count)
        
        while max_heap or q:
            time += 1
            
            if q and q[0][0] == time:
                heapq.heappush(max_heap, q.popleft()[1])
            
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt < 0:
                    q.append((time + n + 1, cnt))
        
        return time


        