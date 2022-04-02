# Leetcode 239. Sliding Window Maximum
#
# Link: https://leetcode.com/problems/sliding-window-maximum/
# Difficulty: Hard

# Solution using a monotonically decreasing queue (deque based)
# Complexity:
#   O(N) time | where N represent the number of elements in the input list
#   O(k) space | where k represent the windows size
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_queue = deque()  # monotonically decreasing queue
                             # containing indexes, since we need to remove
                             # elements out of bound
        result = []

        for i in range(len(nums)):

            # remove elements in queue less than current value
            while max_queue and nums[max_queue[-1]] < nums[i]:
                max_queue.pop()

            max_queue.append(i)

            # remove the left value if out of scope
            if max_queue and max_queue[0] == i - k:
                max_queue.popleft()

            # update result only when window is ready
            if i >= k - 1:
                result.append(nums[max_queue[0]])

        return result
