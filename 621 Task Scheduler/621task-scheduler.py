class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-count, task) for task, count in Counter(tasks).items()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while heap or queue:
            if queue and queue[0][0] == time:
                time, count, task = queue.popleft()
                heapq.heappush(heap, (count, task))
            if heap:
                count, task = heapq.heappop(heap)
                count += 1
                if count != 0:
                    queue.append((time + n + 1, count, task))
            time += 1
        return time
