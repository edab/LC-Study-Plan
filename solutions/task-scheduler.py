# Leetcode 621. Task Scheduler
#
# Link: https://leetcode.com/problems/task-scheduler/
# Difficulty: Medium

# Solution using min_heap and queue
# Complexity:
#   O(N*M) | where N represent the number of tasks and M the interval
#   O(N) space
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_count = Counter(tasks) # only # of similar tasks count
        task_heap = [-count for count in task_count.values()]
        heapq.heapify(task_heap)

        q = deque() # pair of (-count, idleTime)
        time = 0

        while task_heap or q:

            time += 1

            # if we have tasks to process, we add 1 (it's a min_heap)
            if task_heap:
                count = 1 + heapq.heappop(task_heap)
                if count:
                    # we save the task in a queue and wait the interval
                    q.append([count, time + n])

            # If idletime is passed, we put the task back to the heap
            if q and q[0][1] == time:
                heapq.heappush(task_heap, q.popleft()[0])

        return time
