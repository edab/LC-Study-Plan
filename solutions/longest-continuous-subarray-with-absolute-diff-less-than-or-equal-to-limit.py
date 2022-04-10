# Leetcode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
# Link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# Difficulty: Medium

# Solution using two monotonically decreasing queue (deque based)
# Complexity:
#   O(N) time | where N represent the number of elements in the input list
#   O(N) space | where N represent the number of elements in the input list
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        min_queue, max_queue = deque([0]), deque([0])

        left, right = 0, 0

        longestSubarray = 0

        while right < len(nums):

            # Move right
            longestSubarray = max(longestSubarray, right - left + 1)
            right += 1

            # Maintain queues monotonic
            if right < len(nums):

                while min_queue and nums[min_queue[-1]] > nums[right]:
                    min_queue.pop()

                while max_queue and nums[max_queue[-1]] < nums[right]:
                    max_queue.pop()

                max_queue.append(right)
                min_queue.append(right)

            # Move left
            while max_queue and min_queue and nums[max_queue[0]] - nums[min_queue[0]] > limit and left <= right:
                left += 1
                while max_queue and max_queue[0] < left:
                    max_queue.popleft()

                while min_queue and min_queue[0] < left:
                    min_queue.popleft()

        return longestSubarray
